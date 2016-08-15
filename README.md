# anthill-backend

Anthill connects (soon-to-be) activists based on their location and enables them to organize an event and get in touch.

<s>*This is the repo for our Django driven backend.*</s>
This repo also contains frontend stuff and should be renamed soon™.

## Setup

### Notes
 * review settings before using it in production

### Vagrant

*not recommended for production*

start vagrant
```
vagrant up --provider virtualbox
```

ssh into the vagrant box (run all other commands from inside the box)

```shell
vagrant ssh
```

create an admin user:

```
python manage.py createsuperuser
```

start django development Server
```
python manage.py runserver 0.0.0.0:8000
```

the app should be reachable at http://127.0.0.1:8000/ now.

Navigate to the `/admin` path of your app and login with the user you just created.

### Manual

#### Django Requirements

To install Django and it's requirements, simply run:

```
pip install -r requirements.txt
```


#### PostGIS Setup


PostGIS needs the following Debian packages: postgresql-x.x, postgresql-x.x-postgis, postgresql-server-dev-x.x, python-psycopg2 (x.x matching the PostgreSQL version you want to install).

So, for example:

```
apt-get install postgresql-9.4 postgresql-9.4-postgis-2.2 postgresql-server-dev-all python-psycopg2
```


#### Database Setup

After installing PostGIS, you need to create a database and enable spatial functionality. Furthermore, add an user for our app.

```
$ createdb  <db name>
$ psql <db name>
> CREATE EXTENSION postgis;
> CREATE USER anthill PASSWORD 'my_passwd';
```

You might need to change your Postgres' configuration.
In */etc/postgresql/9.4/main/pg_hba.conf*:
Change the following line

```
local   all             all                                     peer
```

to

```
local   all             all                                     md5
```


#### Finalize Setup

To fill the database with our tables, navigate to the project dir and run:

```
python manage.py migrate
```

Afterwards, you can create an admin user:

```
python manage.py createsuperuser
```

Finally, you are able to run the app. The quickest way to do so is the following:

```
python manage.py runserver
```

Please don't do this in production. Use something like *gunicorn* + *nginx* instead.

Now navigate to the `/admin` path of your app and login with the user you just created.


### OS X notes


Get Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install Postgres
```
brew install postgresql PostGIS
```

Install PIP
```
sudo easy_install pip;
```

#### To start Server:
```
brew services start postgres
```
