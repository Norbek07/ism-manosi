from bs4 import BeautifulSoup
import requests 
from latincrill import transliterate


def ism_manosi_funksiyasi(ism):
    url = f"https://ismlar.com/uz/name/{ism}"
    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    natija = soup.find("div",attrs={"class":"space-y-4"})
    try:
        natija = transliterate(natija.p.text.strip())
    except:
        natija = False
    return natija
