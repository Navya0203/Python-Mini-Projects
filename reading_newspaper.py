#Akhbaar padhke sunaao
# 21972f2d79fc47d596a40c116bdd42c4 api key
import requests
import json






def speak(str):
    from win32com.client import Dispatch

    speak =Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':

    inp1=input('Enter the country you want the news from:')
    inp2=input('Enter the date you want the news from.In the folowing format 2022-01-15:')


    url=f"https://newsapi.org/v2/everything?q={inp1}&from={inp2}&sortBy=popularity&apiKey=21972f2d79fc47d596a40c116bdd42c4"
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
