def camel_to_snake (camel):
    snake_case = ""
    for char in camel:
        if char.isupper():
            
            snake_case += "_" + char.lower()
            
        else:
            snake_case += char
            
    return snake_case
    
name = input("enter camel name")
print(camel_to_snake(name))