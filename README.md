# Movie List
This project allows you to add, read, update, delete the movies.

## Installation
Use the package manager pip to install the dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

## Documentation

User needs to login to use crud operations on movies data

To login,

Http call: POST

```python 
http://127.0.0.1:5000/login

{
  "username": "admin",
  "password": "admin"
}

```

You will get the token. Use the token to access the movies API.

Pass the token in request headers in all the APIs to access

```python
x-access-token: 'generated-token'
```



To add the movie,

Http call: POST

```python
http://127.0.0.1:5000/movie

{
  "productionCompany": "Company",
  "releaseDate": "Date,
  "title": "Title"
}

```
To get all the movies,

Http call: GET

```python
http://127.0.0.1:5000/movie

```

To update the movies, 

This will update the details of movie using the title key

Http call: PUT

```python
http://127.0.0.1:5000/movie

{
  "productionCompany": "Company",
  "releaseDate": "Date,
  "title": "Title"
}
```

To delete the movie,
Http call: DELETE

```python
http://127.0.0.1:5000/movie

{
  "title": "Title"
}