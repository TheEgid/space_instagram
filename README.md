# Космический Инстаграм

Проект предназначен для автоматизированного сбора и выкладывания в инстаграм фотографий космической тематики с сайтов [hubblesite.org](http://hubblesite.org) и [spacex.com](https://www.spacex.com)

### Как установить

Скачиваем файлы в папку space_instagram. В этой же папке создаем .env файл. Ваш .env должен содержать строки:

```
LOGIN_INST=ваш_инстаграм_логин
PASSWORD_INST=ваш_инстаграм_пароль
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Использование

Используем консольный ввод. Аргументом передаем название любой коллекции (например, "wallpaper") изображений с сайта [hubblesite.org](http://hubblesite.org) 

```
python main.py

python main.py wallpaper

```

Программа выводит в консоль лог своей работы. Пример лога

```
INFO:root:download & saved images/space1.jpg
2019-01-02 00:51:41,505 - INFO - Photo 'images\space1.jpg' is uploaded.
INFO:root:timeout= 21
```

После этого сообщения полученные изображения загружены в инстаграм

```
INFO:root:finished!
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
