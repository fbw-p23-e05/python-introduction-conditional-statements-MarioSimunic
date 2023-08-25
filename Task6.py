scale = input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: ")
temperature = int(input("Input the value of temperature you'd like to convert  :"))

if scale == "C":
    result = (temperature - 32) * 5 / 9
    print("he temperature in Celsius is ", result, "degrees.")
elif scale == "F":
    result = (temperature * 9 / 5) +32
    print("he temperature in Fahrenheit is ", result, "degrees.")
else:
    print("Please insert in right format.")