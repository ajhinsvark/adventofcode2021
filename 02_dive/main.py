

def main():
    x, y = 0, 0
    with open('input.txt') as f:
        for line in f:
            cmd, v = line.split()
            v = int(v)
            if cmd == "forward":
                x += v
            elif cmd == "down":
                y += v
            elif cmd == "up":
                y -= v
    print(f"final position: [{x}, {y}] dist = {x * y}")

    # Part 2
    x, y, aim = 0, 0, 0
    with open('input.txt') as f:
        for line in f:
            cmd, v = line.split()
            v = int(v)
            if cmd == "forward":
                x += v
                y += aim * v
            elif cmd == "down":
                aim += v
            elif cmd == "up":
                aim -= v
    print(f"final position with aim: [{x}, {y}] dist = {x * y}")





if __name__ == "__main__":
    main()
