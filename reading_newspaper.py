#Akhbaar padhke sunaao

import requests
import json


def speak(str):
    from win32com.client import Dispatch

    speak =Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    
    

if __name__ == '__main__':
    
    #taking input
    inp1=input('Enter the country you want the news from:')
    inp2=input('Enter the date you want the news from.In the folowing format 2022-01-15:')

    #getting data
    url=f"https://newsapi.org/v2/everything?q={inp1}&from={inp2}&sortBy=popularity&apiKey=API_Key"
    r=requests.get(url)
    s=r.text
    js=json.loads(s)
    #print(json.dumps(js,indent=4))
    listmain=js["articles"][:10]
    #print(listmain)

    speak('Todays important news')
    for i in listmain:
        str= i['description']
        speak(str)
        speak('moving on to the next news')
