from collections import deque


def parse_grid(data):
    grid = [list(line) for line in data.split("\n")]

    starts = []
    start = end = None
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == "S":
                start = (i, j)
                starts.append((i, j))
                grid[i][j] = "a"
            elif v == "E":
                end = (i, j)
                grid[i][j] = chr(ord("z")+1)
            elif v == "a":
                starts.append((i, j))
    return grid, start, end, starts


# Y X
MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))
MAX_HEIGHT_CHANGE = 1

def sibling_search(grid, starts, end):

    
    seen = set()
    queue = deque([(start, 0) for start in starts])

    rows = len(grid)
    cols = len(grid[0])

    while queue:
        pos, dist = queue.popleft()
        if pos == end:
            return dist

        # already seen (prevent recursion)
        if pos in seen:
            continue

        seen.add(pos)
        y, x = pos

        origin_value = ord(grid[y][x])

        for dy, dx in MOVES:
            if 0 > x or 0 > y:
                continue

            move_y = y + dy
            move_x = x + dx

            if move_y >= rows or move_x >= cols:
                continue

            value = ord(grid[ move_y ][ move_x ])

            diff = (value - origin_value)
    
            if abs(diff) > MAX_HEIGHT_CHANGE:
                continue

            queue.append( ( (move_y, move_x), dist + 1))

    return float("inf")


with open('/config/workspace/AoC/2022/12/input.txt', "r") as file:
    data = file.read().strip()

GRID, START, END, A_LIST = parse_grid(data)


def part_one():
    return sibling_search(GRID, [START], END)


def part_two():
    return sibling_search(GRID, A_LIST, END)


print(f"Part 1: {part_one()}")  # 339
print(f"Part 2: {part_two()}")  # 332