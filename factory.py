import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from random import randint

from entity_class import Customer, Product, Source, User, Offer


class Factory:
    def __init__(self, engine, **count_kwargs):
        self.engine = engine
        self.__dict__.update(count_kwargs)

    def fill_customer(self):
        df = pd.DataFrame(range(self.customer), columns=['id'])
        df.to_sql(Customer.__tablename__, self.engine, if_exists='append', index=False)

    def fill_product(self):
        df = pd.DataFrame({'id': range(self.product), 'customer_id': np.random.randint(0, self.customer, size=(1, self.product))[0]})
        df.to_sql(Product.__tablename__, self.engine, if_exists='append', index=False)

    def fill_source(self):
        df = pd.DataFrame({'id': range(self.source), 'premium': np.random.randint(0, 2, size=(1, self.source))[0]})
        df['premium'] = df['premium'].map(bool)
        df.to_sql(Source.__tablename__, self.engine, if_exists='append', index=False)

    def fill_user(self):
        df = pd.DataFrame(range(self.user), columns=['id'])
        df.to_sql(User.__tablename__, self.engine, if_exists='append', index=False)

    def fill_offer(self):
        df = pd.DataFrame({
            'id': range(self.offer),
            'user_id': np.random.randint(0, self.user, size=(1, self.offer))[0],
            'product_id': np.random.randint(0, self.product, size=(1, self.offer))[0],
            'source_id': np.random.randint(0, self.source, size=(1, self.offer))[0],
            'date_time': [datetime(2016, 1, 1) + timedelta(days=randint(1, 100),
                                                           hours=randint(1, 100),
                                                           minutes=randint(1, 100))
                          for _ in range(self.offer)]
        })
        df.to_sql(Offer.__tablename__, self.engine, if_exists='append', index=False)

    def fill(self):
        self.fill_customer()
        self.fill_product()
        self.fill_source()
        self.fill_user()
        self.fill_offer()


if __name__ == '__main__':
    from engine import Engine
    sample_count = {'customer': 10, 'product': 20, 'source': 5, 'user': 70, 'offer': 400}
    factory = Factory(Engine.engine, **sample_count)
    factory.fill()
