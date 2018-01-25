import sys


def file_write():
    f = open("./source/wonderland.txt", mode="wt", encoding="utf-8")
    f.write("What are the roots that clutch")
    f.write('what branches grow\n')
    f.write('out of this stony rubbish?')
    f.close()


def file_read():
    f = open('./source/wonderland.txt', mode='rt', encoding='utf-8')
    print(f.read(32))
    print(f.read())
    print(f.read())
    f.seek(0)
    print(f.readline())
    print(f.readline())
    f.seek(0)
    print(f.readlines())
    f.close()


def file_append():
    f = open('./source/wonderland.txt', mode='at', encoding='utf-8')
    f.writelines(
        ['Son of man\n',
         'You cannot say or guess, '
         'for you know only\n',
         'A heap of broken images, ',
         'where the sun beats.\n'])
    f.close()


def main(filename):
    file_write()
    file_read()
    file_append()
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        # print(line) will have newline after each print
        sys.stdout.write(line)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
