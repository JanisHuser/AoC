import math
# from s import 

import os


class Operation():


    def __init__(self, action):
        self._action = action.strip()
        
        action = self._action.replace('new = old ','').split(' ')

        self._operand = action[0]

        if action[1] != 'old':
            self._next = (int(action[1]))
        else:
            self._next = False

    def execute(self, old):
        what = self._next
        if not what:
            what = old
        if (self._operand == '*'):            
            return old * what
        elif self._operand == '+':
            return old + what



class Test():
    
    def __init__(self, line):
        test = line.strip().replace('Test: ','')
        self._action = test.split(' ')[0]
        self._numeric = (int(test.split(' ')[2]))


    def execute(self, number):
        if self._action == 'divisible':
            return (number % self._numeric) == 0


        return False



class Monkey():

    WORRY_LEVEL_DIVISION = 3
    def parse_id(self, line):
        self._id = int(line.replace(':', '').split(' ')[1])

    def parse_starting_items(self, line):
        line = line.strip().replace('Starting items:', '')
        self._items = [(int(x)) for x in line.split(', ')]

    def parse_test(self, line):
        self._test = Test(line)

    def parse_operation(self, line):
        operation = line.strip().replace('Operation: ', '')
        self._operation = Operation(operation)


    def parse_test_actions(self, line_true, line_false):
        monkey_true = line_true.strip().replace('If true: throw to monkey ', '')
        monkey_false = line_false.strip().replace('If false: throw to monkey ', '')
        
        self._monkey_true = int(monkey_true)
        self._monkey_false = int(monkey_false)


    def __init__(self, lines):
        self.parse_id(lines[0])
        self.parse_starting_items(lines[1])
        self.parse_operation(lines[2])
        self.parse_test(lines[3])
        self.parse_test_actions(lines[4], lines[5])
        self._inspection_count = 0


    def inspect(self):
        new_items = {}
        for item in self._items:
            self._inspection_count += 1
            new_item = self._operation.execute(item)

            

            # new_item = math.floor(new_item/Monkey.WORRY_LEVEL_DIVISION)
            throw_to = 0
            if self._test.execute(new_item):
                throw_to = self._monkey_true
            else:
                throw_to = self._monkey_false

            if throw_to not in new_items:
                new_items[throw_to] = []

            new_items[throw_to].append(new_item)

        self._items = []
        return new_items


    def add(self, items):
        self._items.extend(items)



def main():


    file = os.getcwd() + "/input.txt"
    lines = lines = open(file, 'r').readlines()

    grid = []

    start = []
    end = []

    row_index = 0
    for line in lines:
        line = line.strip()
        row = []
        for i in range(len(row)):
            c = line[i]

            if c == 'S':
                row.append(0)
                start = [row_index, i]
            elif c == 'E':
                row.append(0)
                end = [row_index, i]
            else:
                row.append(ord(c) - ord('a'))

        grid.append(row)
        row_index += 1

    part1(grid,)


if __name__ == '__main__':
    main()
