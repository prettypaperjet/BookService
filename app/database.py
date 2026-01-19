from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

engine = create_async_engine(settings.database_url, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise





'''
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


# create the tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


#Сессия — это объект, который хранит данные в памяти и отслеживает любые необходимые изменения в данных,
# а затем использует engine для связи с базой данных.

# Мы создадим зависимость FastAPI с параметром yield, которая будет предоставлять новую сессию для каждого запроса.
# Это гарантирует использование одной сессии на каждый запрос.
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
'''