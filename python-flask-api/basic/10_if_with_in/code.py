movies = {'The Matrix', 'Coda', 'Her', 'Monty Python'}
user_choice_movie = input('Enter something that you\'ve watched recentrly: ')

if user_choice_movie in movies:
    print(f'I\'ve watched {user_choice_movie.lower()} too')
else:
    print('I haven\'t watched that yet')
