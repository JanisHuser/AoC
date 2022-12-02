import os
from enum import IntEnum, Enum
from typing import Tuple, List


class RPS(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def compare(self, other) -> bool:
        if self is other:
            return 0

        if self is RPS.ROCK and other == RPS.SCISSORS:
            return 1
        
        if self is RPS.PAPER and other == RPS.ROCK:
            return 1

        if self is RPS.SCISSORS and other is RPS.PAPER:
            return 1
        
        return -1


DELIMITER = ' '
def read(file: str, parsing: List[Tuple[str, any]]) -> List[List[any]]:
    def replace(part: str) -> any:
        part = part.strip()
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


    
def main():


    lines = read(
        '/config/workspace/AoC/2022/02/input.txt',
        [
            ('A', RPS.ROCK),
            ('B', RPS.PAPER),
            ('C', RPS.SCISSORS),
            ('X', RPS.ROCK),
            ('Y', RPS.PAPER),
            ('Z', RPS.SCISSORS)
        ])
    
    score = 0
    for opp, me in lines:

        beats = me.compare(opp)

        if beats == 0:
            score += 3
        elif beats == 1:
            score += 6
            

        score += me.value


    
    print (score)

if __name__ == '__main__':
    main()