


def swap_case(s):
    thestring = ""
    for x in s:
        if str(x).isupper():
            thestring += str(x).lower()
        elif str(x).islower():
            thestring += str(x).upper()
    print(thestring)
    return thestring


def swap_case1(s):
    thenewstring = ""
    thelist = str(s).split()
    print(thelist)


    thenewstring = " ".join(thelist)
    print(thenewstring)


def split_and_join(line):
    # write your code here
    a = line.split()
    print("-".join(line))
    return "-".join(line)


def print_full_name(a, b):
    thenewstring = "Hello {} {}! You just delved into python.".format(a, b)
    print(thenewstring)
    print("Hello Ross Taylor! You just delved into python.")
    return thestring


def mutate_string(string, position, character):
    thelist = list(string)
    thelist[position] = character
    string = "".join(thelist)
    print(string)
    return string


def count_substring(string, sub_string):
    num = 0
    occur = 0
    while num != -1:
        num = string.find(sub_string, num)
        #print("top: " + str(num))
        if num != -1:
            occur += 1
            num = string.find(sub_string, num + 1)
    return occur


def stringvalid(s):
    print(str(s).isalpha())
    print(str(s).isalnum())
    
if __name__ == '__main__':
    #N = number of commands
    TheList = []
    N = int(input())
    for n in range(N):
        x = input().split()
        command = x[0]
        if command == "append":
            TheList.append(int(x[1]))
        if command ==  "print":
            print(TheList)
        if command == "insert":
            TheList.insert(int(x[1]), int(x[2]))
        if command == "reverse":
            TheList.reverse()
        if command == "sort":
            TheList = sorted(TheList)
        if command == "pop":
            TheList.pop()
        if command == "remove":
            TheList.remove(int(x[1]))
    



