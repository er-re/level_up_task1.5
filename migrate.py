from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy import and_

from entity_class import Offer, Product


class Migrate:
    def __init__(self, engine, chunk_size):
        self.engine = engine
        self.chunk_size = chunk_size
        self.update_premium()
        self.update()

    def update_premium(self):
        """Updating the premium sources at once step. They don't require further processing"""
        query = """UPDATE offer
        set "order" = 0
        where source_id in (SELECT id from source WHERE premium = 'true');"""
        with self.engine.connect() as con:
            statement = text(query)
            con.execute(statement)

    def fetch_product(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for product in session.query(Product).filter(Product.has_migrated == False).yield_per(1):
            yield product

    def fetch_offer(self, product_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for offer in session.query(Offer).filter(and_(Offer.order.is_(None), Offer.product_id == product_id)).order_by(Offer.date_time.asc()).yield_per(self.chunk_size):
            yield offer

    def update(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for product in self.fetch_product():
            order_count = 1
            for offer in self.fetch_offer(product.id):
                offer.order = order_count
                order_count += 1
                session.query(Offer).filter(Offer.id == offer.id).update({'order': offer.order})

            session.query(Product).filter(Product.id == product.id).update({'has_migrated': True})
            try:
                session.commit()
            except:
                session.rollback()


if __name__ == '__main__':
    from engine import Engine
    Migrate(Engine.engine, 10)