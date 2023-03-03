#Variables
name = 'Mike'
print(name)

name = input("Enter the name:")
print("Hello", name)

#Data Types
integer_num = 1
float_num = 2.0
string = 'Mike'
boolean = True

print(integer_num)
print(float_num)
print(string)
print(boolean)

a =  1
print(int(a))
print(str(a))
print(float(a))
print(bool(a))

x = 1
y = 2
print("addition", x + y)
print("Subtraction", x - y)
print("Multiply", x * y)
print("Division", x / y)

print((2*4) - 2 + 1 / 2)

#String Operations
string = "ABCDEFGH"
print(len(string))
print(string[0])
print(string[-1])

string = "WXYZ"
print(len(string))
print(string[0])
print(string[-1])

string = 'UVWXYZ'
print(string)

first_name = "Mike"
second_name = "Raw"
name=(first_name +" "+second_name)
print(name)

age = 30
print(' I am ' + str(age) + ' years old ')

message = 'python language'
print(message)
sliced_message = message[0:6]
print(sliced_message)

notic = '10 boys and 5 girls in class'
print(notic)
batch_boys = (notic[ :8])
batch_girls = (notic[12: ])
print(batch_boys)
print(batch_girls)

numbers = '123456789'
even_num = numbers[1::2]
print(even_num)
odd_num = numbers[0::2]
print(odd_num)

message = "John, did you start learning python"
print( 'John' in string)
print('Mike' not in string)

string = 'abcd'
print (string*4)

message = 'I am upper rank'
print(message.upper())

message = ' I am lower rank'
print(message.lower())

message = 'I am title'
print(message.title())

message = 'This is the best languagae.     '
print(message)
print(message.rstrip())

increment = '4%'
print(increment.rstrip('%'))

message = "        There is a space at the start"
print(message)
print(message.lstrip())

message = "    There is a space here  "
print(message)
print(message.strip())

message = '#########444********'
print(message)
print(message.rstrip('*').lstrip('#'))

message = 'this is lang'
print(message)
print(message.count('i'))
print(message.count('i',5))
