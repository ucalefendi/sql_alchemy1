from crud import create_customer,create_product,create_order,get_customers,get_products,get_orders,update_product_price,delete_customer


def make_customer():
    name = input('enter customer name:')
    email = input('Enter customer email:')
    create_customer(name,email)
    print(f"Customer {name} created!")



def make_product():
    name = input('enter product name:')    
    price = float(input('enter product price:'))    
    stock = int(input('enter product stock:'))   
    create_product(name,price,stock) 
    print(f"Product {name} added!")




def make_order():
    customer_id = int(input('enter customer id:'))
    product_quantities = {}

    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {product_name}:"))
        product_quantities[product_name] = quantity

    try:
        create_order(customer_id,product_quantities) 
        print(f"Order created ID {customer_id}")   
    except Exception as e:
        print(f"Failed to create order: {e}")



#main function
def main():
    while True:
        print("Store managment system") 
        print("1.Create customer")       
        print("2.Create product")       
        print("3.Create order")       
        print("4.View customers")       
        print("5.View products")    
        print("6.Viev orders")   
        print("7.Update product price")   
        print("8.Delete customer")
        print("9.Exit")

        option = input('Select an option (1-9): ')
        if option == "1":
            make_customer()
        elif option == "2":
            make_product()
        elif option == "3":
            make_order()
        elif option == "4":
            print("Customers",get_customers())
        elif option == "5":
            print("Products",get_products())
        elif option == "6":
            print("Orders",get_orders())
        elif option == "7":
            product_id = int(input("Enter id to update price: "))
            new_price = float(input("Enter new price: "))
            update_product_price(product_id,new_price)
            print("new price updated")
        elif option == "8":
            customer_id = int(input("Enter customer id to delete: "))
            delete_customer(customer_id)
            print("Customer deleted")
        elif option == "9":
            print("exiting application ")
            break
        else:
            print("invalid choise ,Try again!")


if __name__ == '__main__':
    main()            
