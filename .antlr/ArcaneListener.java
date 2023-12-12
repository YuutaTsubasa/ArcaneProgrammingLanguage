// Generated from c:/Users/yuuta/Documents/Arcane/Arcane.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ArcaneParser}.
 */
public interface ArcaneListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ArcaneParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(ArcaneParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArcaneParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(ArcaneParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArcaneParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(ArcaneParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArcaneParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(ArcaneParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArcaneParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ArcaneParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArcaneParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ArcaneParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArcaneParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclaration(ArcaneParser.VarDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArcaneParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclaration(ArcaneParser.VarDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArcaneParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ArcaneParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArcaneParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ArcaneParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArcaneParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(ArcaneParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArcaneParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(ArcaneParser.AtomContext ctx);
}