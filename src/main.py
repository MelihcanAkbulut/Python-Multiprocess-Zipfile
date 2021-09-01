# coding=utf-8
import os
import zipfile
from os.path import basename
from progress.bar import Bar
import multiprocessing
import listener


def isdir(path, sec="n"):
    try:
        name = path.split("\\")
        zipf = zipfile.ZipFile('C:\Users\melih\OneDrive\Desktop\output\{}.zip'.format(name[-1]), 'w',
                               zipfile.ZIP_DEFLATED)
        if (sec == "y"):
            sayi = say(path, "y")
            bar = Bar('Processing', max=sayi, suffix='%(percent).1f%% - %(eta)ds')
            for root, dirs, files in os.walk(path):
                sayac = 0
                for file in files:
                    sayac += 1
                    zipf.write(os.path.join(root, file),
                               os.path.relpath(os.path.join(root, file),
                                               os.path.join(path, '..')))
                    bar.next()

        elif (sec == "n"):
            sayi = say(path, "n")
            bar = Bar('Processing', max=sayi, suffix='%(percent).1f%% - %(eta)ds')
            for root, dirs, files in os.walk(path):
                sayac = 0
                for file in files:
                    sayac += 1
                    filePath = os.path.join(root, file)
                    zipf.write(filePath, basename(filePath))
                    bar.next()
                break
        zipf.close()
    except:
        print("Zip dosyasına yazılırken hata oluştu")


def isfile(path):
    bar = Bar('Processing', max=1, suffix='%(percent).1f%% - %(eta)ds')
    name = path.split("\\")
    zipf = zipfile.ZipFile('C:\Users\melih\OneDrive\Desktop\output\{}.zip'.format(name[-1]), 'w', zipfile.ZIP_DEFLATED)
    zipf.write(path)
    bar.next()
    zipf.close()


def say(path, dr="n"):
    sayac2 = 0
    if (dr == "y"):
        for root, dirs, files in os.walk(path):
            for file in files:
                sayac2 += 1
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                sayac2 += 1
            break
    return sayac2


def forZip():
    with open('main.txt') as f:
        temp2 = f.read().splitlines()
        sayac2 = 0
        for i in range(len(temp2)):
            a = temp2[i].split('"')
            if (len(a) != 1):
                path = a[1]
                sayac2 += 1
                if os.path.isdir(path):
                    if (len(a) == 3):
                        p = multiprocessing.Process(target=isdir, args=(path,))
                        p.start()
                    elif (a[3] == 'y'):
                        p = multiprocessing.Process(target=isdir, args=(path, "y"))
                        p.start()
                    elif (a[3] == 'n' or a[3] == ''):
                        p = multiprocessing.Process(target=isdir, args=(path,))
                        p.start()
                elif os.path.isfile(path):
                    p = multiprocessing.Process(target=isfile, args=(path,))
                    p.start()
                else:
                    print("Geçerli dosya/dizin bulunamadı")


def main():
    listener.main()
    forZip()


if __name__ == "__main__":
    main()
