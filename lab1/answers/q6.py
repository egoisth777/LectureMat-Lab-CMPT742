[](Project,%20Ray%20Marching%20SDFs.md)import random

# Todo 1: Set a seed
random.seed(1300)

# Todo 2: weighted_sum using for loop
def weighted_sum_1(weights, values):
    """Calculate weighted sum using for loop"""
    total = 0
    for i in range(len(weights)):
        total += weights[i] * values[i]
    return total

# Todo 3: weighted_sum using list comprehension
def weighted_sum_2(weights, values):
    """Calculate weighted sum using list comprehension"""
    return sum(v*w for w, v in zip(weights, values))


# Define main function
def main():
    n = 10**6  # Number of elements
    weights, values = [], []
    # Todo 4: Generate random weights and values
    for i in range(n):
        weights.append(random.uniform(0, 1))
        values.append(random.uniform(0, 1))

    print(weighted_sum_1(weights, values))

    print(weighted_sum_2(weights, values))


if __name__ == "__main__":
    main()