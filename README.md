# CrawlingRules 1.0

Crawling Helper with Defining Rules in Django (Python)

## How to run

This program is written in Python 3.x, so you need to install it.

1. Activate your virtual environment (recommend)

```shell
$ source ~/venv/bin/activate
```

2. Install django, bs4 (beautifulsoup) packages

```shell
(venv) $ pip install django bs4
```

3. Create secrets.json file in the main directory

```shell
(venv) $ cd /path/to/CrawlingRules
(venv) $ echo "{\"SECRET_KEY\": \"...\"}" > secrets.json
```

You must put your secret key on `"..."` (string).

How to get your own secret key: https://miniwebtool.com/django-secret-key-generator/

4. Migrate

```shell
(venv) $ python manage.py migrate
```

5. Start server (localhost:8000)

```shell
(venv) $ python manage.py runserver
```

6. Access http://localhost:8000 in your web browser

