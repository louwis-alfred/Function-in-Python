def multiply(*numbers):
    total = 1
    for number in numbers: # Itiration
        total = total * number
    return total
    
print(multiply(2,4,5,6,7))
