from zeep import Client, exceptions

try:
    client = Client('http://localhost:8000/?wsdl')
    
    print("Select The Operation")
    print("--------------------")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    print("--------------------")

    while True:
        try:
            c = int(input("Enter Your Choice (1 to 4): "))
            if c not in [1, 2, 3, 4]:
                print("Invalid choice. Please enter 1 to 4.")
                continue

            x = int(input("Enter Num 1: "))
            y = int(input("Enter Num 2: "))

            if c == 1:
                result = client.service.add(x, y)
                print(f"Result of Addition: {result}")
            elif c == 2:
                result = client.service.subtract(x, y)
                print(f"Result of Subtraction: {result}")
            elif c == 3:
                result = client.service.multiply(x, y)
                print(f"Result of Multiplication: {result}")
            elif c == 4:
                try:
                    result = client.service.divide(x, y)
                    print(f"Result of Division: {result}")
                except ValueError as e:
                    print(f"Error: {e}")

        except ValueError:
            print("Invalid input. Please enter valid integers.")

except exceptions.TransportError as e:
    print(f"TransportError: {e}")
except exceptions.Fault as e:
    print(f"SOAP Fault: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
