# CrawlingRules 1.0

Crawling Helper with Defining Rules in Django (Python)

## How to run

This program is written in Python 3.x, so you need to install it.

1. Activate your virtual environment (recommend)

```shell
$ source ~/venv/bin/activate
```

2. Install django, bs4 (beautifulsoup)

```shell
(venv) $ pip install django, bs4
```

3. Create secrets.json file

```shell
(venv) $ echo "{\"SECRET_KEY\": \"...\"}" > secrets.json
```

You must put your secret key on `\"...\"` (string).

How to get your own secret key: https://miniwebtool.com/django-secret-key-generator/

4. Start server (localhost:8000)

```shell
(venv) $ python manage.py runserver
```

5. Access http://localhost:8000 in your web browser

