from sqlmodel import SQLModel, create_engine, Session

# Conexión local a la base de datos SQLite
DATABASE_URL = "sqlite:///./base_datos.db"

engine = create_engine(DATABASE_URL, echo=False)

def get_db():
    with Session(engine) as session:
        yield session
