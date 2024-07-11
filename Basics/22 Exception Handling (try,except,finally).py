# Exception Handling

def square(num):
    # Exceptional Statements
    try:
        return int(num) ** 2
    except Exception as e:
        print(e)
        return 0
    finally:
        print("The Finally Statements are Executed")

print(square("asees"))
print(square(5))