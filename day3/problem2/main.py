import re

def mul(a,b):
    return a*b

def main():
    file = open("input.txt", "r")
    input = file.read()
    acc = 0
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, input)
    enabled = True
    for match in matches:
        if not match.startswith('do'):
            if enabled:
                acc += eval(match)
        else:
            if match=="do()":
                enabled = True
            else:
                enabled = False
    print(f'Total is {acc}')


if __name__ == '__main__':
    main()
