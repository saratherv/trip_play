from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import bs4
import requests
from gtts import gTTS
import os  

# Create your views here.



@csrf_exempt
def getName(request):
    if request.method == "POST":
        place_name = request.POST["name"]
        print(place_name,"11111111111111111111111")
        from googlesearch import search 
        url = "https://en.wikipedia.org/wiki/Taj_Mahal"
        for j in search(place_name, tld="co.in", num=10, stop=1, pause=2): 
            print(j)
            url = j 
        
        response = requests.get(url)
        print(response,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        if response is not None:
            print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
            html = bs4.BeautifulSoup(response.text, 'html.parser')
            title = html.select("#firstHeading")[0].text
            paragraphs = html.select("p")
            mytext = ""
            for para in paragraphs:
                mytext = mytext + "   "  + str(para.text)
            # mytext = "Place Name check"
            print(mytext)
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("media/" + str(place_name) + ".mp3")
            os.system("mpg321 welcome.mp3")  

        print(place_name, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return render(request, "audio1.html", {"place_name" : place_name, "description" : mytext})
    else:
        return render(request, "main.html")



@csrf_exempt
def login(request):
    if request.method == "POST":
        print("post here")
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        # if user_name == "admin" and password == "admin1234":
        return render(request, "home.html")
    else:
        return render(request, "login.html")