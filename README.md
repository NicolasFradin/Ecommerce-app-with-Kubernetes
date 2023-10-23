# Ecommerce api created with FastAPI and deployed with Kubernetes:
This Python app is a simple but efficient containerized API with a Postgres database. It uses the recommendations of the FastAPI main documentation and best practices.

The data is CSVs files loaded during the pull process of the Postgres Docker image and SQL tables are created with 2 SQL files located in the dedicated folder. 
This data loading part is not a best practice because the sqlalchemy ORM could create tables from its models with the line: 

```models.Base.metadata.create_all(bind=engine)```

You may also use Alembic for a better migration process. Find more infos here: https://fastapi.tiangolo.com/fr/tutorial/sql-databases/

# Installation:

- Create a virtual env and make:

```pip install -r requirements.txt```

- Install Docker:

```brew install docker```

# Environment
Don't forget to create your own .env file with the database credentials and your Dockerhub secrets.

# Launch FastAPI application locally without Docker:
- To launch the app locally with uvicorn make:

```python api.py```

# Launch FastAPI application with Docker:
- To launch the app through Docker make:

```docker compose down```
```docker volume rm ecommerce-app-with-kubernetes_psqldata```
```docker compose up --build```


![alt text](https://github.com/NicolasFradin/Ecommerce-app-with-Kubernetes/blob/master/api-screenshot.png)

# Remaining steps: 
- Asynchronous requests 
- Alembic use
- Frontend app 
- Unit tests 

# Found my detailled process through my Medium articles here:

https://medium.com/@fradin.nicolas/


