
import os

class Section():

    def __init__(self, section: str):
        self._section = section
        self._from = int(section.split('-')[0])
        self._to = int(section.split('-')[1])

    def fully_contains(self, other) -> bool:
        if other._from < self._from:
            return False

        if other._to > self._to:
            return False

        return True

    def overlaps(self, other) -> bool:
        if other._from > self._to:
            return False

        if self._from > other._to:
            return False
        
        return True

    
def main():

    file = '/config/workspace/AoC/2022/04/input.txt'
    lines = lines = open(file, 'r').readlines()


    sections = []

    for line in lines:
        if len(line) < 4:
            continue
        elves = line.split(',')
        
        sections.append((
            Section(elves[0]),
            Section(elves[1])
        ))

    
    def part1():
        containers = []

        for (elf1, elf2) in sections:

            if elf1.fully_contains(elf2) or elf2.fully_contains(elf1):
                containers.append((elf1, elf2))

        return len(containers)

    
    def part2():
        containers = []

        for (elf1, elf2) in sections:

            if elf1.overlaps(elf2):
                containers.append((elf1, elf2))

        return len(containers)



    print ("part1:" ,part1())
    print("part2", part2())
    



    

if __name__ == '__main__':
    main()