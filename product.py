class product:
    inventory=[]
    product_id_counter=0
    order_id_counter=0
    def __init__(self,product_id, name, category, quantity, price, supplier): # initialize product attributes
        self.name=name
        self.price=price
        self.quantity=quantity
        self.product_id = product_id
        self.category=category
        self.supplier=supplier
     

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier): # add new product to inventory
        cls.product_id_counter += 1 # Increment product ID counter
        new_product = product(cls.product_id_counter, name, category, quantity, price, supplier) # Create new product instance
        cls.inventory.append(new_product) # Add to inventory list
        print(f"Product '{name}' added with ID {new_product.product_id}.")
        return "Product added successfully."

    @classmethod
    def view_products(cls):# view all products in inventory
        if not cls.inventory: # Check if inventory is empty
            print("No products in inventory.") 
            return
        print("\n--- PRODUCT LIST ---")
        for prod in cls.inventory: # Iterate through inventory and print details
            print(f"ID: {prod.product_id} | Name: {prod.name} | Category: {prod.category} | Quantity: {prod.quantity} | Price: {prod.price} | Supplier: {prod.supplier}") # Print product details
        print("---------------------\n")
    
    @classmethod
    def delete_product(cls): # delete product from inventory
        prod_id = int(input("Enter product ID to delete: ")) # Get product ID from user
        for prod in cls.inventory: # Iterate through inventory
            if prod.product_id == prod_id: # Find product by ID
                cls.inventory.remove(prod) # Remove product from inventory
                print(f"Product ID {prod_id} deleted.")
                return "Product deleted successfully."
        print("Product not found.")
        return "Deletion failed."

    @classmethod
    def update_product(cls): # update product quantity in inventory
        prod_id = int(input("Enter product ID to update: ")) # Get product ID from user
        for prod in cls.inventory: # Iterate through inventory
            if prod.product_id == prod_id: # Find product by ID
                new_quantity = int(input(f"Enter new quantity for '{prod.name}': ")) # Get new quantity from user
                prod.quantity = new_quantity # Update product quantity
                print(f"Product ID {prod_id} quantity updated to {new_quantity}.")
                return "Product updated successfully."
        print("Product not found.")
        return "Update failed."
    
    @classmethod
    def place_order(cls): # place order for a product
        cls.order_id_counter += 1 # Increment order ID counter
        prod_id=int(input("Enter product ID to order: ")) # Get product ID from user
        for prod in cls.inventory: # Iterate through inventory
            if prod.product_id==prod_id: # Find product by ID
                order_quanity=int(input("Enter order quantity: ")) # Get order quantity from user
                if order_quanity>prod.quantity: # Check if sufficient stock is available
                    print("Insufficient stock!") 
                    return "Order failed." # Return if not enough stock
                customer_name=input("Enter customer name: ")# Get customer name from user

                return f"Order placed for {order_quanity} of '{prod.name}' by {customer_name}. and order id is {cls.order_id_counter} and the product id is {prod_id}"
            

p1=product.add_product("PC","Electronics",10,1000,"Supplier A")
print(p1)
p2=product.add_product("Laptop","Electronics",5,1500,"Supplier B")
print(p2)

p1=product.view_products()
print(p1)
p1=product.update_product()
print(p1)
p1=product.delete_product()
print(p1)

p1=product.place_order()
print(p1)

p1=product.view_products()
print(p1)
