
import os
import re
import copy

REGEX = "(\[[A-Z]\])*"
    
def main():

    file = '/config/workspace/AoC/2022/06/input.txt'
    lines = lines = open(file, 'r').readlines()

    recent = []

    signal = lines[0]

    marker_length = 14

    for i in range(marker_length,len(signal)):
        last = signal[i-marker_length: i]

        failed = False
        for c in last:
            occ = last.count(c)

            
            if occ > 1:
                failed = True
                break

        if not failed:
            return i

    

if __name__ == '__main__':
    print(main())