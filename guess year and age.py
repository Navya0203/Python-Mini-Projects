#age
def age_in_an_year(inp):
    q=input('Do you want to know your age in a particular year press y/n:')
    if q=='y':
        y=input('please enter the year:')
        try:
            yr=int(y)
            if len(y)==4 and len(str(inp))==4:
                if yr>=inp :
                    ol=yr-inp
                    print('You will be',ol,'years')
                else:
                    print('please enter valid input')
                    age_in_an_year()
            elif len(y)==4 and len(str(inp))<4:
                t=2021-yr
                if yr>t:
                    ol=2021-y+inp
                    print('You will be',ol,'years')
            else:
                print('please enter a valid value')
                age_in_an_year(inp)
        except:
            print('please enter a valid value')
            age_in_an_year(inp)
    elif q=='n':
        print('done')
    else:
        print('enter a valid value')
        age_in_an_year(inp)




def age(inp):
    print('You have entered your age:',inp,'years')
    s=2021-inp
    year_100=s+100
    print('You will turn 100 in ',year_100)
def year(inp):
    print('You have entered your year of birth')
    year_100=inp+100
    print('You will turn 100 in ',year_100)

if __name__ == '__main__':
    inp=input('Please enter your age or year of birth:')
    try:
        inp=int(inp)
        if inp>0:
            if len(str(inp))==4:
                if inp>1900 and inp<2021:
                    year(inp)
                    age_in_an_year(inp)
                elif inp>2021:
                    print('Seems like you are not born yet')
                elif inp<1900:
                    print('Seems like you are the oldest person alive')
            elif len(str(inp))<4:
                if inp<120:
                    age(inp)
                    age_in_an_year(inp)
                else:
                    print('You seem like you are the oldest person alive')
            else:
                print('Please enter a valid input')
        else:
            print('Please enter a valid input')


    except:
        print('please enter a valid value')
