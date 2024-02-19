import time
import random
import matplotlib.pyplot as plt

# Function to generate simulated air quality data
def generate_air_quality_data():
    # Simulate MQ135 sensor data for air quality (PPM values)
    mq135_ppm = random.randint(50, 300)
    # Simulate MQ6 sensor data for air quality (PPM values)
    mq6_ppm = random.randint(50, 300)
    return mq135_ppm, mq6_ppm

# Function to display real-time air quality data
def display_air_quality_data(mq135_ppm, mq6_ppm):
    print("MQ135 PPM:", mq135_ppm)
    print("MQ6 PPM:", mq6_ppm)

# Function to trigger alarm if air quality exceeds threshold
def check_air_quality(mq135_ppm, mq6_ppm, threshold=200):
    if mq135_ppm > threshold or mq6_ppm > threshold:
        print("Air quality exceeded threshold! Alarm triggered.")
    else:
        print("Air quality within safe limits.")

# Function to log air quality data
def log_air_quality_data(mq135_ppm, mq6_ppm):
    with open("air_quality_logs.txt", "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}, MQ135 PPM: {mq135_ppm}, MQ6 PPM: {mq6_ppm}\n")

# Simulate air quality monitoring
num_iterations = 10  # Number of iterations to simulate
mq135_data = []
mq6_data = []

for i in range(num_iterations):
    mq135_ppm, mq6_ppm = generate_air_quality_data()
    mq135_data.append(mq135_ppm)
    mq6_data.append(mq6_ppm)
    display_air_quality_data(mq135_ppm, mq6_ppm)
    check_air_quality(mq135_ppm, mq6_ppm)
    log_air_quality_data(mq135_ppm, mq6_ppm)
    time.sleep(1)  # Simulate data collection every 1 second

# Plotting the data
plt.plot(range(num_iterations), mq135_data, label='MQ135 PPM')
plt.plot(range(num_iterations), mq6_data, label='MQ6 PPM')
plt.xlabel('Time')
plt.ylabel('PPM Value')
plt.title('Air Quality Monitoring')
plt.legend()
plt.show()
