# bbakdoc

### Prerequisite
* [Docker](https://docs.docker.com/docker-for-mac/install/)
* Python3.6 is a programming language.


### Optional-Prerequisite
* [Pycharm](https://www.jetbrains.com/pycharm/) is the Python IDE for professional developers. 


### Core Library
* [django](https://www.djangoproject.com/) is high-level Python Web framework that encourage rapid development!!!
* [django-channel](https://channels.readthedocs.io/en/latest/) is web socket library based on django


### DATA Backends

* mysql is persistence data backend. 
* redis is cache backend.

#### run mysql by docker
```bash
docker run --detach --env MYSQL_USER=root --env MYSQL_ALLOW_EMPTY_PASSWORD=yes \
 --rm \
 --volume $PWD/.mysql:/var/lib/mysql  -p 3306:3306 \
 --name=mysql-5.6.41 \
 mysql:5.6.41
```

#### run mysql by redis
```bash
docker run -p 6379:6379 -d redis:2.8
```




--- 

### RunServerPlus
* https://django-extensions.readthedocs.io/en/latest/runserver_plus.html
