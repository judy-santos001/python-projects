


import sys

contacts = [
    ('James', 42),
    ('Livia', 36),
    ('Jolie', 12),
    
]
name = input ("nome: ")

for x in  contacts:
    if  name in x :
        print(str(x[0])+ " tem " + str(x[1]),  "anos")
        break

else:
    print("Not found")

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print(' You typed' + response + '.')