from database import get_session
from models import Customer,Order,OrderItem,Product


def create_customer(name,email):
    session = get_session()
    new_customer = Customer(name=name,email=email)
    session.add(new_customer)
    session.commit()
    session.close()


def create_product(name,price,stock_quantity): 
    session = get_session()   
    new_product = Product(name=name,price=price,stock=stock_quantity)
    session.add(new_product)
    session.commit()
    session.close()



def create_order(customer_id,product_quantities):
    session = get_session() 
    products = {product.name:product for product in session.query(Product).all()}

    #order create here
    order = Order(customer_id=customer_id)   
    session.add(order)
    session.commit()
    

    #making order based on product names
    for product_name , quantity in product_quantities.items():
        if product_name in products:
            product = products[product_name]
            order_item = OrderItem(order_id=order.id,product_id=product.id,quantity=quantity)
            session.add(order_item)
        else:
            print(f'Product {product_name} not found!')
    session.commit()
    session.close()



def get_customers():
    session = get_session()
    customers = session.query(Customer).all()
    session.close()
    return customers


def get_products():
    session = get_session()
    products = session.query(Product).all()
    session.close()
    return products


def get_orders():
    session = get_session()
    orders = session.query(Order).all()
    session.close()
    return orders



def update_product_price(product_id,new_price):
    session = get_session()
    product = session.query(Product).filter_by(Product.id == product_id).first()
    if product:
        product.price = new_price
        session.commit()
    session.close()    



def delete_customer(customer_id,):
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        session.delete(customer)   
        session.commit()
    session.close()    
