#request input from user to enter three different integers
#print out the sum of all integers
#print out the first number minus the second number
#print out the third number multiplied by the first number 
#the sum of all three numbers divided by the third number
import math

request_1 = int(input("Enter a digit: "))
request_2 = int(input("Enter second digit: "))
request_3 = int(input("Enter third digit: "))

request_sum = request_1 + request_2 + request_3
request_subtraction = request_1 - request_2
request_multiplication = request_3 * request_1
final_request = request_sum / request_3



print(request_sum)
print(request_multiplication)
print(final_request)
print(request_subtraction)

