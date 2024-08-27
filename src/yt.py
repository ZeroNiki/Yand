from bs4 import BeautifulSoup
import requests
import time


from src.config import YT_LINK


def yt_search(keyword: str):

    link = f"{YT_LINK}{keyword}"

    print("Please wait 5 second")
    time.sleep(5)
    r = requests.get(link)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

        get_div = soup.find("div", class_="pure-u-1 pure-u-md-1-4")
        get_href = get_div.find("a")['href']

        return f"https://www.youtube.com{get_href}"

    else:
        print("Error")
        return None
        return None
