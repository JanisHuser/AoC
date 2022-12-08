
import os
import re
import copy

REGEX = "(\[[A-Z]\])*"

class Node():
    def __init__(self, size, name):
        self._size = size
        self._name = name

class Structure():
    def __init__(self, directory):
        self._content = []
        self._name = directory
        self._parent = None


    def parseDir(self, line):
        directory = line[4:]
        self._name = directory

    def parseLs(self, line):
        size, name = line.split(' ')

        node = Node(int(size), name)
        self._content.append(node)

    def addFile(self, line):
        self.parseLs(line)

    def setDirectory(self, directory):
        nextS = Structure(directory)
        nextS._parent = self
        self._content.append(nextS)
        return nextS

    def addDirectory(self, directory):
        nextS = Structure(directory)
        nextS._parent = self
        self._content.append(nextS)

    def get_directories(self):
        dirs = []

        for f in self._content:
            if not isinstance(f, Node):
                dirs.append(f)

        return dirs



    def totalFileSize(self):
        total_size = 0
        for f in self._content:
            if isinstance(f, Node):
                total_size += f._size
            else:
                total_size += f.totalFileSize()

        return total_size

    def move_back(self):
        return self._parent


def main():
    file = '/config/workspace/AoC/2022/07/input.txt'
    lines = lines = open(file, 'r').readlines()

    current = Structure("")

    def command(line):
        nonlocal current
        command = line[2:]

        if command.startswith("cd"):
            list_files = False
            move_to = command[3:]

            if move_to == '..':
                current = current.move_back()
            else:
                current = current.setDirectory(move_to)

    def doFile(line):
        if line.startswith("dir"):
            current.addDirectory(line[4: ])
        else:
            current.addFile(line)
    
    for line in lines:
        line = line.strip()

        if line.startswith("$"):
            command(line)
        else:
            doFile(line)    

    while current._parent is not None:
        current = current.move_back()

    
    def part1():
        matches = []

        def rec(d):
            size = d.totalFileSize()
            if size <= 100000:
                matches.append(d)

            dirs = d.get_directories()
            for x in dirs:
                rec(x)
        
        rec(current)

        total_size = 0
        for m in matches:
            total_size += m.totalFileSize()

        return total_size

    def part2():     
        matches = []
        smallest =70000000
        space_needed = 0
        def rec(d):
            nonlocal smallest
            size = d.totalFileSize()

            if size >= space_needed:
                matches.append(d)
                if smallest > size:
                    smallest = size

            dirs = d.get_directories()

            for x in dirs:
                rec(x)

        space_needed = current.totalFileSize() -  (70000000 - 30000000)
        
        rec(current)

        return smallest


    print (f"Part 1: {part1()}")
    print (f"Part 2: {part2()}")

if __name__ == '__main__':
    main()