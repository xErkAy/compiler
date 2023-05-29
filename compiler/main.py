from src.constants import BASE_DIR
from src.lexer import Lexer
from src.parser import Parser, ParserState
from src.tree.json_parsed_tree import Node, write
from src.code_generator import CodeGenerator

from copy import copy
from pprint import pprint


class Compiler:
    def __init__(self) -> None:
        input_file = open(f'{BASE_DIR}/code/input.txt').read()
        lexer = Lexer().build()

        try:
            self.tokens = lexer.lex(input_file)
            # pprint(list(copy(self.tokens)))
        except Exception as e:
            print(f'\n\nCompile log:\nError occurred at line: {e.source_pos.__dict__["lineno"]}')
            exit(0)

        self.code_generator = CodeGenerator()
        self.module = self.code_generator.module
        self.builder = self.code_generator.builder
        self.printf = self.code_generator.printf

        self.symbol_table = ParserState()
        self.semantic_root = Node("main")

    def result(self) -> None:
        """ This function returns the result """
        print("\n\nCompile log:")
        try:
            Parser(self.module, self.builder, self.printf).build().parse(
                copy(self.tokens), state=self.symbol_table
            ).eval(self.semantic_root)
        except Exception as e:
            print(f'Error occurred: {e}')
            exit(0)

        write(self.semantic_root, "JSONTree")

        self.code_generator.create_ir()
        self.code_generator.save_ir(f"{BASE_DIR}/code/output.ll")

        print('Compile completed without errors')

        print("\n\nSymbol table:\nName\t|\tType\t|\tFunction")
        for m in self.symbol_table.variables.keys():
            for v in self.symbol_table.variables[m].keys():
                if v != 'args':
                    print('%s\t|\t%s\t|\t%s' % (v, self.symbol_table.variables[m][v]['type'], m._name))
        for v in self.symbol_table.functions.keys():
            print('%s\t|\t%s\t|\t-' % (v, self.symbol_table.functions[v].typ))
        print('\n\n')


if __name__ == '__main__':
    compiler = Compiler()
    compiler.result()
