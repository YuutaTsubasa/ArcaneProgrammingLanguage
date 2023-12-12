from Definitions.TypeDefinition import TypeDefinition
from llvmlite import ir

class ValueDefinition:
    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type

    def add(self, builder, rhs):
        if self.type.is_integer() and rhs.type.is_integer():
            value = builder.add(self.value, rhs.value)
        elif self.type.is_float() and rhs.type.is_float():
            value = builder.fadd(self.value, rhs.value)
        else:
            raise Exception(f"Can not `add` on {self.type} and {rhs.type}.")
        return ValueDefinition(value, self.type)
    
    def sub(self, builder, rhs):
        if self.type.is_integer() and rhs.type.is_integer():
            value = builder.sub(self.value, rhs.value)
        elif self.type.is_float() and rhs.type.is_float():
            value = builder.fsub(self.value, rhs.value)
        else:
            raise Exception(f"Can not `sub` on {self.type} and {rhs.type}.")
        return ValueDefinition(value, self.type)
    
    def mul(self, builder, rhs):
        if self.type.is_integer() and rhs.type.is_integer():
            value = builder.mul(self.value, rhs.value)
        elif self.type.is_float() and rhs.type.is_float():
            value = builder.fmul(self.value, rhs.value)
        else:
            raise Exception(f"Can not `mul` on {self.type} and {rhs.type}.")
        return ValueDefinition(value, self.type)
    
    def div(self, builder, rhs):
        if self.type.is_integer() and rhs.type.is_integer():
            value = builder.sdiv(self.value, rhs.value)
        elif self.type.is_float() and rhs.type.is_float():
            value = builder.fdiv(self.value, rhs.value)
        else:
            raise Exception(f"Can not `div` on {self.type} and {rhs.type}.")
        return ValueDefinition(value, self.type)
    
    def rem(self, builder, rhs):
        if self.type.is_integer() and rhs.type.is_integer():
            value = builder.srem(self.value, rhs.value)
        elif self.type.is_float() and rhs.type.is_float():
            value = builder.frem(self.value, rhs.value)
        else:
            raise Exception(f"Can not `rem` on {self.type} and {rhs.type}.")
        return ValueDefinition(value, self.type)

    def convert_to(self, builder, type):
        if type == self.type:
            return self
        
        match self.type:
            case TypeDefinition.Int8:
                match type:
                    case TypeDefinition.Int16:
                        return ValueDefinition(builder.zext(self.value, ir.IntType(16)), TypeDefinition.Int16)
                    case TypeDefinition.Int32:
                        return ValueDefinition(builder.zext(self.value, ir.IntType(32)), TypeDefinition.Int32)
                    case TypeDefinition.Int64:
                        return ValueDefinition(builder.zext(self.value, ir.IntType(64)), TypeDefinition.Int64)
                    case TypeDefinition.Float32:
                        return ValueDefinition(builder.sitofp(self.value, ir.FloatType()), TypeDefinition.Float32)
                    case TypeDefinition.Float64:
                        return ValueDefinition(builder.sitofp(self.value, ir.DoubleType()), TypeDefinition.Float64)
            case TypeDefinition.Int16:
                match type:
                    case TypeDefinition.Int32:
                        return ValueDefinition(builder.zext(self.value, ir.IntType(32)), TypeDefinition.Int32)
                    case TypeDefinition.Int64:
                        return ValueDefinition(builder.zext(self.value, ir.IntType(64)), TypeDefinition.Int64)
                    case TypeDefinition.Float32:
                        return ValueDefinition(builder.sitofp(self.value, ir.FloatType()), TypeDefinition.Float32)
                    case TypeDefinition.Float64:
                        return ValueDefinition(builder.sitofp(self.value, ir.DoubleType()), TypeDefinition.Float64)
            case TypeDefinition.Int32:
                match type:
                    case TypeDefinition.Int64:
                        return ValueDefinition(builder.zext(self.value, ir.IntType(64)), TypeDefinition.Int64)
                    case TypeDefinition.Float32:
                        return ValueDefinition(builder.sitofp(self.value, ir.FloatType()), TypeDefinition.Float32)
                    case TypeDefinition.Float64:
                        return ValueDefinition(builder.sitofp(self.value, ir.DoubleType()), TypeDefinition.Float64)
            case TypeDefinition.Int64:
                match type:
                    case TypeDefinition.Float32:
                        return ValueDefinition(builder.sitofp(self.value, ir.FloatType()), TypeDefinition.Float32)
                    case TypeDefinition.Float64:
                        return ValueDefinition(builder.sitofp(self.value, ir.DoubleType()), TypeDefinition.Float64)
            case TypeDefinition.Float32:
                match type:
                    case TypeDefinition.Float64:
                        return ValueDefinition(builder.fpext(self.value, ir.DoubleType()), TypeDefinition.Float64)
        
        raise Exception(f"Not compatible convert type from {self.type} to {type}.")