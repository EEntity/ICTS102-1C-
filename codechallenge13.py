name = input("Enter your name: ")
print("POSITIVE NUMBER COLLECTOR")

positive_numbers = ""
total = 0
collecting = True

while collecting == True:
    number = eval(input("Enter a positive number (0 to stop): "))

    if number > 0:
        print("POSITIVE NUMBER ACCEPTED")
        total += number
        positive_numbers += str(number) + " "
        continue
    elif number == 0:
        print("SESSION ENDED")
        break
    else:
        if number < 0:
            print("NEGATIVE NUMBER REJECTED")
        else:
            print("Invalid input detected")
        continue

print(f"Hello {name}, the total of all positive numbers is {total}")
print(f"Your POSITIVE NUMBERS are: {positive_numbers}")
