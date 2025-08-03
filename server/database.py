# Importing create_engine to establish the connection to the database.
from sqlalchemy import create_engine

# Importing declarative_base to create the base class for ORM models.
from sqlalchemy.ext.declarative import declarative_base

# Importing sessionmaker to create a session factory for database interactions.
from sqlalchemy.orm import sessionmaker

# Importing a hidden module 
import hidden

# Creating a database engine using the URL from the hidden module.
# 'check_same_thread=False' is required for SQLite when using multiple threads.
engine = create_engine(hidden.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Creating a session factory bound to the engine.
# autocommit=False: changes won't be auto committed to the DB.
# autoflush=False: prevents automatic flush to the DB before queries.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Creating a base class for all ORM models (tables will inherit from this).
Base = declarative_base()

# Dependency function to get a DB session.
# Used in FastAPI to manage sessions per request.
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to be used in the request
        yield db
    finally:
        # Close the session after the request is done
        db.close()
