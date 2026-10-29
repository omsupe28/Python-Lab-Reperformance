def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result is: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers only.")
    except ValueError:
        print("Error: Invalid input value. Please enter a valid number.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Error: Invalid input!"


def find_index(lst, elem):
    try:
        return lst.index(elem)
    except ValueError:
        return "Error: Element not found!"


def main():
    print("Test 1: Valid inputs (10, 2)")
    divide_numbers(10, 2)

    print("\nTest 2: Division by zero (10, 0)")
    divide_numbers(10, 0)

    print("\nTest 3: Invalid input types ('ten', 2)")
    divide_numbers("ten", 2)

    print("\nTest 4: Invalid denominator (10, 'two') - TypeError")
    divide_numbers(10, "two")

    print("\nTest 5: Missing denominator (10, None) - TypeError")
    divide_numbers(10, None)

    print("\nTest 6: Integer conversion - handling a real ValueError")
    print("convert_to_int('25'):", convert_to_int("25"))
    print("convert_to_int('two'):", convert_to_int("two"))

    print("\nTest 7: List search - handling a real ValueError")
    print("find_index([10, 20, 30], 20):", find_index([10, 20, 30], 20))
    print("find_index([10, 20, 30], 99):", find_index([10, 20, 30], 99))


if __name__ == "__main__":
    main()
