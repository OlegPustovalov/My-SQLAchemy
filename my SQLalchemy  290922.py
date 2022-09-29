import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    
    publisher = relationship(Publisher, backref="book")
    
class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    
class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer)
    
    shop = relationship(Shop, backref="stock") #???stock дважды
    book = relationship(Book, backref="stock")
    
class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.String(length=40))
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer)
    
    stock = relationship(Stock, backref="sale")
    
def create_tables(engine):
# Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":

#     str_v = input(' Введите c если создать таблицы или s если запрос по издателю: ')
    str_v = 's'
#     str_p = input('Введите название издателя (Эксмо, Диалектика,БХВ Петербург,Microsoft Press) ->')
    str_p = 'Диалектика'

    DSN = "postgresql://postgres:postgres@localhost:5432/postgres"
    engine = sq.create_engine(DSN)
    if str_v == 'c':
        create_tables(engine)
    if str_v == 's':
# сессия
        Session = sessionmaker(bind=engine)
        session = Session()
     
        result2 = session.query(Shop,Stock,Book,Publisher).filter(Publisher.id == Book.id_publisher).filter(Book.id == Stock.id_book).filter(Stock.id_shop ==Shop.id).filter(Publisher.name == str_p)
        print (f'Книги издателя {str_p} есть в следующих магазинах:')
        for row in result2:
            print ('магазин: ',row.Shop.name,',книга: ',row.Book.title)
        
        