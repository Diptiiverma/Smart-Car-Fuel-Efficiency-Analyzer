import numpy as np   # Import NumPy library for numerical operations

# Load the car dataset from CSV file (skip first row which contains column names)
data = np.genfromtxt("Smart Car Fuel Efficiency Analyzer/car_data.csv", delimiter=",", skip_header=1)

# Extract individual columns using slicing
engine = data[:,1]      # Engine size of cars
weight = data[:,2]      # Weight of cars
hp = data[:,3]          # Horsepower
city = data[:,4]        # City mileage
highway = data[:,5]     # Highway mileage
age = data[:,6]         # Age of car in years

# Calculate average mileage using vectorized operation
avg_mileage = (city + highway) / 2

# Calculate fuel efficiency score using broadcasting
# Higher score means better fuel efficiency
efficiency_score = (avg_mileage * 1000) / (weight * age)

# Identify bottom 25% low efficiency cars using percentile
low_eff = efficiency_score < np.percentile(efficiency_score, 25)
low_eff_cars = data[low_eff]

# Find best and worst performing cars based on efficiency score
best = np.argsort(efficiency_score)[-3:]     # Top 3 efficient cars
worst = np.argsort(efficiency_score)[:3]     # Bottom 3 inefficient cars

# Detect extreme high efficiency outliers (top 10%)
outliers = efficiency_score > np.percentile(efficiency_score, 90)

# Mark cars that require service:
# Condition → Below average efficiency & Age > 5 years
service_required = (efficiency_score < np.mean(efficiency_score)) & (age > 5)

# Save service required cars into a new CSV file
header = "Car_ID,Engine_Size,Weight,Horsepower,City_Mileage,Highway_Mileage,Age"
np.savetxt("service_required_cars.csv",
           data[service_required],
           delimiter=",",
           fmt="%.2f",
           header=header,
           comments="")
