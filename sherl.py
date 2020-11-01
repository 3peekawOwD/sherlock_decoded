import requests
import html2text
import urllib3
from bs4 import BeautifulSoup
import lxml

def car_ua():
	num = input("Введите номер: ")
	req = requests.get("https://fakescreen-3d98a1.eu1.kinto.io/ua?num=" + num).json()
	if req["error"]:
		return print("Ничего не найдено")
	print("🚘")
	print("├ Регион: " + req["region"]["name"])
	print("├ Марка: " + req["vendor"])
	print("├ Модель: " + req["model"])
	if req["stolen"] == True:
		print("├ Проверка на угон: Числится в угоне")
	else:
		print("├ Проверка на угон: Не числится в угоне")
	print("├ Заметки: " + req["operations"][0]["notes"])
	print("└ Дата последней регистрации: " + req["operations"][0]["regAt"])

def tel():
	num = input("Введите номер телфона: ")
	try:
		req = requests.get("http://rosreestr.subnets.ru/?get=num&num=" + num + "&format=json").json()
		print("📱")
		print("├ Оператор: " + req["0"]["operator"])
		print("├ Регион: " + req["0"]["region"])
		print("└ DEF Код: " + req["0"]["from"] + "-" + req["0"]["to"])
	except:
		print("Произошла ошибка")

def nick():
	nick = input("Введите ник: ")
	req = requests.get("http://api.usersbox.su/sherlock?q=" + nick).json()
	print("Получение информации...")
	print('\n'.join(req["response"]))

def ip():
	ip = input("Введите IP: ")
	try:
		req = requests.get("http://demo.ip-api.com/json/" + ip + "?fields=66842623&lang=ru").json()
		print("🌐")
		print("├ Страна: " + req["country"])
		print("├ Регион: " + req["regionName"])
		print("├ Город: " + req["city"])
		print("└ Провайдер: " + req["as"])
	except:
		print("Произошла ошибка")

def mentions():
	userId = input("Введите ID пользователя: ")
	print("https://vk.com/feed?obj=" + userId + "&q=&section=mentions")

def fio():
	name = input("Введите ник/ФИ: ")
	req = requests.get("https://phonebook.space/?input=" + name + "&check=Name", headers={"Cookie": "__atuvc=3%7C44%2C4%7C45; __atuvs=5f9e30e7193af6a7003"})
	soup = BeautifulSoup(req.content, 'lxml')
	for result in soup.select("div.results > ul"):
		print(result.get_text().replace(" ", ""))

def getcontact():
	tel = input("Введите номер телефона: ")
	req = requests.get("https://phonebook.space/?input=+" + tel, headers={"Cookie": "__atuvc=3%7C44%2C4%7C45; __atuvs=5f9e30e7193af6a7003"})
	soup = BeautifulSoup(req.content, 'lxml')
	for result in soup.select("div.results > ul"):
		print(result.get_text().replace(" ", ""))

banner = """
       ,_
     ,'  `╲,_
     |_,-'_)
     /##c '╲  (
    ' |'  -{.  )
      /╲__-' ╲[]
     /`-_`╲            Sherlock Apps
     '     ╲ 2.1
   _____________________________________________
   |   Termux-Lab  |   TG: @termuxlab | Beta   |
   |-------------------------------------------|
   | Decoded by 3peekawOwD | @peekawOwD_channel|
   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Возможности:
[1] - Поиск авто(UA)
[2] - Инф о номере
[3] - Поиск по нику
[4] - IP-Чек
[5] - Упоминания (Vk)
[6] - Получить пароль
[7] - Актив Трекер (Vk)
[8] - Глаз Шерлока 
[9] - Поиск номера телефона по имени
[10] - Поиск авто(RU)
[11] - Поиск по фото
"""

print(banner)

while True:
	mode = input("Выберите режим: ")

	if mode == "1":
		car_ua()
	elif mode == "2":
		tel()
	elif mode == "3":
		nick()
	elif mode == "4":
		ip()
	elif mode == "5":
		mentions()
	elif mode == "8":
		getcontact()
	elif mode == "9":
		fio()
	else:
		print("Я вас не понял")