# Generated from Arcane.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,69,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,30,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,
        9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        57,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,67,8,5,1,5,0,1,4,6,0,
        2,4,6,8,10,0,2,1,0,2,4,1,0,5,6,73,0,15,1,0,0,0,2,20,1,0,0,0,4,29,
        1,0,0,0,6,42,1,0,0,0,8,56,1,0,0,0,10,66,1,0,0,0,12,14,3,2,1,0,13,
        12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,
        0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,21,3,4,2,0,21,22,5,
        1,0,0,22,3,1,0,0,0,23,24,6,2,-1,0,24,30,3,6,3,0,25,30,3,8,4,0,26,
        27,5,7,0,0,27,30,3,4,2,2,28,30,3,10,5,0,29,23,1,0,0,0,29,25,1,0,
        0,0,29,26,1,0,0,0,29,28,1,0,0,0,30,39,1,0,0,0,31,32,10,6,0,0,32,
        33,7,0,0,0,33,38,3,4,2,7,34,35,10,5,0,0,35,36,7,1,0,0,36,38,3,4,
        2,6,37,31,1,0,0,0,37,34,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,5,1,0,0,0,41,39,1,0,0,0,42,43,5,13,0,0,43,44,5,15,0,0,
        44,45,5,8,0,0,45,46,5,12,0,0,46,47,5,9,0,0,47,48,3,4,2,0,48,7,1,
        0,0,0,49,50,5,15,0,0,50,51,5,9,0,0,51,57,3,4,2,0,52,53,3,6,3,0,53,
        54,5,9,0,0,54,55,3,4,2,0,55,57,1,0,0,0,56,49,1,0,0,0,56,52,1,0,0,
        0,57,9,1,0,0,0,58,67,5,16,0,0,59,67,5,17,0,0,60,67,5,14,0,0,61,67,
        5,15,0,0,62,63,5,10,0,0,63,64,3,4,2,0,64,65,5,11,0,0,65,67,1,0,0,
        0,66,58,1,0,0,0,66,59,1,0,0,0,66,60,1,0,0,0,66,61,1,0,0,0,66,62,
        1,0,0,0,67,11,1,0,0,0,6,15,29,37,39,56,66
    ]

class ArcaneParser ( Parser ):

    grammarFileName = "Arcane.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'return'", "':'", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TYPE", "VAR", "BOOL", "ID", "INT", "FLOAT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_varDeclaration = 3
    RULE_assignment = 4
    RULE_atom = 5

    ruleNames =  [ "prog", "stat", "expr", "varDeclaration", "assignment", 
                   "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    TYPE=12
    VAR=13
    BOOL=14
    ID=15
    INT=16
    FLOAT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ArcaneParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArcaneParser.StatContext)
            else:
                return self.getTypedRuleContext(ArcaneParser.StatContext,i)


        def getRuleIndex(self):
            return ArcaneParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ArcaneParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 255104) != 0):
                self.state = 12
                self.stat()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(ArcaneParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ArcaneParser.ExprContext,0)


        def getRuleIndex(self):
            return ArcaneParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = ArcaneParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.expr(0)
            self.state = 21
            self.match(ArcaneParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(ArcaneParser.VarDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ArcaneParser.AssignmentContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArcaneParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArcaneParser.ExprContext,i)


        def atom(self):
            return self.getTypedRuleContext(ArcaneParser.AtomContext,0)


        def getRuleIndex(self):
            return ArcaneParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArcaneParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 24
                self.varDeclaration()
                pass

            elif la_ == 2:
                self.state = 25
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 26
                self.match(ArcaneParser.T__6)
                self.state = 27
                self.expr(2)
                pass

            elif la_ == 4:
                self.state = 28
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ArcaneParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ArcaneParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expr(6)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ArcaneParser.VAR, 0)

        def ID(self):
            return self.getToken(ArcaneParser.ID, 0)

        def TYPE(self):
            return self.getToken(ArcaneParser.TYPE, 0)

        def expr(self):
            return self.getTypedRuleContext(ArcaneParser.ExprContext,0)


        def getRuleIndex(self):
            return ArcaneParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = ArcaneParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ArcaneParser.VAR)
            self.state = 43
            self.match(ArcaneParser.ID)
            self.state = 44
            self.match(ArcaneParser.T__7)
            self.state = 45
            self.match(ArcaneParser.TYPE)
            self.state = 46
            self.match(ArcaneParser.T__8)
            self.state = 47
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArcaneParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ArcaneParser.ExprContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(ArcaneParser.VarDeclarationContext,0)


        def getRuleIndex(self):
            return ArcaneParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ArcaneParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(ArcaneParser.ID)
                self.state = 50
                self.match(ArcaneParser.T__8)
                self.state = 51
                self.expr(0)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.varDeclaration()
                self.state = 53
                self.match(ArcaneParser.T__8)
                self.state = 54
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ArcaneParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ArcaneParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(ArcaneParser.BOOL, 0)

        def ID(self):
            return self.getToken(ArcaneParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ArcaneParser.ExprContext,0)


        def getRuleIndex(self):
            return ArcaneParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ArcaneParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ArcaneParser.INT)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(ArcaneParser.FLOAT)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(ArcaneParser.BOOL)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.match(ArcaneParser.ID)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.match(ArcaneParser.T__9)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(ArcaneParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




