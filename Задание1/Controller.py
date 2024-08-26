class ArticlesController:
    def __init__(self, model):
        self.model = model

    def default_action(self):
        if self.model.get_articles():
            return self.model.get_articles()
        else:
            return 'Нет данных!'

    def only_titles_list(self):
        titles = []
        data = self.model.get_articles()
        if data:
            for elem in data:
                for key in elem.keys():
                    titles.append(key)
        else:
            return 'Нет данных!'
        return titles

    def only_authors_list(self):
        authors = []
        data = self.model.get_articles()
        if data:
            for elem in data:
                for value in elem.values():
                    authors.append(value['author'])
        else:
            return 'Нет данных!'
        return authors

    def only_publications_list(self):
        publications = []
        data = self.model.get_articles()
        if data:
            for elem in data:
                for value in elem.values():
                    publications.append(value['publication'])
        else:
            return 'Нет данных!'
        return publications

    def only_titles_authors_dict(self):
        titles_authors = {}
        data = self.model.get_articles()
        if data:
            for elem in data:
                for key, value in elem.items():
                    titles_authors[key] = value['author']
        else:
            return 'Нет данных!'
        return titles_authors

    def add_article(self, title, author, content_length, publication, description, filename, validation):
        if validation in ['is_superuser', 'is_stuff']:
            self.model.add_article(title, author, content_length, publication, description, filename)
            return 'Статья успешно добавлена!'
        else:
            return 'Нет доступа!'
