
def level_check(l):
    diff_list = []
    for x,y in zip(l[0::],l[1::]):
        diff_list.append(y-x)
    if all((x>0 and x<4) for x in diff_list):
        return True
    if all((x<0 and x>-4) for x in diff_list):
        return True
    return False

def main():
    with open('input.txt','r') as file:
        num_safe = 0
        for line in file:
            level = [int(x) for x in line.split()]
            if(level_check(level)):
                num_safe+=1
        print(f"Number of safe levels = {num_safe}")

if __name__ == '__main__':
    main()
