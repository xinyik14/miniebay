
## steps for mysql setup with docker
```
docker run -p 3306:3306 --name=miniebay-mysql -e MYSQL_ROOT_PASSWORD=test -e MYSQL_ROOT_HOST=% -d mysql/mysql-server:5.7
docker exec -it miniebay-mysql mysql -uroot -ptest -e 'create database miniebay';
```

## extra steps for mysql to work on MacOS
```
brew install mysql-connector-c
brew unlink mysql-connector-c
brew install mysql
xcode-select --install (if error about clang encountered, try run)
pip install mysql-python
```

## steps to bootstap
```
virtualenv dev
. dev/bin/activate
pip install -r requirements.txt
alembic upgrade head
```
