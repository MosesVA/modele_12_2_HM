from MovieModel import MovieModel
from View import MovieView
from Controller import MovieController

model = MovieModel()
controller = MovieController(model)
view = MovieView(controller)

view.print_default_action()
view.print_titles()
view.print_genres()
view.print_directors()
view.print_years()
view.print_studios()
view.print_titles_genres()
print()
view.add_movie('Гарри Поттер', 'Фантастика', 'Крис Коламбус', 2001, '2 ч 32 мин',
               'Warner Bros. Pictures', ['Дэниэл Рэдклифф', 'Руперт Гринт', 'Эмма Уотсон'], 'movies.json', 'is_stuff')
view.add_movie('1+1', 'Драма', 'Оливье Накаш', 2011, '1 ч 52 мин', 'Chaocorp', ['Франсуа Клюзе', 'Омар Си'],
               'movies.json', 'is_stuff')
view.add_movie('Бойцовский клуб', 'Триллер', 'Дэвид Финчер', 1999, '2 ч 19 мин', 'Atman Entertainment',
               ['Эдвард Нортон', 'Брэд Питт'], 'movies.json')
print()
view.print_default_action()
view.print_titles()
view.print_genres()
view.print_directors()
view.print_years()
view.print_studios()
view.print_titles_genres()
