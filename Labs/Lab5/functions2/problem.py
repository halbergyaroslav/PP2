movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def task1(movie_name):
    for e in movies:
        if e['name'] == movie_name: return (e['imdb'] > 5.5)      
        
def task2():
    sublist = list()
    for e in movies: 
        if task1(e['name']): sublist.append(e)
    return sublist

def task3(category_name):
    sublist = list()
    for e in movies:
        if e['category'] == category_name: sublist.append(e)
    return sublist

def task4(list_movies):
    sum = 0
    for e in list_movies:
        sum += e['imdb']
    return sum / len(list_movies)

def task5(category_name):
    return (task4(task3(category_name)))

#print(task1('Exam'))
#print(task1('Detective'))

#print(task2())

#print(task3('Romance'))

#print(task4([{"name": "Detective", "imdb": 7.0, "category": "Suspense"}, {"name": "Exam", "imdb": 4.2, "category": "Thriller"}, {"name": "We Two", "imdb": 7.2, "category": "Romance"}]))

#print(task5('Suspense'))