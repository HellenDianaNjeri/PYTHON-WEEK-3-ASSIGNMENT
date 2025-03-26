# Creating a function to calculate the discounted price
def calculate_discount(original_price, discount_percentage):
    final_price = original_price-(original_price*discount_percentage/100)
    return(final_price)

# Define original price and discount percentage before calling the function
original_price = 1000  
discount_percentage = 5              
final_price = original_price-(original_price*discount_percentage/100)

# Apply discount if it is 20% or higher
if discount_percentage >= 20:
    print(final_price)
else:
    print(original_price)

