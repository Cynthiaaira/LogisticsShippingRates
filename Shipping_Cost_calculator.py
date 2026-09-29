#Shipping Calculator

##input package weight and shipping weight
weight = float(input("Enter the weight of the package in kilograms:"))
rate = float(input("Enter the shipping rate per kilogram:"))

#calculate shipping cost
shipping_cost = weight * rate

#deisplay the result
print(f"Shipping cost: {shipping_cost} USD")
