#snake water gun gamelist
print('This is Snake Water Gun game')
print('Choose 1 for Snake\n2 for Water\n3 for Gun')


T=int(input('Input the number of Rounds'))
Sc=0
def comp():
    import random
    gamelist=['Snake','Water','Gun']
    comp=random.choice(gamelist)
    for i in range(len(gamelist)):
        if comp==gamelist[i]:
            c=i+1
    return c


while T>0:
    P=int(input('Choose one option:'))
    C=comp()
    if P==C:
        Pt=0
        print('Both entered same')
        print('Point is equal to:',Pt)
    elif P==1 and C==2:
        print('Computer Chose Water')
        print('You Won')
        Pt=1
        print('Point is equal to:',Pt)
    elif P==2 and C==1:
        print('Computer Chose Snake')
        print('You Lost')
        Pt=0
        print('Point is equal to:',Pt)
    elif P==1 and C==3:
        print('Computer Chose Gun')
        print('You Lost')
        Pt=0
        print('Point is equal to:',Pt)
    elif P==3 and C==1:
        print('Computer Chose Snake')
        print('You Won')
        Pt=1
        print('Point is equal to:',Pt)
    elif P==2 and C==3:
        print('Computer Chose Gun')
        print('You Won')
        Pt=1
        print('Point is equal to:',Pt)
    else:
        print('Computer Chose # WARNING: ater')
        print('You Lost')
        Pt=0
        print('Point is equal to:',Pt)
    Sc=Sc+Pt
    T=T-1
print('Your final Score is',Sc)
print('Game Over')
