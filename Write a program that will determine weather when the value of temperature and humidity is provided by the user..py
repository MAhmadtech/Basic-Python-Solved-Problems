

# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool


Temperature_in_celcius = int(input("Enter your temperture in celcius: "))
humidity_in_percentage = int(input("Enter your humidity in percentage: "))
if Temperature_in_celcius >=30 and humidity_in_percentage >=90:
    print("The whether is Hot and Humid")
elif Temperature_in_celcius >=30 and humidity_in_percentage <90:
    print("The whether is Hot")
elif Temperature_in_celcius <30 and humidity_in_percentage >=90:
    print("The whether is Cool and Humid")
else:
    Temperature_in_celcius <30 and humidity_in_percentage <90 
    print("The whether is Cool")  
 