import os
import string
from films_titles import films_titles
from film_awards import films_awards

if not os.path.exists("Harry Potter"):
    os.mkdir("Harry Potter")
if not os.listdir("Harry Potter"):
    for film in films_titles["results"]: #В середині дерикторії Harry Potter створіть 8 дерикторій з назвою кожної частни.
        title = film["title"]
    for letter in string.ascii_uppercase: #В середині дерикторій кожної частини фільму створіть теки(дерикторії) від A до Z. Використовуйте модуль OS.
        directory = os.path.join("Harry Potter", title, letter)
        os.makedirs(directory)


award_list = [] #Для кожного фільму створіть новий список, він має зберігати словники з ключем award_name та його значенням, ключем award та його значенням, ключем type та його значенням.
award_list_sorted = []
for film in films_titles['results']:
  film_dict = {'title':film['title'], 'awards':[]}
  for awards in films_awards:
    for award in awards['results']:
      if award['movie']['title'] == film['title']:
        film_dict['awards'].append({
                            'award_name': award['award_name'],
                            'award': award['award'],
                            'type': award['type']
                          })
  award_list.append(film_dict)
print(award_list)



for award in award_list: #Відсортуйте кожен список з нагородами за алфавітом по ключу award_name. Використай sorted та lambda функції.
  sorted_awards = sorted(award['awards'], key=lambda x: x['award_name'])
  award_list_sorted.append({'title':award['title'],'awards': sorted_awards})
print(sorted_awards)

for i in award_list_sorted:
  for j in i['awards']:
    letter_award_name = j['award_name'][0]
    folder_award_name = f'Harry Potter/{i["title"]}/{letter_award_name}/{j["award_name"]}.txt' #Для кожного фільму у теках з літерами від A до Z створи txt файл з назвою(ключ award_name) нагороди яка починаєтья на відповідну літеру
    print(folder_award_name)
    file_award = open(folder_award_name, 'w')
    file_award_name = open(folder_award_name, 'a')
    file_award_name.write(f'{j["award"]}') #У файл з ім'ям кожної нагороди перенеси всі назви номінацій цієї(award) нагороди.



if not os.path.exists('film_player/film_storage'): #homework15 В середині пакету film_player створіть дерикторію film_storage. А в середині film_storage дерикторії від A до Z
    os.makedirs('film_player/film_storage')

for letter in range(ord('A'), ord('Z')+1):
    letter_dir = f'film_player/film_storage/{chr(letter)}'
    if not os.path.exists(letter_dir):
        os.makedirs(letter_dir)