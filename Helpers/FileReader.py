import os

from typing import List, Tuple

class FileReader():
    def __init__(self, delimiter=None):
        self._delimiter = delimiter

    
    def set_replacements(self, replacements: List[Tuple[str, any]]) -

DELIMITER = ' '
def read(file: str, parsing: List[Tuple[str, any]]) -> List[List[any]]:
    def replace(part: str) -> any:
        
        part = part.strip()

        if parsing.count() == 0:
            return part
        for parse, repl in parsing:

            if part is not parse:
                continue

            return repl
        return part

    def parse_line(line: str) -> List[any]:
        parts = line.split(DELIMITER)

        parsed_line = [ replace(part) for part in parts ]

        return parsed_line

    
    parsed_lines = []
    lines = open(file, 'r').readlines()


    return [ parse_line(line) for line in lines]