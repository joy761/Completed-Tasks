'''Create a program to calculate total holiday cost based on user's input. 
1.file has functions 'hotel_cost', 'place cost' and 'car_rental' with arguments (nights, city, days)
2. functions calculate the values (hotel, plane and car)
3.The function holiday_cost should calculate the total cost for the trip
4. code displays total cost for the trip'''


def hotel_cost(nights):
    return nights * 200

def plane_cost(city):
   if city == 'Manchester':
    return 250
   elif city =='Liverpool':
      return 450
    
   elif city == 'London':
        return 600
   elif city == 'Kent':
        return 200 
   else:
       print("Invalid input")
   
def car_rental(days):
   return days * 50
    
def holiday_cost(nights,city, days):
    hotel = hotel_cost(nights)
    print("The cost for your hotel stay for", nights, " nights is:", hotel)

    plane = plane_cost(city)
    print("The cost of your plane ticket to", city, "is:", plane )

    car = car_rental(days)
    print("The cost for your car rental for ", days, "days is:", car )
    
    total = hotel + plane + car
    print("The total cost for oyour holiday is: ", total)

print("Hello there! pick a city below: ")
city = (input('\n 1. Manchester \n 2. Liverpool \n 3. London \n 4. Kent \n  '))
nights =(int(input('How many nights will you be staying? ')))
days = (int(input('How many days will you need a car for? ')))

holiday_cost(nights, city, days)