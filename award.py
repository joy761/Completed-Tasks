#request input from user for each sport to determine the total time taken to complete the triarhlon.
#within_the_qualifying_time = 0 - 100 minutes
#within_5_minutes_of_the_qualifying_time = 101 - 105 minutes
#within_10minues_of_the_qualifying_time = 106 - 110 minutes
#more_than_10_minutes_of_from_the_qualifying_time = 111+ minutes




swimming = int(input("Enter time taken for swimming in minutes : "))
print("Time taken for Swimming task: ",swimming)
#request input for swimming time

cycling = int(input("Enter time taken for cycling in minutes : "))
print("Time taken for Cycling task: ",cycling)
#request input for cycling time

running = int(input("Enter time taken for running in minutes : "))
print("Time taken for Running task: ",running)
#request input for running time

Total_time=swimming+cycling+running
print("Total time taken for triathlon: ",Total_time)
#calculate total time for the trialthon


if Total_time <= 100:
    print("Provincial colours")

elif Total_time >= 101 and Total_time <= 105:
        print("Provincial Half colours")

elif Total_time >=106 and Total_time <= 110: 
        print("Provincial scroll")

else :
    print("No award")





