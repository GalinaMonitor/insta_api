# Insta_api
## Preparations
You should have Docker+Docker-compose installed. 
All commands made from insta_api folder
## First launch
	docker-compose up --build
	docker-compose run django python manage.py migrate
	docker-compose run django python manage.py makemigrations api
	docker-compose run django python manage.py migrate
	docker-compose run django python manage.py createsuperuser
## To launch/exit
	docker-compose up / down
## Postgres
	docker exec -it pgdb psql -U postgres
## Django
	docker exec -it django bash
## Update base(working too slow)
	docker-compose run django python manage.py update_base
## Add_example_bloggers
	docker-compose run django python manage.py add_bloggers
## API
Access is available with login/password. 

Go to http://0.0.0.0:8000/ to find help-response
