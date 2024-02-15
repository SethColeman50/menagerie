from bs4 import BeautifulSoup
import requests

def collect_single_zoo(discord_id: int):
    contents = requests.get(f"https://gdcolon.com/zoo/{discord_id}")
    soup = BeautifulSoup(contents.text, 'html.parser')

    
    zoo_list = soup.find('div',class_='zooList')
    if zoo_list is None:
        return []
    
    h4s = zoo_list.find_all('h4')
    animals = []

    for h4 in h4s:
        h4_split = h4["title"].split(" ")
        animal_number = h4_split[0][:-1]
        animal_name = h4_split[1]
        animals.append({'number': animal_number, 'name': animal_name})

    return animals
