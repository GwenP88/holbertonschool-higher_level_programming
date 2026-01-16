import sys

if __name__ == "__main__":
    result = 0
    if len(sys.argv) == 1:
        print("{}".format((result)))
    else:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
        print("{}".format(result))
