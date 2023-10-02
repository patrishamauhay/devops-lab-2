num = int(input("Enter list of numbers"))

numbers = [float(num) for num in numbers]

if len(numbers) == 0:
    print("No numbers provided")
else:
    avg=sum(numbers)/len(numbers)
    print("Average is: {average:.2f}")

    # Ritika changes
    largest = max(num)
    smallest = min(num)
    print(f"Largest Number: (largest)")
    print(f"Smallest Number: (smallest)")

    
    #We had completed the average numbers.