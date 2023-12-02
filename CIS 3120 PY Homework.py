def introduction():
  
    print("Welcome to the Average Comparison Program!")
    print("This program takes three integer values, calculates their average,")
    print("and compares each value to the average.")
    print("To end the program, enter a special combination of three values.")
    print("Created by: Ella Mahalia Simeon")

#Using the def function to caluclate the average of three numbers
def findaverage(num1, num2, num3):
    
    average = (num1 + num2 + num3) / 3
    return average

#Function to compare each number to the average and print the results 
def comparetoavg(num1, num2, num3, avg):
    
    equal_count = 0

    #Compare num1 to the average and so on 
    if num1 == avg:
        print(f"{num1} is equal to the average.")
        equal_count += 1
    elif num1 < avg:
        print(f"{num1} is below the average.")
    else:
        print(f"{num1} is above the average.")
    
    if num2 == avg:
        print(f"{num2} is equal to the average.")
        equal_count += 1
    elif num2 < avg:
        print(f"{num2} is below the average.")
    else:
        print(f"{num2} is above the average.")
    
    if num3 == avg:
        print(f"{num3} is equal to the average.")
        equal_count += 1
    elif num3 < avg:
        print(f"{num3} is below the average.")
    else:
        print(f"{num3} is above the average.")
    
    print(f"{equal_count} parameter(s) is/are equal to the average.")

#Main function to run the program
def main():
    introduction()
    
    sets_processed = 0
    
    while True:
        try:
            num1 = int(input("Enter the first integer: "))
            num2 = int(input("Enter the second integer: "))
            num3 = int(input("Enter the third integer: "))
        except ValueError:
            print("Please enter valid integer values.")
            continue
        
        print(f"Numbers entered: {num1}, {num2}, {num3}")

        #Using a special combination to end the program
        if num1 == num2 == num3 == 0:
            break

        #Calculate the average of the three numbers and then comapring each number to the average 
        average = findaverage(num1, num2, num3)
        print(f"Average: {average:.3f}")
        
        comparetoavg(num1, num2, num3, average)
        
        sets_processed += 1
    
    print(f"Sets of three data values processed: {sets_processed}")

if __name__ == "__main__":
    main()
