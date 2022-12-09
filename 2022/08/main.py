
import os
import re
import copy


def main():
    file = '/config/workspace/AoC/2022/08/input.txt'
    lines = lines = open(file, 'r').readlines()

    grid = []
    for line in lines:
        row = []
        for c in line.strip():
            row.append(int(c))

        grid.append(row)

    rows = len(grid)
    columns = len(grid[0])


    def is_visible(row, column):
        nonlocal grid
        nonlocal rows
        nonlocal columns

        height = grid[row][column]

        if row == 0 or row == rows-1:
            return True

        if column == 0 or column == columns -1:
            return True


        is_visible = 4
        # # left side visible
        for i in range(column):
            tree = grid[row][i]

            if tree >= height:
                is_visible -= 1
                break

        for i in range(column+1, columns):
            tree = grid[row][i]

            if tree >= height:
                is_visible -= 1
                break

        # Top
        for i in range(row):
            tree = grid[i][column]

            if tree >= height:
                is_visible -= 1
                break

        # Bottom
        for i in range(row+1, rows):
            tree = grid[i][column]

            if tree >= height:
                is_visible  -= 1
                break
        return is_visible > 0


    
    def calc_viewing(row, column):
        nonlocal grid
        nonlocal rows
        nonlocal columns
        
        height = grid[row][column]
        def distance_north():
            distance_north = 0

            for i in reversed(range(row)):
                tree = grid[i][column]

                distance_north += 1

                if tree >= height:
                    return distance_north

            return distance_north

        def distance_south():
            distance_south = 0
            for i in range(row+1, rows):
                tree = grid[i][column]

                distance_south += 1

                if tree >= height:
                    return distance_south

            return distance_south

        def distance_east():
            distance_east = 0

            for i in reversed(range(column)):
                tree = grid[row][i]

                distance_east += 1

                if tree >= height:
                    return distance_east

            return distance_east


        def distance_west():
            west = 0

            for i in range(column+1, columns):
                tree = grid[row][i]

                west += 1

                if tree >= height:
                    return west

            return west

        
        
        
        distance = 1
        distance *= distance_north()
        distance *= distance_south()
        distance *= distance_east()
        distance *= distance_west()

        return distance




    def part1():
        visible = 0
        for i in range(rows):
            for j in range(columns):
                if is_visible(i,j):
                    visible += 1

        return visible


    def part2():
        max_distance = 0
        for i in range(rows):
            for j in range(columns):
                distance = calc_viewing(i, j)

                if distance > max_distance:
                    max_distance = distance

        return max_distance

    print (f"Part 1: {part1()}")
    print (f"Part 2: {part2()}")

if __name__ == '__main__':
    main()