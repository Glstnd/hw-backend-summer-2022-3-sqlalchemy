from typing import Optional, TYPE_CHECKING, Any

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from app.store.database import db

if TYPE_CHECKING:
    from app.web.app import Application


class Database:
    def __init__(self, app: "Application"):
        self.app = app

        self._engine: Optional[AsyncEngine] = None
        self._db: Optional[declarative_base] = None
        self.session: Optional[async_sessionmaker[AsyncSession]] = None

    async def connect(self, *_: Any, **__: Any) -> None:
        self._db = db

        self._engine = create_async_engine(
            URL.create(
                drivername="postgresql+asyncpg",
                host=self.app.config.database.host,
                database=self.app.config.database.database,
                username=self.app.config.database.user,
                password=self.app.config.database.password,
                port=self.app.config.database.port,
            ),
        )
        self.session = async_sessionmaker(
            self._engine,
            expire_on_commit=False,
            autoflush=True,
            class_=AsyncSession
        )

    async def disconnect(self, *_: Any, **__: Any) -> None:
        try:
            await self._engine.dispose()
        except:
            pass
