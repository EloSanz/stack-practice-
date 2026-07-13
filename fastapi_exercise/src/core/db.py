from sqlmodel import Session, create_engine
from sqlalchemy.orm import DeclarativeBase
from src.core.config import settings

import logging

# Custom color formatter for SQLAlchemy logs in the console
class SQLColorFormatter(logging.Formatter):
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    def format(self, record):
        formatted = super().format(record)
        # Colorize core SQL queries (SELECT, INSERT, UPDATE, DELETE)
        if any(keyword in formatted for keyword in ("SELECT", "INSERT", "UPDATE", "DELETE")):
            return f"{self.CYAN}{formatted}{self.RESET}"
        else:
            return f"{self.GREEN}{formatted}{self.RESET}"

# Set up the SQLAlchemy engine logger
sql_logger = logging.getLogger("sqlalchemy.engine")
sql_logger.setLevel(logging.INFO)

# Prevent duplicate handlers and root propagation
if not sql_logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(SQLColorFormatter("%(asctime)s - %(levelname)s - %(message)s"))
    sql_logger.addHandler(handler)
    sql_logger.propagate = False

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=False)

class Base(DeclarativeBase):
    pass

# make sure all SQLModel models are imported (src.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from src.models
    # SQLModel.metadata.create_all(engine)
    pass
    # TODO: Add superuser creation once User and crud modules are implemented