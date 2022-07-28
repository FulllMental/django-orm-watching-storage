# Пишем пульт охраны банка

Данный репозиторий это сайт с интерфейсом пульта охраны хранилища банка, позволяющий узнать данные о сотрудниках находящихся
в хранилище в данный момент, время входа, выхода и сколько сотрудники там находятся. А так же насколько данный визит подозрителен
в рамках средней продолжительности рабочего визита сотрудника банка.

Для корректной работы потребуется доступ к базе данных банка.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Необходимо подключиться к базе данных банка, заполнив соответствующие данные `DATABASES` в `settings.py`:
```python
'ENGINE': ...,
'HOST': ...,
'PORT': ...,
'NAME': ...,
'USER': ...,
'PASSWORD': ...,
```

Для запуска сервера:
```commandline
python main.py runserver localhost:8000
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).