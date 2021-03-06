# Ближайшие бары

Данная программа позволяет с помоoью открытых данных, взятых с сайта [http://data.mos.ru](http://data.mos.ru)
найти самый вместительный бар и самый маленький, а так-же найти самый ближний к вам бар.

# Требования к окружению.

Для запуска данного скрипта необходим Python версии 3.x и старше.

# Как установить?

Установка заключается в git clone репозитория на Ваш компьютер. 

# Как запустить?

С помощью командной строки прейдите в каталог с репозиторием на Вашем компьютере, запустите файл bars.py со следующими параметрами: 
-c долгота широта _путь_к_файлу_с_данными_  
Для примера возьмем следующие данные: файл с данными лежит в одном каталоге с файлом bars.py, координаты возьмем из сервиса Яндекс.Карты, адрес: Мясницкая улица, 40А, координаты: долгота - 55.766415, широта - 37.640596:

```bash
python bars.py -c 55.766415 37.640596 data.txt
```

Результатом работы программы будет вывод следующих данных:

```bash
Хотите много места? Тогда вам в "Спорт бар «Красная машина»" в нем 450 мест, он находится по адресу: г. Москва, Автозаводская улица, дом 23, строение 1, телефон - +7 (905) 795-15-84
Самым маленьким заведением является "БАР. СОКИ" - 0 мест, находящийся по адресу: г. Москва, Дубравная улица, дом 34/29, телефон - +7 (495) 258-94-19
Рядом с Вами находится Гранд Бурбон Стрит, в нем - 85 мест, он находиться по адресу: г. Москва, Потаповский переулок, дом 5, строение 2, телефон - +7 (495) 625-94-24
```

Запуск на Linux происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
