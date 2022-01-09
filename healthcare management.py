#healthcare management system
def getdate():
    from datetime import datetime as dt
    now=dt.now()
    string=dt.isoformat(now)
    return string
def log(s):
        f=open(s,'a')
        det=input('Enter the details:')
        t=getdate()
        f.write(t+ " " +det+"\n")
        q=input('Do you want to continue writing y/n:')
        if q=='y':
            log()
        else:
            f.close()
def ret(s):
    f2=open(s,'rt')
    print(f2.read())
    f2.close()



def inp():

    Name=int(input("Please enter 1 for Harry's Information 2 for Hamad and 3 for Rohan :"))
    Act=int(input('Please enter 1 for exercise and 0 for diet:'))
    Purp=int(input('please enter 1 for log and 0 for retrieve:'))

    if Name==1:
        if Act==1:
            s="harryex.txt"

        else:
            s="harrydiet.txt"
    elif Name==2:
        if Act==1:
            s="hamadex.txt"
        else:
            s="hamaddiet.txt"
    elif Name==3:
        if Act==1:
            s="rohanex.txt"
        else:
            s="rohandiet.txt"
    print( "The file that will be available",s)
    if Purp==1:
        log(s)
    else:
        ret(s)
print('Welcome to my healthcare management system')
inp()
Q=input('Enter Y if you want to continue with next file else N:')
if Q=='Y':
    inp()
else:
    print(done)
