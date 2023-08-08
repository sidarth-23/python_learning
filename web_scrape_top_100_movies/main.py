import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

movies_data = soup.find_all(name='h3', class_='title')

movie_name = []
for item in movies_data:
    movie_name.append(item.getText())

movie_name = movie_name[::-1]
print(movie_name)

with open('movies.txt', encoding='utf8', mode='w') as file:
    for item in movie_name:
        file.write(f'{item}\n')
