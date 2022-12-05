# Sample_data=[22, 28,33,26,39,15,19]
# 1. Write a function to calculate mean
# 2. Write a function to calculate variance
# 3. Calculate standard deviation

# Start
import statistics
# Declare the Sample_data
sample_data=[22, 28,33,26,39,15,19]
# Start the function
def calculations(sample_data):
    print("The mean is:",statistics.mean(sample_data))
# Call the function
calculations(sample_data)