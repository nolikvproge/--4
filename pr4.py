import requests
from bs4 import BeautifulSoup


def parse_imdb_top_movies() -> object:
    url = 'https://www.imdb.com/chart/top/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        movies = soup.find_all('td', class_='titleColumn')

        for index, movie in enumerate(movies, start=1):
            title = movie.find('a').text
            year = movie.find('span', class_='secondaryInfo').text
            rating = movie.find_next('td', class_='ratingColumn imdbRating').text.strip()

            print(f'{index}. {title} ({year}) - Rating: {rating}')
    else:
        print('Ошибка.')


if __name__ == '__main__':
    print('IMDb Top 250 Фильмов:\n')
    parse_imdb_top_movies()
