# black-mesa-db-demos

Code samples demonstrating database access patterns in Python and C#/.NET, using a PostgreSQL database running in Docker.

> [!NOTE]
> These demos assume you have the Docker database environment from CSCI 2020 already running.
> If not, follow the setup instructions at https://github.com/rochellew/csci_2020_docker_setup before continuing.

## What's in here

### Python (`/python`)

Three scripts showing progressively higher levels of abstraction:

| File | Approach |
|---|---|
| `raw_psycopg2.py` | Raw SQL using the psycopg2 driver directly |
| `sqlalchemy_core.py` | SQLAlchemy Core — still writes SQL, but uses the SQLAlchemy engine |
| `sqlalchemy_orm.py` | SQLAlchemy ORM — maps tables to Python classes, no SQL written |

### C#/.NET (`/EFDemos`)

Three projects in the `EFDemos` solution showing Entity Framework Core with different configuration styles:

| Project | Approach |
|---|---|
| `FluentAPI` | EF Core configured via method chaining in `OnModelCreating` |
| `Annotations` | EF Core configured via data annotation attributes on model classes |
| `AnnotationsSpectre` | Same as Annotations, with styled console output via Spectre.Console |

## ORM vs. non-ORM

The raw psycopg2 and SQLAlchemy Core scripts write SQL directly as strings. Rows come back as tuples and you access data by index (`row[0]`, `row[1]`).

The SQLAlchemy ORM and Entity Framework scripts map database tables to classes. Rows come back as objects with named properties (`emp.last_name`, `emp.first_name`). The ORM generates the SQL for you — you never write a SELECT statement.

The tradeoff: raw drivers keep SQL visible and explicit, which is useful for learning. ORMs reduce boilerplate for common operations but add an abstraction layer that can obscure what's actually happening against the database.

## Running the Python scripts

### Prerequisites
- Python 3.10+
- Docker database environment running (see note above)

### Setup

> [!NOTE]
> Run the commands in your command prompt in terminal or VS Code.
> You may not need  to run the `cd python` command if you're already in the `/python` directory.

```bash
cd python
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Run

Run with the IDE or by typing the command below that corresponds to the Python file you want to run.

```bash
python raw_psycopg2.py
python sqlalchemy_core.py
python sqlalchemy_orm.py
```

> [!NOTE]
> All three scripts connect to `localhost:5432`, database `coursedb`, with username `student` and password `password123`. These match the defaults from the Docker setup repo.

## Running the C# projects

### Prerequisites
- .NET 8 SDK or later
- Docker database environment running (see note above)

### Run

> [!NOTE]
> You can run these projects by opening the solution file in Visual Studio, Rider, or VS Code and clicking the 'play' button.
> You will need to change the startup project if you choose to do this. 

If you would rather run this from the terminal, see below. 

From the `EFDemos` directory:

```bash
dotnet run --project FluentAPI
dotnet run --project Annotations
dotnet run --project AnnotationsSpectre
```

> [!IMPORTANT]
> NuGet packages restore automatically on first run — no separate install step needed.

> [!NOTE]
> Connection details are hardcoded in `BlackMesaContext.cs` in each project. They match the Docker setup defaults. If your environment uses different credentials, update the connection string there.

## Fluent API vs. Data Annotations

Both `FluentAPI` and `Annotations` produce identical output — the difference is only in how the database mapping is configured.

Fluent API puts all configuration in `OnModelCreating` in the `DbContext`:

```csharp
entity.Property(e => e.FirstName).HasColumnName("first_name");
```

Data annotations put configuration directly on the model class properties:

```csharp
[Column("first_name")]
public string FirstName { get; set; } = null!;
```

Annotations are more readable for simple mappings since the configuration lives next to the property it describes. Fluent API is more powerful for complex scenarios and keeps model classes clean.
