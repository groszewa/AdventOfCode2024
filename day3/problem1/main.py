import re

def mul(a,b):
    return a*b

def main():
    file = open("input.txt", "r")
    input = file.read()
    acc = 0
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, input)
    for match in matches:
        acc += eval(match)
    print(f"Total is {acc}")

if __name__ == '__main__':
    main()
