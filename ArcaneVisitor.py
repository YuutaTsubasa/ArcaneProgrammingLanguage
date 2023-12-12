# Generated from Arcane.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArcaneParser import ArcaneParser
else:
    from ArcaneParser import ArcaneParser

# This class defines a complete generic visitor for a parse tree produced by ArcaneParser.

class ArcaneVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArcaneParser#prog.
    def visitProg(self, ctx:ArcaneParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArcaneParser#stat.
    def visitStat(self, ctx:ArcaneParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArcaneParser#expr.
    def visitExpr(self, ctx:ArcaneParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArcaneParser#varDeclaration.
    def visitVarDeclaration(self, ctx:ArcaneParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArcaneParser#assignment.
    def visitAssignment(self, ctx:ArcaneParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArcaneParser#atom.
    def visitAtom(self, ctx:ArcaneParser.AtomContext):
        return self.visitChildren(ctx)



del ArcaneParser