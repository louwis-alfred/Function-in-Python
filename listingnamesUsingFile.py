list_of_names = []
while True:
    name = input("What's your name?: ")
    list_of_names.append(name)
    file = open("names.txt", "w")
    continuation = input('Do you want to continue?: ').strip().lower()
    if continuation != "yes":
        break
    
with open("names.txt", "w") as file:
    for index, name in enumerate(list_of_names, start=1):
        file.write(f"{index}. {name}\n")
    file.close()