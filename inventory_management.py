import json

class Product:
   # Represents a product in the inventory with attributes: id, name, price and quantity

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryManagementSystem:

    # Manages the inventory of products.
    def __init__(self, file_path):
        self.file_path = file_path
        self.inventory = self.load_inventory()

    def load_inventory(self):
        
        # Loads the inventory data from the JSON file and returns a list of product objects representing the inventory.
        try:
            with open(self.file_path, 'r') as file:
                return [Product(**product_data) for product_data in json.load(file)]
        except FileNotFoundError:
            return []

    def save_inventory(self):

        # Saves the current inventory data to the JSON file.
        with open(self.file_path, 'w') as file:
            json.dump([vars(product) for product in self.inventory], file, indent=4)

    def add_product(self, id, name, price, quantity):

        # Adds a new product to the inventory.
        product = Product(id, name, price, quantity)
        self.inventory.append(product)
        print(f"Added product: {product.name}")

    def update_product(self, id, name=None, price=None, quantity=None):
        # Updates the information of an existing product in the inventory.

        for product in self.inventory:
            if product.id == id:
                if name is not None:
                    product.name = name
                if price is not None:
                    product.price = price
                if quantity is not None:
                    product.quantity = quantity
                print(f"Updated product: {product.name}")
                return
        print(f"Product with ID {id} not found.")

    def delete_product(self, id):
 
        # Deletes a product from the inventory.
        for i, product in enumerate(self.inventory):
            if product.id == id:
                deleted_product = self.inventory.pop(i)
                print(f"Deleted product: {deleted_product.name}")
                return
        print(f"Product with ID {id} not found.")

    def view_product(self, id):

        # Displays the details of a specific product in the inventory.
        for product in self.inventory:
            if product.id == id:
                print(f"Product ID: {product.id}")
                print(f"Name: {product.name}")
                print(f"Price: {product.price}")
                print(f"Quantity: {product.quantity}")
                return
        print(f"Product with ID {id} not found.")

    def list_all_products(self):

        # Displays a list of all products in the inventory.
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("All Products:")
            for product in self.inventory:
                print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def get_low_stock_products(self, threshold):
      
        # Retrieves a list of products with stock below a given threshold.
        low_stock_products = [product for product in self.inventory if product.quantity < threshold]
        return low_stock_products

    def get_total_inventory_value(self):
     
        # Calculates the total value of the inventory.
        total_value = sum(product.price * product.quantity for product in self.inventory)
        return total_value

def main():
    
    # The main function that runs the Inventory Management System.
    inventory_system = InventoryManagementSystem('inventory.json')

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Product")
        print("5. List All Products")
        print("6. Low-Stock Alert")
        print("7. Total Inventory Value")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            inventory_system.add_product(id, name, price, quantity)
        elif choice == '2':
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = input("Enter product quantity: ")
            inventory_system.update_product(id, name, float(price), int(quantity))
        elif choice == '3':
            id = input("Enter product ID: ")
            inventory_system.delete_product(id)
        elif choice == '4':
            id = input("Enter product ID: ")
            inventory_system.view_product(id)
        elif choice == '5':
            inventory_system.list_all_products()
        elif choice == '6':
            threshold = int(input("Enter low-stock threshold: "))
            low_stock_products = inventory_system.get_low_stock_products(threshold)
            if low_stock_products:
                print("Low-stock products:")
                for product in low_stock_products:
                    print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}")
            else:
                print("No products below the low-stock threshold.")
        elif choice == '7':
            total_value = inventory_system.get_total_inventory_value()
            print(f"Total inventory value: ${total_value:.2f}")
        elif choice == '8':
            inventory_system.save_inventory()
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()