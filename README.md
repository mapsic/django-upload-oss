# Django File Upload Tutorial

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)

Code example used in the tutorial series on Django File Upload.

Watch it on YouTube: [Django 2.1 File Upload](https://www.youtube.com/playlist?list=PLLxk3TkuAYnpm24Ma1XenNeq1oxxRcYFT)

Subscribe to my YouTube channel: [youtube.com/VitorFreitas](https://www.youtube.com/VitorFreitas?sub_confirmation=1)

Read the Django storage backends for AliCloud OSS: [django-oss-storage](https://github.com/aliyun/django-oss-storage)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:mapsic/django-upload-oss.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Then update settings.py file for follow keys:

* OSS_ACCESS_KEY_ID

* OSS_ACCESS_KEY_SECRET

* OSS_BUCKET_NAME

* OSS_ENDPOINT


Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/sibtc/django-upload-example/blob/master/LICENSE).