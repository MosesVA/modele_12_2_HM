import json


class ArticleModel:
    def __init__(self):
        self.articles = []

    def get_articles(self):
        return self.articles

    def add_article(self, title, author, content_length, publication, description, filename):
        data = {}
        data[f'{title}'] = {'author': author,
                            'content_length': content_length,
                            'publication': publication,
                            'description': description}
        self.articles.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.articles, fp, ensure_ascii=False, indent=2)
