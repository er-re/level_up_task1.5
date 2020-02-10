from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column
from sqlalchemy.dialects.postgresql import INTEGER, BIGINT, TIMESTAMP, BOOLEAN


Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(INTEGER, primary_key=True)


class Product(Base):
    __tablename__ = 'product'
    id = Column(INTEGER, primary_key=True)
    customer_id = Column(INTEGER, ForeignKey("customer.id"))
    has_migrated = Column(BOOLEAN)


class Source(Base):
    __tablename__ = 'source'
    id = Column(INTEGER, primary_key=True)
    premium = Column(BOOLEAN)


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True)


class Offer(Base):
    __tablename__ = 'offer'
    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey("user.id"))
    product_id = Column(INTEGER, ForeignKey("product.id"))
    source_id = Column(INTEGER, ForeignKey("source.id"))
    date_time = Column(TIMESTAMP, nullable=False)
    order = Column(BIGINT)

    def __repr__(self):
        return f'Offer(id={self.id}, order={self.order})'


if __name__ == '__main__':
    from engine import Engine
    Base.metadata.create_all(Engine.engine)



