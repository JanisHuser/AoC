from typing import List, Tuple
def main():
    file1 = open('/config/workspace/AoC/2022/01/calories.txt', 'r')
    Lines = file1.readlines()
    
    snacks = []

    current_elf_calories = 0
    elf_pos = 1
    
    count = 0
    # Strips the newline character
    for line in Lines:
        if line == '\n':
            t = (count, current_elf_calories)
            snacks.append(t)
            count += 1
            current_elf_calories = 0
        else:
            digit = ''.join(c for c in line if c.isdigit())
            current_elf_calories += int(digit)

    snacks.append((elf_pos, current_elf_calories))

    sorted_list = sorted(
        snacks,
        key=lambda t: t[1],
        reverse =True
    )
    sum = 0
    for i in range(0, 3):
        sum += sorted_list[i][1]
        
        print (sorted_list[i])

    print (sum)






if __name__ == '__main__':
    main()