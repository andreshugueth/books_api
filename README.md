# Books API

## Dev Setup

* Postgres database setup:
  * `sudo apt-get install postgresql`
  * `sudo su - postgres`
  * `createdb books_db`
  * `createuser <username> -P`
  * Enter the interactive postgreSQL console by typing: `psql`
  * Once in the console, grant your user all the privileges on books_db:
`GRANT ALL PRIVILEGES ON DATABASE learning_management_system TO <username>;`
  * In order to use the test suite, you'll need a user with create database right. You might use the same user or create a new one, enter the following in psql: `ALTER USER <username> CREATEDB;`
* Create a python 3.6 virtual env (Perhaps with [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or [Anaconda](https://www.anaconda.com/products/individual))
* Activate your virtual env and install requirements: `pip install -r requirements.txt`
* Implement flask code for migrations:
  * `flask db init`
  * `flask db migrate`
  * `flask db upgrade`

## Run server

To run the server, execute the following command:

```bash
python app.py
```

## Swagger docs

To see swagger docs, please go to the enpoint:
```
http://127.0.0.1:5000/apidocs/
```
<p align=center>
<img src="https://i.imgur.com/eeuA007.png" atl="swagger-img" width=600px>
</p>
