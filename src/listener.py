import os

def plan(path):
    with open('main.txt', 'a') as f:
        f.write('\n')
    with open('main.txt', 'a') as f:
        for root, dirs, files in os.walk(path):
            sayac = 0
            for file in files:
                f.write('"')
                f.write("{}\{}".format(path, file))
                f.write('"')
                f.write('\n')
                f.write('\n')
            break

    with open("main.txt", "r") as f:
        lines = f.readlines()
    with open("main.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != '"{}" "exp"'.format(path):
                f.write(line)

def main():
    with open('main.txt') as f:
        temp2 = f.read().splitlines()
        for i in range(len(temp2)):
            a = temp2[i].split('"')
            if (len(a) != 1):
                if a[3] == 'exp':
                    plan(a[1])

if __name__ == "__main__":
    main()



