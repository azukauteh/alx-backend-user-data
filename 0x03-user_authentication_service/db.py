#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy.orm.exc import NoResultFound
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
    """
    Add a new user to the database.

    Args:
        email (str): The email of the user.
        hashed_password (str): The hashed password of the user.

    Returns:
        User: The User object representing the newly added user.
    """
    """ Create a new User object"""
    new_user = User(email=email, hashed_password=hashed_password)

    try:
        """ Add the new user to the session and commit the changes"""
        self._session.add(new_user)
        self._session.commit()
    except IntegrityError as e:
        """ Handle integrity errors (e.g., duplicate email)"""
        self._session.rollback()
        raise ValueError("User with the same email already exists")

    """ Return the created User object"""
    return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user with given attributes.

        Args:
            **kwargs: Arbitrary keyword arguments representing the
            attributes to filter by.

        Returns:
            User: The User object found based on the input arguments.

        Raises:
            InvalidRequestError: If invalid query arguments are passed.
            NoResultFound: If no results are found based on the input
            arguments.
        """
        for key in kwargs:
            if not hasattr(User, key):
                raise InvalidRequestError("Invalid query argument: {}"
                                          .format(key))
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("No user found with  provided criteria")
            return user
        except NoResultFound:
            raise NoResultFound("No user found with the provided criteria.")

    def update_user(self, user_id: int, session_id: str) -> None:
        """Update the session ID for a user
        """
        user = self._session.query(User).filter_by(id=user_id).first()
        if user:
            user.session_id = session_id
            self._session.commit()
