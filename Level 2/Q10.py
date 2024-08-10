

def make_pile(n):
    stones = []
    current_stones = n
    while current_stones > 0:
        if n % 2 == 0:
            stones.append(current_stones)
            current_stones -= 2
        else:
            stones.append(current_stones)
            current_stones -= 2

    stones.sort()
    return stones

n = 6
print(" Stones in a single pile : ", make_pile(n))




