# Sample_data=[22, 28,33,26,39,15,19]
# 1. Write a function to calculate mean
# 2. Write a function to calculate variance
# 3. Calculate standard deviation

# Start
import statistics
# Declare the Sample_data
sample_data=[22,28,33,26,39,15,19]
# Start the function
def calculations(sample_data):
    # Calculate the mean
    print("The mean is:",statistics.mean(sample_data))
    # Calculate the variance
    print("The variance is:",statistics.variance(sample_data))
    # Calculate the standard deviation
    print("The standard deviation:",statistics.stdev(sample_data))
# Call the function
calculations(sample_data)
