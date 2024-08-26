class MovieController:
    def __init__(self, model):
        self.model = model

    def default_action(self):
        if self.model.get_movies():
            return self.model.get_movies()
        else:
            return 'Нет данных!'

    def only_titles_list(self):
        titles = []
        data = self.model.get_movies()
        if data:
            for elem in data:
                for key in elem.keys():
                    titles.append(key)
        else:
            return 'Нет данных!'
        return titles

    def only_genres_list(self):
        genres = []
        data = self.model.get_movies()
        if data:
            for elem in data:
                for value in elem.values():
                    genres.append(value['genre'])
        else:
            return 'Нет данных!'
        return genres

    def only_directors_list(self):
        directors = []
        data = self.model.get_movies()
        if data:
            for elem in data:
                for value in elem.values():
                    directors.append(value['director'])
        else:
            return 'Нет данных!'
        return directors

    def only_years_list(self):
        years = []
        data = self.model.get_movies()
        if data:
            for elem in data:
                for value in elem.values():
                    years.append(value['year'])
        else:
            return 'Нет данных!'
        return years

    def only_studios_list(self):
        studios = []
        data = self.model.get_movies()
        if data:
            for elem in data:
                for value in elem.values():
                    studios.append(value['studio'])
        else:
            return 'Нет данных!'
        return studios

    def only_titles_genres_dict(self):
        titles_genres = {}
        data = self.model.get_movies()
        if data:
            for elem in data:
                for key, value in elem.items():
                    titles_genres[key] = value['genre']
        else:
            return 'Нет данных!'
        return titles_genres

    def add_movie(self, title, genre, director, year, length, studio, actors: list, filename, validation):
        if validation in ['is_superuser', 'is_stuff']:
            self.model.add_movie(title, genre, director, year, length, studio, actors, filename)
            return 'Фильм успешно добавлена!'
        else:
            return 'Нет доступа!'
