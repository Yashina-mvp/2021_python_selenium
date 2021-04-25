
list= [5,10,15,20,25,50,20]

for index,value in enumerate(list):
    if value == 20:
        list[index]= 200
print(list)
print(list[2:6])