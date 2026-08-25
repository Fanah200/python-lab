import sys
sys.path.append('src')
from utils import square, is_even, celsius_to_fahrenheit

def main():
    print("--- Python Lab Program ---")
    try:
        user_input = float(input("Enter a number to process: "))
        num_square = square(user_input)
        even_status = "even" if is_even(user_input) else "odd"
        fahrenheit_val = celsius_to_fahrenheit(user_input)
        
        print(f"\nResults for {user_input}:")
        print(f"1. Square of the number: {num_square}")
        print(f"2. The number is: {even_status}")
        print(f"3. Treated as Celsius to Fahrenheit: {fahrenheit_val:.2f}°F")
    except ValueError:
        print("Error: Please enter a valid numerical value.")

if __name__ == "__main__":
    main()
