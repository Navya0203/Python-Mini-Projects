#folder path is given
#string input legal
import os

def soldier(path,file,ext):
    j=1
    os.chdir(path)
    files=os.listdir(path)
    f=open(file)
    filelist=f.read().split()
    for i in files:
        if os.path.isfile(i):
            if os.path.splitext(i)[1]==ext:
                os.rename(i,f"{j}{ext}")
                j=j+1
            elif i not in filelist:
                os.rename(i,i.capitalize())
    print('done')
if __name__ == '__main__':

    path=input('Enter the path to the directory:')

    file=input('Enter the path of the file:')
    ext=input('enter the file extension in .ext format:')
    soldier(path,file,ext)
