#continuously request input from user, until user enters -1
#when input == -1, stop request
#The program must then calculate the average of enteries excluding -1

request = float(0)
numbers = float(-1)
count = []

print("Enter a number different from -1 ")
request = float(input("or Enter -1 to calculate average: "))

request = float(request)
while request != -1:
    count.append(request)
    request = float(input("Enter a number: "))
    request = float(request)
if request == -1:
    average = sum(count)/len(count)
print("average is: ", average)