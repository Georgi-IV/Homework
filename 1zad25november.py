# без рекурсия
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(sum([1, 2, 3, 4, 5]))

# с рекурсия
def recursive(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + recursive(numbers[1:])
print(recursive([1, 2, 3, 4, 5]))