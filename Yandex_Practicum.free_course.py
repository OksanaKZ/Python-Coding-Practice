bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.
for i in range(1, 6):
    # На каждой итерации цикла
    # к переменной bunny_counter будет дописываться
    # очередная цифра, запятая и пробел (чтобы числа в строке не слиплись).
    # Получившееся значение будет присвоено той же переменной bunny_counter
    bunny_counter = bunny_counter + str(i) + ', '
print(bunny_counter + 'вышел зайчик погулять!')

#1, 2, 3, 4, 5, вышел зайчик погулять!


for messages_count in range(6):
    if messages_count > 0:
        print('Новых сообщений: ' + str(messages_count))
    else:
        print('У вас нет сообщений')

#У вас нет сообщений
#Новых сообщений: 1
#Новых сообщений: 2
#Новых сообщений: 3
#Новых сообщений: 4
#Новых сообщений: 5


countdown_str = ''
for i in reversed(range(0, 11)):
    countdown_str = countdown_str + str(i) + ', '
countdown_str = countdown_str + 'поехали!'
print(countdown_str)

#10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, поехали!


print('Это первый этаж.')
for i in range(2, 7):
    print('А это', i, 'этаж, он на один выше, чем этаж', i - 1)

#Это первый этаж.
#А это 2 этаж, он на один выше, чем этаж 1
#А это 3 этаж, он на один выше, чем этаж 2
#А это 4 этаж, он на один выше, чем этаж 3
#А это 5 этаж, он на один выше, чем этаж 4
#А это 6 этаж, он на один выше, чем этаж 5


#Функция reversed() переворачивает и список, и диапазон; чтение любой последовательности начнётся с конца.
for i in reversed(range(1, 13)):
    print(i, 'бомм!')
print('C новым годом!')

#12 бомм!
#11 бомм!
#10 бомм!
#9 бомм!
#8 бомм!
#7 бомм!
#6 бомм!
#5 бомм!
#4 бомм!
#3 бомм!
#2 бомм!
#1 бомм!
#C новым годом!

#импортируем библиотеку для работы с API-запросами:
import requests
import json

city = 'Омск'

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2) 

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
wind_speed = round(weather_data['wind']['speed'])

print('Сейчас в городе', city, str(temperature), 'градусов')
print('Ощущается как', str(temperature_feels), 'градусов')
print('Скорость ветра', str(wind_speed), 'м/с')
