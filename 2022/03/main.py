import os
from enum import IntEnum, Enum
from typing import Tuple, List


class Rucksack():
    def __init__(self, content: str):
        self._content = content.strip()

        length = int(len(self._content) / 2)
        a = self._content[:length]
        b = self._content[length:length*2]

        a_mapped = self.map(a)
        b_mapped = self.map(b)

        
        duplicates = []

        total_sum = 0
        for (letter, value) in a_mapped:
            if (letter,value) in b_mapped and not (letter,value) in duplicates:
                duplicates.append((letter, value))
                total_sum += value

        self._sum = total_sum
        self._a = a_mapped
        self._b = b_mapped



    def map(self, content: str) -> List[Tuple[str, int]]:
        sorted_str = sorted(content)

        sorted_list: List[Tuple[str, int]] = []

        for c in sorted_str:
            
            i_val = 0
            if c.islower():
                i_val = ord(c) - ord('a') + 1
            else:
                i_val = (ord(c) - ord('A') + 27)

            value = i_val
            sorted_list.append((c, value))
        return sorted_list

    def contained_in(self, a, b) -> int:
        mapped = self.map(self._content)
        mapped_a = self.map(a._content)
        mapped_b = self.map(b._content)

        

        total_sum = 0
        duplicates = []
        for (letter, value) in mapped:
            if (letter, value) in duplicates:
                continue

            if (letter,value) not in mapped_a:
                continue

            if (letter, value) not in mapped_b:
                continue

            duplicates.append((letter, value))

            total_sum += value

        
        return total_sum





    
def main():

    file = '/config/workspace/AoC/2022/03/input.txt'
    lines = lines = open(file, 'r').readlines()


    rucksacks =  [ Rucksack(line) for line in lines]
    
    def part1():
        total_sum = 0
        for rucksack in rucksacks:
                total_sum += rucksack._sum

        print (total_sum)

    
    def part2():
        total_sum = 0
        for i in range(0, len(rucksacks),3):
            r1 = rucksacks[i]
            r2 = rucksacks[i+1]
            r3 = rucksacks[i+2]

            total_sum += r1.contained_in(r2, r3)

        
        print (total_sum)


    part2()
    



    

if __name__ == '__main__':
    main()