def mathTableGenerator(number):
    
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")
    print("\n")

print("--- Welcome to mathTableGenerator ---")
while True:
    user_input = input("Enter a number ('quit' to exit): ").strip()
    if user_input == "quit":
        break

    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        print("\n")
        continue

    mathTableGenerator(user_input)