
class Knot:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self._x = x
        self._y = y
        
        
    def move(self, direction):
        match direction:
            case 'L':
                self._x -= 1
            case 'R':
                self._x += 1
            case 'U':
                self._y -= 1
            case 'D':
                self._y += 1
                
    def follow(self, head):
        x_distance = head._x - self._x
        y_distance = head._y - self._y

        if abs(x_distance) <= 1 and abs(y_distance) <= 1:
            return
        
        if  x_distance > 0:
            self._x += 1
        elif x_distance < 0:
            self._x -= 1
            
        
        if  y_distance > 0:
            self._y += 1
        elif y_distance < 0:
            self._y -= 1

    def get_coords(self):
        return self._x, self._y
        
def trace_rope(lines):
    rope_length = 10
    rope = [Knot() for _ in range(rope_length)]
    head, tail = rope[0], rope[-1]

    # Use set, array can hold same item twice
    visited = {tail.get_coords()}

    for line in lines:
        direction, steps = line.split()
        
        for _ in range(int(steps)):
            head.move(direction)
            for i in range(1, len(rope)):
                rope[i].follow(rope[i - 1])
            visited.add(tail.get_coords())
    return len(visited)

def main():
    lines = open('/config/workspace/AoC/2022/09/input.txt').readlines()

    print (f"Part 1: {trace_rope(lines)}")

if __name__ == '__main__':
    main()

