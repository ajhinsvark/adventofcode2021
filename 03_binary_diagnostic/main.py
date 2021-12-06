

def get_o2(nums, pos=0):
    if len(nums) == 1:
        return nums[0]

    ones = 0
    for x in nums:
        if x[pos] == '1':
            ones += 1

    if ones >= len(nums) / 2:
        nums = [x for x in nums if x[pos] == '1']
    else:
        nums = [x for x in nums if x[pos] == '0']

    return get_o2(nums, pos + 1)


def get_co2(nums, pos=0):
    if len(nums) == 1:
        return nums[0]

    ones = 0
    for x in nums:
        if x[pos] == '1':
            ones += 1

    if ones < len(nums) / 2:
        nums = [x for x in nums if x[pos] == '1']
    else:
        nums = [x for x in nums if x[pos] == '0']

    return get_co2(nums, pos + 1)


def main():
    count = 0
    bits = {}
    with open('input.txt') as f:
        for line in f:
            count += 1
            for i, b in enumerate(line.strip()):
                if i not in bits:
                    bits[i] = 0
                bits[i] += 1 if b == "1" else 0

    gamma = []
    epsilon = []
    for i in range(len(bits)):
        if bits[i] > count // 2:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")
    
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    print(f"gamma {gamma} eps {epsilon}, result = {gamma * epsilon}")

    with open('input.txt') as f:
        nums = [x.strip() for x in f.readlines()]
        o2 = int(get_o2(nums), 2)
        co2 = int(get_co2(nums), 2)

        print(o2, co2, o2 * co2)
        





if __name__ == "__main__":
    main()
