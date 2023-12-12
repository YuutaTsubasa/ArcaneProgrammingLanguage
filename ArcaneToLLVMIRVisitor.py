from ArcaneParser import ArcaneParser
from ArcaneVisitor import ArcaneVisitor
from llvmlite import ir
from llvmlite.ir.instructions import AllocaInstr
from Definitions.TypeDefinition import TypeDefinition
from Definitions.ValueDefinition import ValueDefinition
from Definitions.VariableDefinition import VariableDefinition

class ArcaneToLLVMIRVisitor(ArcaneVisitor):
    def __init__(self):
        self.module = ir.Module()
        self.builder = None
        self.variables = {}

    def get_rvalue(self, definition):
        return (ValueDefinition(self.builder.load(definition.addr), definition.type)
                if isinstance(definition, VariableDefinition) 
                else definition)

    def visitProg(self, ctx:ArcaneParser.ProgContext):
        func_type = ir.FunctionType(
            ir.IntType(32),
            ())
        func = ir.Function(
            self.module,
            func_type,
            name="main")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        
        for stat in ctx.stat():
            self.visit(stat)

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))

        return self.module

    def visitStat(self, ctx:ArcaneParser.StatContext):
        self.visitExpr(ctx.expr())

    def visitVarDeclaration(self, ctx:ArcaneParser.VarDeclarationContext):
        var_name = ctx.ID().getText()
        var_type = ctx.TYPE().getText()

        llvm_var_type = TypeDefinition(var_type).get_llvm_type()

        alloca = self.builder.alloca(llvm_var_type, name=var_name)

        init_value = self.visit(ctx.expr())
        self.builder.store(self
                           .get_rvalue(init_value)
                           .convert_to(self.builder, var_type)
                           .value, alloca)

        is_mutable = ctx.VAR().getText() == "var"
        self.variables[var_name] = VariableDefinition(
            var_name, 
            alloca, 
            TypeDefinition(var_type),
            is_mutable)
        return self.variables[var_name]
        
    def visitAssignment(self, ctx:ArcaneParser.AssignmentContext):
        if ctx.ID() is not None:
            var_name = ctx.ID().getText() 

            if var_name in self.variables:
                variable_definition = self.variables[var_name]
            
            if not variable_definition.is_mutable:
                raise Exception(f"Variable '{var_name}' is immutable and cannot be reassigned")
        elif ctx.varDeclaration() is not None:
            variable_definition = self.visitVarDeclaration(ctx.varDeclaration())
        else:
            raise Exception(f"Undefined variable '{var_name}'")

        expr_value = self.get_rvalue(self.visit(ctx.expr())).convert_to(self.builder, variable_definition.type)
        self.builder.store(expr_value.value, variable_definition.addr)

        return variable_definition
    
    def visitExpr(self, ctx:ArcaneParser.ExprContext):
        if ctx.getChildCount() == 3:
            lhs = self.get_rvalue(self.visit(ctx.getChild(0)))
            rhs = self.get_rvalue(self.visit(ctx.getChild(2)))
            target_type = TypeDefinition.get_convertible_type(lhs.type, rhs.type)
            lhs = lhs.convert_to(self.builder, target_type)
            rhs = rhs.convert_to(self.builder, target_type)
            op = ctx.getChild(1).getText()

            match op:
                case '+': return lhs.add(self.builder, rhs)
                case '-': return lhs.sub(self.builder, rhs)
                case '*': return lhs.mul(self.builder, rhs)
                case '/': return lhs.div(self.builder, rhs)
                case '%': return lhs.rem(self.builder, rhs)
        else:
            if ctx.varDeclaration() is not None:
                return self.visitVarDeclaration(ctx.varDeclaration())

            if ctx.assignment() is not None:
                return self.visitAssignment(ctx.assignment())

            if ctx.getChild(0).getText() == "return":
                return_value = self.visit(ctx.getChild(1))
                self.builder.ret(self
                                 .get_rvalue(return_value)
                                 .convert_to(self.builder, TypeDefinition.Int32)
                                 .value)
                return return_value

            return self.visitAtom(ctx.atom())
        
    def visitAtom(self, ctx:ArcaneParser.AtomContext):
        if ctx.INT():
            value = int(ctx.INT().getText())
            if value >= -128 and value <= 127:
                return ValueDefinition(ir.Constant(ir.IntType(8), value), TypeDefinition.Int8)
            if value >= -32768 and value <= 32767:
                return ValueDefinition(ir.Constant(ir.IntType(16), value), TypeDefinition.Int16)
            if value >= -2147483648 and value <= 2147483647:
                return ValueDefinition(ir.Constant(ir.IntType(32), value), TypeDefinition.Int32)
            if value >= -9223372036854775808 and value <= 9223372036854775807:
                return ValueDefinition(ir.Constant(ir.IntType(64), value), TypeDefinition.Int64)
            raise Exception(f"Value {value} is too long to be stored.")
        
        if ctx.FLOAT():
            value = float(ctx.FLOAT().getText())
            return ValueDefinition(ir.Constant(ir.FloatType(), value), TypeDefinition.Float32)
        
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise Exception(f"Undefined variable '{var_name}'")
            
        if ctx.BOOL():
            value = ctx.BOOL().getText() == 'true'
            return ValueDefinition(ir.Constant(ir.IntType(1), 1 if value else 0), TypeDefinition.Bool)

        if ctx.expr():
            return self.visit(ctx.expr())
            