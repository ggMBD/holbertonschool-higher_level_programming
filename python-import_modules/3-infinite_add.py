#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    sumall = 0
    for i in range (1, argc):
        sumall += int(sys.argv[i])
    print("{}".format(sumall))