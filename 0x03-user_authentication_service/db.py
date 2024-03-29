#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the data base
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
            return user
        except IntegrityError:
            self._session.rollback()
            raise ValueError("User with the same email already exists")

    def find_user_by(self, **kwargs) -> User:
        """Find a user with given attributes
        """
        for key in kwargs:
            if not hasattr(User, key):
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, session_id: str) -> None:
        """Update the session ID for a user
        """
        user = self._session.query(User).filter_by(id=user_id).first()
        if user:
            user.session_id = session_id
            self._session.commit()
