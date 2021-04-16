str = "sujata qa .panda"
str1 = " QA"
str2 = "  sujata  "

print(str)       # sujata
print(str[2])    # j
print(str[-1])   # a
print(str[0:5])  # print substring from 0 index to 5-1 index
print(str+str1)  # concat 2 string with plus operator
print(str2 in str)  # check str2 string present in the str string or not ,return true or false
var = str.split(".")   # split will divide the string in 2 parts one right side and another left side
print(var)
print(var[0])
print(str2.strip())    # trim he space at beginning and end of the string
print(str2.lstrip())    # trim left white space
print(str2.rstrip())    # trim right white space
