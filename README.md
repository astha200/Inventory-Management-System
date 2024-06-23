# Inventory-Management-System
Inventory Management System Program in Python 


This program is a simple Inventory Management System implemented in Python. It allows users to add, update, delete, view, and list products in an inventory. Users can also generate low-stock alerts and calculate the total value of the inventory.

## How to Run the Program
1. Make sure you have Python3 installed on your system.
2. Download the 'inventory_management.py' file to your local machine.
3. Open a terminal or command prompt and navigate to the directory where the 'inventory_management.py' file is located.
4. Run the program by executing the following command:
python inventory_management.py
5. The program will present a menu with various options. Choose the desired operation by entering the corresponding number.
6. Follow the prompts to perform the selected operation.
7. When you're done, choose the "Exit" option to save the inventory data and exit the program.

## Assumptions and Design Choices
- Each product is represented by a 'Product' class with attributes such as ID, name, price, and quantity.
- The 'InventoryManagementSystem' class is responsible for managing the inventory. It provides methods for adding, updating, deleting, and viewing products, as well as generating reports and handling data persistence.
- The inventory data is stored in a JSON file named 'inventory.json'. This file is loaded at the start of the program and saved when the program exits.
- User input is taken through the command line interface with a menu-driven system for easy interaction.
- The code assumes that the user will provide valid input. Error handling, such as input validation, has not been implemented to keep the code simple and focused on the core functionality.
