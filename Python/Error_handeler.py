# Error_handeler.py

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        result = None
    except Exception as e:
        print(f"Unexpected error: {e}")
        result = None
    else:
        print("Division successful.")
    finally:
        print("Execution completed.")
    return result

# Example usage
if __name__ == "__main__":
    print(divide(10, 2))   # Should print 5.0
    print(divide(10, 0))   # Should handle division by zero
    print(divide(10, "a")) # Should handle type error