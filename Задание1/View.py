class ArticlesView:
    def __init__(self, controller):
        self.controller = controller

    def print_default_action(self):
        articles = self.controller.default_action()
        if articles == 'Нет данных!':
            print('Нет данных!')
        else:
            for article in articles:
                for key, value in article.items():
                    print(f'''Статья - {key}
Автор: {value["author"]}
Кол-во знаков: {value["content_length"]}
Издание(сайт): {value["publication"]}
Краткое описание: {value["description"]}''')
                    print()

    def print_titles(self):
        titles = self.controller.only_titles_list()
        if titles == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join(titles))
            print()

    def print_authors(self):
        authors = self.controller.only_authors_list()
        if authors == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join(authors))
            print()

    def print_publications(self):
        publications = self.controller.only_publications_list()
        if publications == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join([str(i) for i in publications]))
            print()

    def print_titles_authors(self):
        titles_authors_dict = self.controller.only_titles_authors_dict()
        if titles_authors_dict == 'Нет данных!':
            print('Нет данных!')
        else:
            for key, value in titles_authors_dict.items():
                print(f'Статья - {key}, Автор - {value}')

    def add_article(self, title, author, content_length, publication, description, filename, validation='user'):
        print(
            self.controller.add_article(title, author, content_length, publication, description, filename, validation))
