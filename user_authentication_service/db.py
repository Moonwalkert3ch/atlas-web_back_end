#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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
        """Creates a new user instance and returns it
        Parameter Args:
        email(str) - email provided
        hashed_passwrd(str) - password provided
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(new_user)
        session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Finds the first row in users table and
        returns it
        Parameter Args: arbitrary kw args
        Return: firt row of users
        """
        session = self._session
        try:
            user = session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Method that updates users attributes
        Parameter Args:
        user-id(int) - userid of the user to update
        **kwargs - arbitary keyword args
        """
        user = self.find_user_by(id=user_id)

        names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in names:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)
        self._session.commit()
