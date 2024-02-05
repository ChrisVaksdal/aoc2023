import utils


def getDigits(line: str) -> list[int]:
    return [int(c) for c in line if c.isdigit()], [i for i, c in enumerate(line) if c.isdigit()]

def digitsToNumber(digits: list[int]) -> int:
    return int(''.join(map(str, digits)))

def findWrittenDigits(s: str) -> list[list[int], list[int]]:
    written_digits = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    output = []
    for i in range(len(s)):
        for digit, value in written_digits.items():
            if s[i:i+len(digit)] == digit:
                output.append((value, i))

    if len(output) == 0:
        return [], []
    return zip(*output)

def part1(data: list[str]) -> int:
    output = []
    for line in data:
        digits, _ = getDigits(line)
        if len(digits) == 0:
            continue
        number = digitsToNumber([digits[0], digits[-1]])
        output.append(number)
    return sum(output)

def part2(data: list[str]) -> int:
    output = []
    for line in data:
        # Get number-digits and their indices:
        digits, digitIndices = getDigits(line)

        # Get written digits and their indices:
        try:
            writtenDigits, writtenIndices = findWrittenDigits(line)
        except ValueError:
            writtenDigits, writtenIndices = [], []

        # If there are no digits, skip the line:
        if len(digits) == 0 and len(writtenDigits) == 0:
            continue

        # Find the first and last digit:
        if len(digits) > 0 and (len(writtenDigits) == 0 or min(digitIndices) < min(writtenIndices)):
            minIndex = min(digitIndices)
            firstDigit = digits[digitIndices.index(minIndex)]
        else:
            minIndex = min(writtenIndices)
            firstDigit = writtenDigits[writtenIndices.index(minIndex)]
        if len(digits) > 0 and (len(writtenDigits) == 0 or max(digitIndices) > max(writtenIndices)):
            maxIndex = max(digitIndices)
            lastDigit = digits[digitIndices.index(maxIndex)]
        else:
            maxIndex = max(writtenIndices)
            lastDigit = writtenDigits[writtenIndices.index(maxIndex)]

        # Convert the digits to a number and append it to the output:
        number = digitsToNumber([firstDigit, lastDigit])
        output.append(number)
    
    # Calculate the sum and return:
    return sum(output)

def main():
    data = utils.readInput(day=1)
    # data = utils.readTestInput()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()
