# MTM-API

MTM is an app used in the course CMPUT401 at the University of Alberta.  The application was developed by Diego Serrano during the Winter of 2018.

## Installation 

First clone the application code into any directory on your disk (preferably, not using spaces in the folder structure)
```sh
$ git clone https://github.com/dfserrano/MTM-API.git
$ cd MTM-API
```

Install virtualenv with pip
```sh
$ pip install virtualenv
```

Create a new virtualenv and activate it
```sh
$ virtualenv venv
$ source venv/bin/activate
```

Install the required libraries: flask-restplus, Flask-SQLAlchemy, and flask-cors
```sh
pip install flask-restplus
pip install Flask-SQLAlchemy
pip install -U flask-cors
```

Run the application:
```sh
./run.sh
```

The application will be available at port 8888.  Then, to access the Swagger API documentation, the address you have to type is:

http://localhost:8888/api


## References
These resources were used for the creation of this app:

- Flask: http://flask.pocoo.org/

- Flask-restplus: http://flask-restplus.readthedocs.io/en/stable/

- Flask-CORS: https://pypi.python.org/pypi/Flask-Cors

- Useful tutorial: http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/

