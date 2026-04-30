import time, os
os.system('clear')
print("\n")
print("Добро пожаловать в ZdHub! v0.1")
print("Хаб сделан ArtiomZd\n")
time.sleep(1)
nick = input("Введите никнейм: ")
print()
time.sleep(1)
print(f"Поиск аккаунта {nick}...")
time.sleep(3)
print(f"{nick} найден")
time.sleep(1)
#Пароль 420
while True:
	code = input("Введите код администратора: ")
	if code =="420":
		time.sleep(2)
		print("Успешно!")
		time.sleep(3)
		os.system('clear')
		print("\n")
		print("Загрузка в хаб...")
		time.sleep(2)
		break
	else:
		time.sleep(2)
		print("Неправильный код!")
os.system('clear')
time.sleep(2)
while True:
	print()
	print(f"Цель: {nick}\n")
	print()
	print("Эксплойты:\n")
	time.sleep(0.5)
	print("[ 1 ] Попытаться подобрать пароль")
	time.sleep(0.2)
	print("[ 2 ] Дюпнуть робуксы")
	time.sleep(0.2)
	print("[ 3 ] Выйти")
	otvet = input("Введите цифру: ")
	
	if otvet =="1":
		print()
		print("Загрузка PasswordHackBeta. . .")
		time.sleep(3)
		print("Иди нахуй блядь мне лень хакать")
		print("\n")
		time.sleep(1)
		print("\n")
		input("ENTER чтобы загрузить меню . . .")
		os.system('clear')

	if otvet =="2":
		print()
		print("Загрузка RobuxDupeBeta. . .")
		time.sleep(3)
		print("Какой дюп робуксов ребенок")
		print("\n")
		time.sleep(1)
		print("\n")
		input("ENTER чтобы загрузить меню . . .")
		os.system('clear')
		
	if otvet=="3":
		print("\n")
		print("Я и так знал что мой хаб хуйня")
		time.sleep(5)
		break
		exit()
