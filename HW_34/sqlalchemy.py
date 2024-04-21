from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql+mysqlconnector://root:test1234@localhost/it_step')

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    profile = relationship("Profile", uselist=False, back_populates="user")


class Profile(Base):
    __tablename__ = 'Profile'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    bio = Column(Text)
    profile_picture = Column(String(255))
    user = relationship("User", back_populates="profile")


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


user_data = [
    User(username="user1", email="user1@example.com"),
    User(username="user2", email="user2@example.com"),
    User(username="user3", email="user3@example.com"),
    User(username="user4", email="user4@example.com"),
    User(username="user5", email="user5@example.com")
]

session.add_all(user_data)


session.commit()

profile_data = [
    Profile(user_id=1, bio="Bio of user1", profile_picture="profile_picture1.jpg"),
    Profile(user_id=2, bio="Bio of user2", profile_picture="profile_picture2.jpg"),
    Profile(user_id=3, bio="Bio of user3", profile_picture="profile_picture3.jpg"),
    Profile(user_id=4, bio="Bio of user4", profile_picture="profile_picture4.jpg"),
    Profile(user_id=5, bio="Bio of user5", profile_picture="profile_picture5.jpg")
]

session.add_all(profile_data)

session.commit()
session.close()
