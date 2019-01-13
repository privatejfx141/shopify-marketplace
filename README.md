# Shopify Summer 2019 Developer Intern Challenge
My attempt at the Summer 2019 Developer Intern Challenge using Django, a Python Web framework.

## Requirements
The app is written in Python 3.7. The only dependencies required are Django and TastyPie, which supplies the REST framework and authorization.
```
$ pip install django
$ pip install tastypie
```

## Usage
### Starting up the Server
Run the following commands to start up the server at `localhost:8000`:
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

### API Usage
To get a list of all products, send a `GET` request to:
```
http://localhost:8000/api/products/
```

To get a specific product, send a `GET` request to:
```
http://localhost:8000/api/products/<product-id>/
```

### Running Tests
To execute the test cases that are specified under `api\tests.py`, run the following command:
```
$ ./manage.py test
```
