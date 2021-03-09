MEME GENERATOR
---------------

This project is the outcome of Udacity's Intermediate python Nanodegree.
It teaches you structuring code correctly, writing clear code and cares 
about design patterns. In this project we have used a Strategy Design 
Pattern to parse different Ingestors.

How to run:

in the main directory you have to install the 
requirements.txt using pip

```pip install requirements.txt```

afterwards you can start the application using 

```flask run```

It will start a development WSGI on the default port 5000.

The application is a meme generator with 2 simple templates.
For some reason Udacity thinks I don't use a virtualenv, all these packages 
in requirements.txt come from a virtualenv. Well, it installed what you see.

I installed
```pip install pandas Pillow requests python-docx Flask```

and it installed all other packages, like urllib3 which the reviewer wrote 
it should NOT be there.

```
(project-2-env) mucko@PSmac01 meme_proj % pip freeze
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
Flask==1.1.2
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.3
lxml==4.6.2
MarkupSafe==1.1.1
numpy==1.20.1
pandas==1.2.3
Pillow==8.1.2
python-dateutil==2.8.1
python-docx==0.8.10
pytz==2021.1
requests==2.25.1
six==1.15.0
urllib3==1.26.3
Werkzeug==1.0.1
(project-2-env) mucko@PSmac01 meme_proj % 
```

It was a nice project. 
And I must say relative import is difficult!