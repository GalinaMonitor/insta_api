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
First you need to set login/password/proxy in
`api/management/commands/update_base.py`
	
	docker-compose run django python manage.py update_base
## Add_blogger
	docker-compose run django python manage.py add_blogger
## API
Access is available with login/password.

Go to http://0.0.0.0:8000/ to find help-response

	INFO			:	/
	User list		:	/users
	Blogger list		:	/bloggers
	Blogger_followers	:	/bloggers/<blogger_name>
	Intersections		:	/intersect/<blogger_name1>/blogger_name2>
	Get User Login		:	/getlogin/<id>
	
## TASKS:
- optimise everything!!! 
