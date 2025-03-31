def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"Final price after discount: {final_price:.2f}")

# File Read & Write Challenge
def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()  # Example modification
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print("File modification successful.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read or write to file.")

# Error Handling Lab
filename = input("Enter the filename to read: ")
out_filename = "modified_" + filename
modify_file(filename, out_filename)
