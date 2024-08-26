class MovieView:
    def __init__(self, controller):
        self.controller = controller

    def print_default_action(self):
        articles = self.controller.default_action()
        if articles == 'Нет данных!':
            print('Нет данных!')
        else:
            for article in articles:
                for key, value in article.items():
                    print(f'''Фильм - {key}
Жанр: {value["genre"]}
Режиссер: {value["director"]}
Год: {value["year"]}
Длительность: {value["length"]}
Студия: {value["studio"]}
Актеры: {", ".join(value["actors"])}''')
                    print()

    def print_titles(self):
        titles = self.controller.only_titles_list()
        if titles == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join(titles))
            print()

    def print_genres(self):
        genres = self.controller.only_genres_list()
        if genres == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join(genres))
            print()

    def print_directors(self):
        directors = self.controller.only_directors_list()
        if directors == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join(directors))
            print()

    def print_years(self):
        years = self.controller.only_years_list()
        if years == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join([str(i) for i in years]))
            print()

    def print_studios(self):
        studios = self.controller.only_studios_list()
        if studios == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join(studios))
            print()

    def print_titles_genres(self):
        titles_genres = self.controller.only_titles_genres_dict()
        if titles_genres == 'Нет данных!':
            print('Нет данных!')
        else:
            for key, value in titles_genres.items():
                print(f'Фильм - {key}, Жанр - {value}')

    def add_movie(self, title, genre, director, year, length, studio, actors: list, filename, validation='user'):
        print(self.controller.add_movie(title, genre, director, year, length, studio, actors, filename, validation))
