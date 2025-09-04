'''
Objects - 
1. Every object is unique
2. Every object have unique attributes
3. Each object can have abstractions (classifications or class) based on attributes
4. We can create/define objects according to abstractions or classes

String is a type of class
Methods/Behavior/Functions of string, example trim the string, change to lowercase, uppercase, etc.
These methods can be used to create (print) different objects.
'''

simple_string = "Hello World" ##string is series of character in quotes, use escape for quote within quotes
print(simple_string)
print(simple_string.upper()) ## change to uppercase
print(simple_string.lower()) ## change to lowercase

question = "Name"
query = input(f"What is your {question}?") ## Format operator help in taking input from previous string
print(query.capitalize())