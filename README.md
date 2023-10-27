# Ecommerce api created with FastAPI and deployed with Kubernetes:

This Python app is a simple but efficient containerized API with a Postgres database. It uses the recommendations of the FastAPI main documentation and best practices.

The data is CSVs files loaded during the pull process of the Postgres Docker image and SQL tables are created with 2 SQL files located in the dedicated folder. 
This data loading part is not a best practice because the sqlalchemy ORM could create tables from its models with the line: 

```models.Base.metadata.create_all(bind=engine)```

You may also use Alembic for a better migration process. Find more infos here: https://fastapi.tiangolo.com/fr/tutorial/sql-databases/

Github Actions were implemented to automatize the CICD of pushing the Docker Images on DockerHub. The Kubernetes part is done by hand. 

# Installation:

I am using a macOS env, feel free to find the equivalent commands for windows.

- Create a virtual env and make:

```pip install -r requirements.txt```

- Install Docker:

```brew install docker```

- Install Act (local run of Github actions)

'''brew install act'''


# Environment variables

Don't forget to create your own .env file with the database credentials and your Dockerhub secrets.
This file is used in both Dockerfile and CICD and ** must not be ** commited with your code.

You must define: 

[Postgres] (same as in the Dockerfile)
- POSTGRES_USER =  'postgres'
- POSTGRES_PASSWORD =  'postgres'
- POSTGRES_DB =  'default_database'
- POSTGRES_HOSTNAME = 'localhost'
- DATABASE_PORT = '5432'

[Act]
- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN
- DOCKERHUB_REPOSITORY_NAME

# Github Actions & Act 

Use the following command to test locally the CICD with your secrets: 

'''act –secret-file .env'''

Else add your dockerhub secrets directly in you Github repository.

# Launch FastAPI application locally without Docker:

- To launch the app locally with uvicorn make:

```python api.py```

# Launch FastAPI application with Docker:

- To launch the app through Docker make:

```docker compose down```
```docker volume rm ecommerce-app-with-kubernetes_psqldata```
```docker compose up --build```

Open the application with the following url: https://localhost:8000
![alt text](https://github.com/NicolasFradin/Ecommerce-app-with-Kubernetes/blob/master/api-screenshot.png)

# Remaining steps: 

- Asynchronous requests 
- Alembic migration tool
- Frontend app 
- Unit tests 

# Found my detailled process through my Medium articles here:

https://medium.com/@fradin.nicolas/


