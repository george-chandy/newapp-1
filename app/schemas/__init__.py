
from sqlalchemy import Boolean, Column, String
from src.config.database import Base




# class User(Base):
#     __tablename__ = "user"
#     id = Column('id', String(128), primary_key=True)
#     first_name = Column('first_name',String(256), nullable=False)
#     last_name = Column('last_name',String(256), nullable=False)
#     email = Column('email',String(256), nullable=False)
#     user_type = Column('user_type',Integer, nullable=False)
#     is_trial = Column('is_trial',Boolean, nullable=True)
#     is_active = Column('is_active',Boolean, nullable=False, default=False)
#     created_at = Column('created_at', TIMESTAMP, server_default=func.now())
#     identifier = Column('identifier',String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

#     def __str__(self):
#         return f"User(id={self.id}, name={self.first_name} {self.last_name}, email={self.email}, user_type={self.user_type.name}, created_at={self.created_at}, is_trial{self.is_trial})"


class ClientTable(Base):
    __tablename__ = "clients"
    id = Column('id', String(128), primary_key = True)
    client_name = Column('client_name', String(128), nullable=False)
    location = Column('location', String(128), nullable = False)
    description = Column('description', String(128), nullable=False)
    status = Column('status', Boolean, nullable=False, default=False)
    identifier = Column('identifier',String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

class UserTable(Base):
    __tablename__ = "users"
    email = Column('email',String(256), nullable=False)
    phone_no = Column('phone_no', String(128), nullable=False)
    first_name = Column('first_name',String(128),nullable=False)
    last_name = Column('last_name',String(128),nullable=False)
    user_name = Column('user_name',String(128),nullable=False)
    identifier = Column('identifier',String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

