# NGRT - ***NetGuru Recruitment Task***

Simple REST API for Cars models implemented in **Django** and **DRF**
<br />Cars and models validation based on external **API**: https://vpic.nhtsa.dot.gov/api/

### Before run app

Create the `.env` file in **main** folder with content

```buildoutcfg
# Django config
SECRET_KEY=your_secret_key
DEBUG=False  #if you wont DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0

# Postgres config
DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_PORT=5432

# External API config
API_URL=https://vpic.nhtsa.dot.gov/api/
```

After making the `.env` file run ***docker-compose*** commands

`docker-compose build`

`docker-compose run api python manage.py migrate`

Create ***Super User*** if you want:

`docker-compose run api python manage.py createsuperuser`

### Run App using ***docker-compose*** 

`docker-compose up -d`