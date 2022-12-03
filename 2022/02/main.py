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
    
    def part1():
        score = 0
        for opp, me in lines:

            beats = me.compare(opp)

            if beats == 0:
                score += 3
            elif beats == 1:
                score += 6
            score += me.value

        print (score)

    
    def part2():
        score = 0

        new_lines = []
        lines = read('/config/workspace/AoC/2022/02/input.txt')

        for opp, me in lines:
            me = opp
            new_lines.append('{opp} {me}')



    

if __name__ == '__main__':
    main()