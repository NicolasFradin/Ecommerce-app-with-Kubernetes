from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import lru_cache
from app.config.config import get_settings

engine = create_engine(
    get_settings().POSTGRES_URL,
    echo=True,
    pool_pre_ping=True
)


@lru_cache
def create_session() -> scoped_session:

    Session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    return Session

def get_session():
    """
    We will use SQLAlchemy's scoped_session for this, like described in its documentation, and create a dependency.
    This dependency will take care of creating a session at the beginning of a web request and close it at the end.
    function that will create a new database session and close the session after the operation has ended.
    """
    Session = create_session()
    try:
        yield Session
    finally:
        Session.close()