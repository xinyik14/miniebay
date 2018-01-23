#!/bin/sh

pip install -r requirements.txt
cd miniebay
python setup.py install
cd ../
alembic upgrade head
docker exec -it miniebay-mysql mysql -uroot -ptest -e "use miniebay; insert into users (username, password) values ('test@gmail.com', 'test')"
cd miniebay/miniebay/
FLASK_APP=app.py flask run
