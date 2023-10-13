# Service Layer – Business Logic

Implementing FastAPI Services for a more maintainable codebase – Abstraction and Separation of Concerns

Service layer acts as an intermediate layer between the API layer and database layer. 
The logic and mapping is done within the service layer to prepare the request as such that it cannot fire a query against the database directly but sends the processed data to the DB layer instead.
