from src.parser.logparser import LogParser, LogLexer
from pathlib import Path
import json


class LogsExtractor:
    '''
    extract info from log dir
    '''

    def __init__(self, LogDir: Path):
        self._lexer = LogLexer()
        self._lexer.build()
        self._parser = LogParser()
        self._parser.build(lexer=self._lexer.lexer)

        self.logsAst = []
        for LogFile in LogDir.rglob('*.txt'):
            if LogFile.name == 'download.txt':  # download time shouldn't be considered in cost
                continue
            print(LogFile)
            ast = self._parser.gen_ast(LogFile.read_text())
            del ast['detail']  # for debug
            self.logsAst.append(ast)

    def toJson(self):
        return json.dumps(self.logsAst, indent=2, sort_keys=False)
