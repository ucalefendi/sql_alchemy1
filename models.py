from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import declarative_base,relationship

#my base class
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)

    orders = relationship('Order',back_populates='customer')


    def __repr__(self):
        return f"Customer( id={self.id},name={self.name},email={self.email})"
    

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    order_items = relationship('OrderItem',back_populates='product')

    def __repr__(self):
        return f"Product(id={self.id},name={self.name},price={self.price},stock_quantity={self.stock})"
    

class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer,primary_key=True)
    customer_id = Column(Integer,ForeignKey('customers.id'))
    total_amount = Column(Float)


    customer = relationship('Customer',back_populates='orders')
    order_items = relationship('OrderItem',back_populates='order')

    def __repr__(self):
        return f"Order( id={self.id},customer_id={self.customer_id},total_amount={self.total_amount})"
    


class OrderItem(Base):

    __tablename__ = 'orderitems'

    id = Column(Integer,primary_key=True)
    order_id = Column(Integer,ForeignKey('orders.id'))
    product_id = Column(Integer,ForeignKey('products.id'))
    quantity = Column(Integer)

    order = relationship('Order',back_populates='order_items')
    product = relationship('Product',back_populates='order_items')

    def __repr__(self):
        return f"OrderItem( id={self.id},order_id={self.order_id},product_idt={self.product_id},quantitiy={self.quantity})"
    



    





