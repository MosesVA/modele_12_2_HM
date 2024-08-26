from ArticleModel import ArticleModel
from View import ArticlesView
from Controller import ArticlesController

model = ArticleModel()
controller = ArticlesController(model)
view = ArticlesView(controller)

view.print_default_action()
view.print_titles()
view.print_authors()
view.print_publications()
view.print_titles_authors()
print()
view.add_article('Позор Нации', 'Петр Пошляков', 320, 'truenation.com', 'Статья о человеке, предавшем нацию',
                 'articles.json', 'is_stuff')
view.add_article('Восход Солнца', 'Дмитрий Пергн', 516, 'Китайская газета', 'О том как красив восход в Китае',
                 'articles.json', 'is_stuff')
view.add_article('Компьютеры - Зло', 'Максим Шаповалов', 795, 'comp-evil.ru', 'Как игры негативно влияют на мозг',
                 'articles.json')
view.add_article('Как выпечь хлеб', 'Лиза Булкина', 150, 'make-bread.ru', 'Рецепт вкусного хлеба', 'articles.json',
                 'is_stuff')
view.add_article('Заноза', 'Андрей Рубанков', 246, 'instruments.ru', 'Как вытащить занозу', 'articles.json', 'is_stuff')
view.add_article('Топ-5 игр', 'Алексей Знатков', 170, 'Журнал Игромания', 'Субъективный топ от автора', 'articles.json',
                 'is_stuff')
print()
view.print_default_action()
view.print_titles()
view.print_authors()
view.print_publications()
view.print_titles_authors()
