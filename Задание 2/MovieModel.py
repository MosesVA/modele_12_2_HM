import json


class MovieModel:
    def __init__(self):
        self.movies = []

    def get_movies(self):
        return self.movies

    def add_movie(self, title, genre, director, year, length, studio, actors: list, filename):
        data = {}
        data[f'{title}'] = {'genre': genre,
                            'director': director,
                            'year': year,
                            'length': length,
                            'studio': studio,
                            'actors': actors}
        self.movies.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.movies, fp, ensure_ascii=False, indent=2)
