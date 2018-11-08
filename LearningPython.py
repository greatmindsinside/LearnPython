
thestring = 'HackerRank.com presents "Pythonist 2".'

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



