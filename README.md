[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">  

Посмотреть скриншоты можно [здесь](https://github.com/number92/Events/tree/master/screenshots)

Склонировать репозиторий:
```
git@github.com:number92/Events.git
```
Создайте .env файл в корне
Создайте SECRET_KEY, используя [сервис](https://djecrety.ir/)  

запустить в докере:  
```
docker compose up -d
```
Копирование статики админки
```
docker compose exec backend python manage.py collectstatic
```

Конечные точки
```
/api/events/
/api/events/<id>/
/api/organizations/
/chat/
/chat/str:<room>/
```
