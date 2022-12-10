# get all input from input.txt

import math

CRT_WIDTH = 40


class Crt:

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._frame = ['.' for i in range(self._width * self._height)]
        self._frame_pos:int = int(0)
    
    def move(self, amount= 1):
        self._frame_pos += amount

        

    def draw(self):
        l = self._frame
        n = self._width
        lines = [l[i:i + n] for i in range(0, len(l), n)]
        for line in lines:
            print (''.join(line))

    # def light(self):
    #     # n = self._width
    #     # lines = [l[i:i + n] for i in range(0, len(l), n)]
    #     # for line in lines:
    #     #     print (''.join(line))


    #     self._frame[self._frame_pos] = '#'

    def light(self):
        self._frame[self._frame_pos] = '#'


    def get_line_pos(self):
        return self._frame_pos % self._width

    def get_size(self):
        return self._width, self._height


class Cpu:

    def __init__(self, cycle_increase):
        self._tick = 0
        self._register = 1
        self._cycle_increase = cycle_increase

    def tick(self) -> None:
        self._tick += 1
        self._cycle_increase()


    def increase(self, amount: int) -> None:
        self._register += amount


    def get_register(self) -> int:
        return self._register


    def execute(self, instruction: str) -> None:

        if instruction == "noop":
            self.tick()
            return
        
        if instruction.startswith("addx"):
            _, amount = instruction.split(' ')

            amount = int(amount)
            for _ in range(2):
                self.tick()

            self.increase(amount)

        




def main():


    file = '/config/workspace/AoC/2022/10/input.txt'
    lines = lines = open(file, 'r').readlines()


    


    def part1():
        total_sum = 0
        tick_halt = [20, 60, 100, 140, 180, 220]
        def on_cycle():
            nonlocal cpu
            nonlocal total_sum
            tick = cpu._tick

            if tick in tick_halt:
                register = cpu.get_register()
                total_sum += tick * register

        
        cpu = Cpu(on_cycle)

        for line in lines:
            cpu.execute(line.strip())

        return total_sum


    def part2():
        def on_cycle():
            nonlocal cpu
            nonlocal crt
            register = cpu.get_register()
            
            
            line_pos = crt.get_line_pos()
            crt_range = range(register -1, register+2)

            if line_pos in crt_range:
                crt.light()
            crt.move()

        cpu = Cpu(on_cycle)
        crt = Crt(40, 6)

        for line in lines:
            cpu.execute(line.strip())

        crt.draw()

    print (f"Part1 : {part1()}")
    part2()
if __name__ == '__main__':
    main()
