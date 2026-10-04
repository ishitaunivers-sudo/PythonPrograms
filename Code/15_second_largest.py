def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two different numbers")

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


if __name__ == "__main__":
    print(second_largest([10, 20, 30, 40]))