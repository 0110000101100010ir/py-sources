#string to binary 

str_inp = input("string: ")
binary = list()
for char in str_inp:
    binary.append("0"+format(ord(char),'b'))
    
out = "".join(binary)
print(out)
