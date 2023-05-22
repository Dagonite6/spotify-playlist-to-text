import requests
from bs4 import BeautifulSoup

with open("songs.txt", "r", encoding='utf-8-sig') as songs:
    data = songs.read()

song_list = data.split("\n")
results = []
for line in song_list:
    page = requests.get(line)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.text
    title = title.replace("song and lyrics by ", "")
    title = title.replace(" | Spotify", "")
    print(title)
    results.append(title)


with open('results.txt', 'w') as f:
    for line in results:
        f.write(f"{line}\n")
