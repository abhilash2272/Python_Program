# You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
# 1.Add a product to the cart.
# 2.Remove a product from the cart 
# 3.Search for a product in the cart 
# 4.Display all products in the cart
# 5.Show the total number of products in the cart
# Cart Operations:
# 1. Add Product
# 2. Remove Product
# 3. Search Product
# 4. Display Cart
# 5. Count Products
# 6. Exit
# Enter choice: 1
# Enter product to add: Laptop
# Product 'Laptop' added to cart. 
# Enter choice: 1
# Enter product to add: Phone
# Product 'Phone' added to cart. 
# Enter choice: 4
# Cart: ['Laptop', 'Phone']
# Enter choice: 3
# Enter product to search: Phone
# Yes, 'Phone' is in the cart.
# Enter choice: 5
# Total products in cart: 2
# E-commerce Cart Program
def ecomm():
    cart = [] 
    while True:
        print("\nCart Operations:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Product")
        print("4. Display Cart")
        print("5. Count Products")
        print("6. Sort Cart")
        print("5. Clear Cart")
        print("8. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            product = input("Enter product to add: ")
            cart.append(product)
            print(f"Product '{product}' added to cart.")
        elif choice == 2:
            product = input("Enter product to remove: ")
            if product in cart:
                cart.remove(product)
                print(f"Product '{product}' removed from cart.")
            else:
                print(f"Product '{product}' not found in cart.")
        elif choice == 3:
            product = input("Enter product to search: ")
            if product in cart:
                print(f"Yes, '{product}' is in the cart.")
            else:
                print(f"No, '{product}' is not in the cart.")
        elif choice == 4:
            print("Cart:", cart if cart else "Cart is empty.")
        elif choice == 5:
            print("Total products in cart:", len(cart))
        elif choice == 6:
            print(cart.sort())
        elif choice==7:
            cart.clear()
        elif choice == 8:
            print("Exiting... Thank you for shopping!")
            break
        
        else:
            print("Invalid choice! Please try again.")
ecomm()



        
        
