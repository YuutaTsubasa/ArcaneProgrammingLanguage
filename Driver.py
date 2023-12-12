import sys
import traceback
from antlr4 import *
from ArcaneLexer import ArcaneLexer
from ArcaneParser import ArcaneParser
from ArcaneToLLVMIRVisitor import ArcaneToLLVMIRVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ArcaneLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArcaneParser(stream)
    tree = parser.prog()

    try:
        visitor = ArcaneToLLVMIRVisitor()
        visitor.visit(tree)
    except Exception as exception:
        traceback.print_exception(exception)
        exit(0)

    with open("output.ll", "w") as f:
        f.write(str(visitor.module))


if __name__ == '__main__':
    main(sys.argv)