up:
	@echo starting django rest api server on port 8000...
	python .\api\manage.py runserver

migrate:
	@echo migrating database
	python .\api\manage.py makemigrations
	python .\api\manage.py migrate

