# bbakdoc

```bash
docker run --detach --env MYSQL_USER=root --env MYSQL_ALLOW_EMPTY_PASSWORD=yes \
 --rm \
 --volume $PWD/.mysql:/var/lib/mysql  -p 3306:3306 \
 --name=mysql-5.6.41 \
 mysql:5.6.41
```

```bash
docker run -p 6379:6379 -d redis:2.8
```


### RunServerPlus
* https://django-extensions.readthedocs.io/en/latest/runserver_plus.html
