#write a python function to perform the addition of all even numbers between 1, 100
#Function, for loop with range(), if condition

def sum_even_numbers():
    total = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total += number
    return total

result = sum_even_numbers()
print("The sum of all even numbers between 1 and 100 is:", result)
