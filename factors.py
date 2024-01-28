import sys

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for number in numbers:
        factors = factorize(number)
        if factors:
            p, q = factors
            print(f"{number}={p}*{q}")

if __name__ == "__main__":
    main()

