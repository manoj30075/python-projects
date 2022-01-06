"""
CSCI-603 PreTee Lab
Author: RIT CS
Author: Manoj Kumar Reddy Palasamudram, Ashwath Halemane

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import sys              # argv
import literal_node     # literal_node.LiteralNode
import variable_node    # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node       # print_node.PrintNode
import math_node        # math_node.MathNode
import syntax_error     # syntax_error.SyntaxError
import runtime_error    # runtime_error.RuntimeError

class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile = srcFile
        self.symTbl = {}
        self.parseTrees = []
        self.lineNum = 1
        self.syntaxError = False

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """
        if not len(tokens):
            return None
        value = tokens.pop(0)
        if value.isdigit():
            return literal_node.LiteralNode(int(value))
        elif value.isidentifier():
            return variable_node.VariableNode(value, self.symTbl)
        else:
            return math_node.MathNode(self.__parse(tokens), self.__parse(tokens), value)

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """
        file_values = []
        # Open the source file and read the lines
        with open(self.srcFile) as f:
            for line in f:
                file_values.append(line.strip())

        for each_line in file_values:
            try:
                if not len(each_line):
                    pass
                elif each_line[0] == self.COMMENT_TOKEN:
                    pass
                elif each_line[0] == self.ASSIGNMENT_TOKEN:
                    split_line = each_line.split(" ")
                    if len(split_line) < 2:
                        raise syntax_error.SyntaxError(" Incomplete statement")
                    elif not split_line[1].isidentifier():
                        raise syntax_error.SyntaxError(" Bad assignment to non-variable")
                    else:
                        # add the assignment to the parse tree
                        assignment_node_temp = assignment_node.AssignmentNode(
                            variable_node.VariableNode(split_line[1], self.symTbl),
                            self.__parse(split_line[2:]),
                            self.symTbl,
                            split_line[0]
                        )
                        self.parseTrees.append(assignment_node_temp)
                elif each_line[0] == self.PRINT_TOKEN:
                    # add the print to the parse tree
                    split_line = each_line.split(" ")
                    print_node_temp = print_node.PrintNode(self.__parse(split_line[1:]))
                    self.parseTrees.append(print_node_temp)
                else:
                    raise syntax_error.SyntaxError(" Invalid token " + each_line[0])
            except syntax_error.SyntaxError as e:
                self.syntaxError = True
                # print the error message and the line number
                print("Syntax error: Line: " + str(self.lineNum) + str(e))
            self.lineNum += 1

    def emit(self):
        """
        Prints an infix string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        # print the parse tree
        for node in self.parseTrees:
            print(node.emit())

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """
        # evaluate the parse tree
        if not self.syntaxError:
            for node in self.parseTrees:
                node.evaluate()


def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)


if __name__ == '__main__':
    main()