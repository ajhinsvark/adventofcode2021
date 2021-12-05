

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    xs = [int(x) for x in lines]

    increases = 0
    for i in range(1, len(xs)):
        if xs[i] > xs[i - 1]:
            increases += 1

    print(f"increases: {increases}")

    increases = 0
    prev = sum(xs[:3])
    for a, b, c in zip(xs[1:], xs[2:], xs[3:]):
        if a + b + c > prev:
            increases += 1
        prev = a + b + c

    print(f"sliding window increases: {increases}")


if __name__ == "__main__":
    main()
