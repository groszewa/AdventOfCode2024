def do_check(arr):
    if all((x>0 and x<4) for x in arr):
        return True
    if all((x<0 and x>-4) for x in arr):
        return True
    return False

def get_diff_list(l):
    diff_list = []
    for x,y in zip(l[0::],l[1::]):
        diff_list.append(y-x)
    return diff_list

def level_check(l):
    diff_list = get_diff_list(l)
    if do_check(diff_list):
        return True
    else:
        for i in range(len(l)):
            mod = l.copy()
            mod.pop(i)
            mod_diff = get_diff_list(mod)
            if do_check(mod_diff):
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
