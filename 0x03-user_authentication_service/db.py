#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
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
        """Adds a new user to the database

        Args:
            email(str): the user's email address
            hashed_password(str): the user's hashed_password

        Return:
            User: the newly created User object
        """
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments

        Args:
            **kwargs: Arbitrary keyword arguments to filter the query

        Return:
            the first user found matching the criteria

        Raises:
            NoResultFound: if no user matching the query is found
            InvalidRequestError: if invalid query arguments are passed
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()

            if user is None:
                raise NoResultFound
            return user
        except InvalidRequestError:
            self._session.rollback()
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes in the database.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments representing
            user attributes to update.

        Raises:
            ValueError: If an invalid attribute is passed.
            NoResultFound: If no user is found with the given ID.
        """
        try:
            user = self.find_user_by(id=user_id)

            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"Invalid user attribute: {key}")
            self._session.commit()
        except NoResultFound:
            raise
