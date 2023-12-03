# ТЕСТ БИБЛИОТЕКИ ФЛОРЕСТА "FLORESTLIBRARYPYTHONPREMIUM".
# ПО ВОПРОСАМ ОБРАЩАЕМСИ В ТГ: FlorestOne4185
# Удачного пользования. Юни - крашиха.

import florestlibrarypythonpremium.florestlibrarypythonpremium as florestlib # импорт библиотеки.
 
### Класс "Florest"
a = florestlib.Florest.generate_otvetka(cool=5) # Генерируем ответку. Крутость может быть от 1 до 5
print(a) # Выводим ответку на экранчик
b = florestlib.Florest.random_chisle(1, 5) # Выбирает рандомную цифру от 1 до 5
print(b) # Выводим цифорку на экран.
f = florestlib.Florest.random_choice(list=['Абоба', 'Тест', 'Слава Юни!'])
print(f)
pon = int(input(f'Введите число от 1 до 5:')) # запрашиваем число для угадайки
c = florestlib.Florest.ugadayka(chislo=pon) # Проверяем, так ли, что chislo равно тому, что ввел пользователь.
print(c) # Возвращаем результат.
#Переменные:
florestlib.Florest.name
florestlib.Florest.nickname
#=================

### Класс "Response"
ff = florestlib.Response.write_webhook_message(link='Введите ссылку на вебхук, короч', message='Введите сообщение') # Отправляем сообщение от имени вебхука
print(ff) # Выводим результат в консоль.
af = florestlib.Response.send_embed(link='Ссылка на вебхук', title='Название эмбеда', description='То что ниже названия') #Отправляем эмбед от имени вебхука
print(af)
ad = florestlib.Response.rcon(ip='IP вашего сервера', port='Порт вашего сервера (RCON)', password='Пароль от RCON вашего сервера', command='Команда, которую вы хотите прописать в RCON консоль. Пример: `say`.', argument='Он только один. К примеру, `say Привет!`.') # Отправить команду на сервер с помощью RCON
print(ad) # Выводим результат
#===================

### Класс "UniKrol"
# Переменные
florestlib.UniKrol.uni_name
florestlib.UniKrol.uni_surname
#==================

#Вы можете найти пременение всем из этих функций. Они значительно облегчают написание кода и другие вещи. Пожалуйста, поддержите меня.
#Канал YouTube: https://youtube.com/@florestone4185
#Канал Telegram: https://t.me/florestchannel
