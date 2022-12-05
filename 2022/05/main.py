
import os
import re
import copy

class Move():
    def __init__(self, move: str):
        self._move = move

        parts = move.split(' ')
        self._count = int(parts[1])
        self._from = int(parts[3])
        self._to = int(parts[5])

        # print (self._count, self._from, self._to)


REGEX = "(\[[A-Z]\])*"
    
def main():

    file = '/config/workspace/AoC/2022/05/input.txt'
    lines = lines = open(file, 'r').readlines()

    
    moves = []
    crates = []
    moving = False
    for line in lines:
        if line == '\n':
            moving = True
            continue

        if not moving:
            line = line.replace('\n', '')
            
            index = 1

            
            for i in range(0,len(line), 4):
                crate = line[i:(i+4)]
                if crate.startswith('['):
                    crate = crate.replace('[', '')
                    crate = crate.replace(']', '')

                    while len(crates) <= index:
                        crates.append([])

                    crates[index].append(crate.strip())
                index += 1
        else:
            moves.append(Move(line))

    
    # print (crates)
    
    # def part1():
    #     crates_copy = crates.deepcopy()
    #     for move in moves:
    #         _from = move._from
    #         _to = move._to
    #         for count in range(move._count):

    #             top = crates_copy[_from][0]
    #             crates_copy[_from].pop(0)

    #             crates_copy[_to].insert(0, top)

    #     msg = ""
    #     for stack in crates_copy:
    #         if len(stack) > 0:
    #             top_crate = stack[0]

    #             msg = msg + top_crate

    #     return msg

    def part2():
        for move in moves:
            _from = move._from
            _to = move._to
            count = move._count

            tops = crates[_from][0:count]

            crates[_from] = crates[_from][count:]

            crates[_to][:0] =  tops

        msg = ""
        for stack in crates:
            if len(stack) > 0:
                top_crate = stack[0]

                msg = msg + top_crate

        return msg
    # print ("part1:" ,part1())
    print("part2", part2())
    



    

if __name__ == '__main__':
    main()