from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import requests

search = input("Enter what to look for :- ")
params = {"q": search}
r = requests.get("https://www.bing.com/images/search", params=params)
print(r.url)
print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")
link = soup.findAll("a", {"class": "thumb"})

for item in link:
    img_obj = requests.get(item.attrs["href"])
    print("Getting item from ", item.attrs["href"])
    print(img_obj)
    title = item.attrs["href"].split("/")[-1]
    try:
        img = Image.open(BytesIO(img_obj.content))
        img.save("./scraped_images/" + title, img.format)
    except:
        print("could not save file")
