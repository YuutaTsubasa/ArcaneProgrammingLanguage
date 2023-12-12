# Generated from Arcane.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArcaneParser import ArcaneParser
else:
    from ArcaneParser import ArcaneParser

# This class defines a complete listener for a parse tree produced by ArcaneParser.
class ArcaneListener(ParseTreeListener):

    # Enter a parse tree produced by ArcaneParser#prog.
    def enterProg(self, ctx:ArcaneParser.ProgContext):
        pass

    # Exit a parse tree produced by ArcaneParser#prog.
    def exitProg(self, ctx:ArcaneParser.ProgContext):
        pass


    # Enter a parse tree produced by ArcaneParser#stat.
    def enterStat(self, ctx:ArcaneParser.StatContext):
        pass

    # Exit a parse tree produced by ArcaneParser#stat.
    def exitStat(self, ctx:ArcaneParser.StatContext):
        pass


    # Enter a parse tree produced by ArcaneParser#expr.
    def enterExpr(self, ctx:ArcaneParser.ExprContext):
        pass

    # Exit a parse tree produced by ArcaneParser#expr.
    def exitExpr(self, ctx:ArcaneParser.ExprContext):
        pass


    # Enter a parse tree produced by ArcaneParser#varDeclaration.
    def enterVarDeclaration(self, ctx:ArcaneParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by ArcaneParser#varDeclaration.
    def exitVarDeclaration(self, ctx:ArcaneParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by ArcaneParser#assignment.
    def enterAssignment(self, ctx:ArcaneParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ArcaneParser#assignment.
    def exitAssignment(self, ctx:ArcaneParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ArcaneParser#atom.
    def enterAtom(self, ctx:ArcaneParser.AtomContext):
        pass

    # Exit a parse tree produced by ArcaneParser#atom.
    def exitAtom(self, ctx:ArcaneParser.AtomContext):
        pass



del ArcaneParser