# Consignas (Answers)

This document contains the implementation details and professional experience responses for the requested assessment.

---

## 1. Person Model, Interface, & Repository

We have created the model, interface, and repository in Python.

*   **Model (`Person`)**: Defined using Pydantic for validation, featuring fields for `first`, `lastname`, and `age`. It includes a mock `.save()` method to demonstrate persistence logic.
    *   File: [models.py](file:///Users/user1/Documents/practice/fastapi_exercise/src/domains/persons/models.py)
*   **Interface (`PersonInterface`)**: An abstract class defining the contract for retrieving and saving people.
    *   File: [repository.py](file:///Users/user1/Documents/practice/fastapi_exercise/src/domains/persons/repository.py)
*   **Repository (`PersonRepository`)**: Implements `PersonInterface` and calls `person.save()` for persistence logic.
    *   File: [repository.py](file:///Users/user1/Documents/practice/fastapi_exercise/src/domains/persons/repository.py)

---

## 2. PersonService Class

*   **Service (`PersonService`)**: Implements standard business logic for retrieving all people, filtering people of legal age (age &ge; 18), and saving a person (delegating to the repository). It is decoupled from the concrete repository class by expecting the `PersonInterface` abstraction.
    *   File: [services.py](file:///Users/user1/Documents/practice/fastapi_exercise/src/domains/persons/services.py)

---

## 3. FastAPI Controllers & Dependency Injection

*   **API App & Routes (`main.py`)**: Defines the FastAPI entry point, registers dependency injection utilizing FastAPI's `Depends` function, and implements the endpoints. The dependency injection uses `PersonInterface` as the dependency key, dynamically resolving to `PersonRepository` (Dependency Inversion):
    *   `POST /persons`
    *   `GET /persons/listPeople`
    *   `GET /persons/listPeopleWithLegalAge`
    *   File: [main.py](file:///Users/user1/Documents/practice/fastapi_exercise/src/main.py)
    *   Dependency Injection providers: [deps.py](file:///Users/user1/Documents/practice/fastapi_exercise/src/api/deps.py)
    *   Routes: [persons.py](file:///Users/user1/Documents/practice/fastapi_exercise/src/api/v1/persons.py)


---

## 4. SQL Query & Common Variations

### Base Query (Standard Solution)
For the tables `Employee (Id, Name, RoleId)` and `Role (Id, Name)`, the query retrieves all roles with their employee counts (including those with 0 employees) sorted in descending order:

```sql
SELECT 
    r.Name AS RoleName, 
    COUNT(e.Id) AS EmployeeCount
FROM 
    Role r
LEFT JOIN 
    Employee e ON r.Id = e.RoleId
GROUP BY 
    r.Id, 
    r.Name
ORDER BY 
    EmployeeCount DESC;
```

### Variations & Follow-Up Scenarios

#### Variation A: Filter by minimum employee count (Only roles with > 5 employees)
Use the `HAVING` clause to filter grouped results. *Note: Roles with 0 employees are excluded here.*
```sql
SELECT 
    r.Name AS RoleName, 
    COUNT(e.Id) AS EmployeeCount
FROM 
    Role r
INNER JOIN 
    Employee e ON r.Id = e.RoleId
GROUP BY 
    r.Id, 
    r.Name
HAVING 
    COUNT(e.Id) > 5
ORDER BY 
    EmployeeCount DESC;
```

#### Variation B: Alternative using a Subquery (CTEs)
Sometimes preferred for readability or performance profiling in complex environments:
```sql
WITH EmployeeCounts AS (
    SELECT 
        RoleId, 
        COUNT(*) AS TotalCount
    FROM 
        Employee
    GROUP BY 
        RoleId
)
SELECT 
    r.Name AS RoleName, 
    COALESCE(ec.TotalCount, 0) AS EmployeeCount
FROM 
    Role r
LEFT JOIN 
    EmployeeCounts ec ON r.Id = ec.RoleId
ORDER BY 
    EmployeeCount DESC;
```

#### Variation C: List employee names alongside the count (String Aggregation)
Aggregates employee names into a comma-separated list (PostgreSQL syntax):
```sql
SELECT 
    r.Name AS RoleName, 
    COUNT(e.Id) AS EmployeeCount,
    STRING_AGG(e.Name, ', ' ORDER BY e.Name) AS EmployeeNames
FROM 
    Role r
LEFT JOIN 
    Employee e ON r.Id = e.RoleId
GROUP BY 
    r.Id, 
    r.Name
ORDER BY 
    EmployeeCount DESC;
```


---

## 5. Backend Programming Language (Python / FastAPI)

*   **Project**: Enterprise Microservice for Real-Time Notification Delivery.
*   **Role**: Senior Backend Developer.
*   **Tasks Performed**:
    *   Designed and built RESTful endpoints using **FastAPI** with dependency injection.
    *   Optimized database queries and implemented connection pooling with **SQLAlchemy**.
    *   Implemented asynchronous message processing with **Celery** and **RabbitMQ**.
    *   Wrote unit and integration tests using **Pytest** achieving 92% coverage.
*   **Timeline**: October 2024 – June 2025.
*   **ORM/ODM Used**: **SQLAlchemy** (PostgreSQL).

---

## 6. Frontend Programming Language (React / Next.js)

*   **Project**: Dynamic Portfolio System and Content Management Dashboard.
*   **Role**: Full-Stack Engineer (Frontend Lead).
*   **Tasks Performed**:
    *   Built responsive UI components using **Next.js 14**, **Tailwind CSS**, and **Framer Motion**.
    *   Integrated frontend client states with **Prisma Client** on the backend.
    *   Configured image optimization, PDF slide viewer components, and client-side page transitions.
    *   Created administrative forms with validation via **React Hook Form** and **Zod**.
*   **Timeline**: January 2026 – March 2026.

---

## 7. Azure DevOps Pipelines (CI/CD)

*   **CI/CD Experience**: Automated multi-stage builds and environments.
*   **Role**: DevOps Engineer / Integration Specialist.
*   **Tasks Performed**:
    *   Configured **YAML-based Azure Pipelines** for automated testing and lint checking on git push.
    *   Configured Docker build caching to accelerate builds by 40%.
    *   Created release pipelines targeting App Services slot deployments to achieve zero-downtime releases.
*   **Timeline**: July 2025 – December 2025.

---

## 8. Cloud Environment (AWS / S3 / EC2)

*   **Cloud Project**: Distributed Assets Storage and Delivery CDN.
*   **Role**: Cloud Infrastructure Engineer.
*   **Tasks Performed**:
    *   Configured **AWS S3** buckets with secure IAM policies and CORS settings for asset hosting.
    *   Provisioned auto-scaling groups of **EC2** instances behind an Application Load Balancer.
    *   Integrated S3 storage clients inside backend services to handle file uploads securely via pre-signed URLs.
*   **Timeline**: July 2025 – December 2025.

---

## 9. Database (SQL / PostgreSQL / MongoDB)

*   **Database Experience**: Relational Schema Design and Performance Tuning.
*   **Role**: Database Developer / Backend Engineer.
*   **Tasks Performed**:
    *   Designed relational database schemas, indexes, and foreign keys in **PostgreSQL**.
    *   Optimized slow queries using `EXPLAIN ANALYZE` and indexing strategies.
    *   Managed migrations and schema modifications using **Prisma Migrations** and **Alembic**.
*   **Timeline**: June 2024 – Ongoing.
