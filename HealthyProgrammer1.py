from pygame import mixer
from time import time
from datetime import datetime


def music(file,stopper):
  mixer.init()
  mixer.music.load(file)
  mixer.music.play()
  while True:
    a=input('')
    if a==stopper:
      mixer.music.stop()
      break
def log(msg):
    f=open('log.txt','a')

    f.write(f"{msg} {datetime.now()}  \n")
    f.close()


if __name__ == '__main__':
    print('Welcome to Healthy Programmer Application')
    l=input('Enter the time you want the program to start in H:M:S format')
    while True:
        r=datetime.now()
        s=r.strftime("%H:%M:%S")
        if s== l:
            print('Starting from',l)
            waterlevel=10
            init_water=time()
            init_eye=time()
            init_physical=time()
            watersecs=5
            eyesecs=1800
            physicalsecs=2700
            while True:
                if time()-init_water>watersecs:
                    print('Time to drink water.Please enter Drank to stop the music')
                    music("water (1).mp3","Drank")
                    init_water=time()
                    log('Drank water at: ')
                    waterlevel-=6
                    if waterlevel==0:
                        print('Done for the Day')
                        break

                if time()-init_water>eyesecs:
                    print('Time for Eye Exercise.Please enter Doneyes to stop the music ')

                    music("eye.mp3","Doneyes")
                    init_eye=time()
                    log('Eye exercise performed at: ')

                if time()-init_water>physicalsecs:
                    print('Time to do physical exercise.Please enter Donephysical to stop the music ')

                    music("physical.mp3","Donephysical ")
                    init_physical=time()
                    log('Physical excercise performed at: ')
