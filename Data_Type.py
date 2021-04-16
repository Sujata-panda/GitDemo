#LIST
Values = [1, 2, 'rahul', 4, 5]
#Index will start from 0 from left and -1 from right
print(Values[0])
print(Values[1])
print(Values[2])
print(Values[3])
print(Values[4])
print(Values[-5])
#print some value at a time last one is index-1
print(Values[1:4])
#Insert some data in Values list in the place of inde 4
Values.insert(4, "sujata")
print(Values)
#add a data in the end of list
Values.append("End")
print(Values)
#update data in list
Values[1] = 22
print(Values)
#Delete data in the list
del Values[2]
print(Values)

#TUPLE
Val = (1, 2, "suj")
print(Val[-3])

#Dictionary
Dic = {1:2, "c":"suja", 2:"sss", "ahu":5  }
print(Dic[1])
print(Dic["c"])

#Create dictionary and add data in run time
Dict={}
Dict["first value"]=1
Dict["Last Value"]=2
print(Dict)
