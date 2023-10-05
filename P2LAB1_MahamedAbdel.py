# Input the car's gas mileage (miles/gallon) and cost of gas (dollars/gallon)
miles_per_gallon = float(input("Enter the car's gas mileage (miles per gallon): "))
cost_per_gallon = float(input("Enter the cost of gas (dollars per gallon): "))

# Calculate the gas cost for different distances
distances = [20, 75, 500]

# Initialize a list to store the results
results = []

# Calculate the gas cost for each distance
for distance in distances:
    cost = (distance / miles_per_gallon) * cost_per_gallon
    results.append((distance, cost))

# Display the results with labels and two decimal places
print("Gas Costs:")
print("-----------")
for distance, cost in results:
    print(f"For {distance} miles: ${cost:.2f}")
