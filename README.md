[![CircleCI](https://circleci.com/gh/fabinhojorge/urlshortener.svg?style=svg)](https://circleci.com/gh/fabinhojorge/urlshortener)

# URL Shortener

The idea of this project is to study some technologies and practice. Here you will find a URL shortener like [bit.ly](http://bit.ly).

## How to install and Run
After activate your Python Virtual Environment (_venv_) run the below command:

```
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

So you can access in the local URL: _[localhost:8000](localhost:8000/)_


## How to use
1. In the home page you can find an input text. Type the URL there and press Enter/Submit button
2. It will generate a short URL. 
3. If you click in the short URL you will be redirect to the original URL
4. To get the statistics you just add a plus (_+_) signal in the end of the URL, example:
    * URL: _localhost:8000/2A14S6REML_
    * Statistic URL: _localhost:8000//2A14S6REML+_

Obs: Replace the _localhost:8000_ by your domain


## Libraries
* Django
* Django Rest Framework
* Bootstrap
* JQuery


## To Do
* [X] Enhance the logic for redirect URL. It´s not working for all the URLs
* [X] Add the continuous integration build and test (Circleci)
* [X] Add test cases for BE
* [ ] Add test cases for FE


## Screen Shots

__Home Page__
![Home page](project_assets/home_page.jpg)

__Statistic Page__
![Statistic page](project_assets/statistic.jpg)

__Redirect Functionality__
![Redirect functionality](project_assets/redirect_functionality.jpg)

