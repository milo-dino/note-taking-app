from sqlmodel import create_engine

DATABASE_URL = "postgresql://postgres:postgres@host.docker.internal:5432/local"

engine = create_engine(DATABASE_URL)