up:
	@echo starting django rest api server on port 8000...
	python .\api\manage.py runserver

migrate:
	@echo migrating database
	python .\api\manage.py makemigrations
	python .\api\manage.py migrate


## up: starts all containers in the background without forcing build
docker-up:
	@echo Starting Docker images...
	docker-compose up -d
	@echo Docker images started!

## up_build: stops docker-compose (if running), builds all projects and starts docker compose
docker-up_build:
	@echo Stopping docker images (if running...)
	docker-compose down
	@echo Building (when required) and starting docker images...
	docker-compose up --build -d
	@echo Docker images built and started!

