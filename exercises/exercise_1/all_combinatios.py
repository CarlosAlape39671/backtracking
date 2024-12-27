def all_combinations(number, numbers, sum):
    if sum == number:
        print(numbers)
        return
    if sum > number:
        return
    for i in range(1, number + 1):
        numbers.append(i)
        all_combinations(number, numbers, sum + i)
        numbers.pop()

def main():
    number = 4
    numbers = []
    sum = 0
    all_combinations(number, numbers, sum)

if __name__ == '__main__':
    main()