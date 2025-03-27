#######################################################################################################################################################
# 
# Name: Nguyen Sao Mai
# SID: 740098557
# Exam Date: 27 March 2025
# Module: BEMM458 - Programming for Business Analytics
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-mai553-exeter
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################

# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []

# The allocated keys are the first and last digit of my SID: 7 and 7
allocated_keys = [7, 7]

# Loop through the allocated keys
for key in allocated_keys:
    # Get the word corresponding to the key from the dictionary
    word = key_comments[key]
    
    # Find the start and end positions of the word in the customer_feedback string
    start_pos = customer_feedback.find(word)
    end_pos = start_pos + len(word) - 1  # End position is inclusive
    
    # Append the tuple (start, end) to the list
    my_list.append((start_pos, end_pos))

# Print the output the result
print("Start and end positions of the words:", my_list)

# OUTPUT: Start and end positions of the words: [(129, 135), (129, 135)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 57

# Function to calculate Operating Profit Margin
def operating_profit_margin(revenue, operating_profit):
    """
    Calculate Operating Profit Margin as a percentage.
    Formula: (Operating Profit / Revenue) * 100
    """
    return (operating_profit / revenue) * 100  # Return the calculated percentage

# Function to calculate Revenue per Customer
def revenue_per_customer(total_revenue, total_customers):
    """
    Calculate Revenue per Customer.
    Formula: Total Revenue / Total Customers
    """
    return total_revenue / total_customers  # Return the revenue per customer

# Function to calculate Customer Churn Rate
def customer_churn_rate(customers_lost, total_customers):
    """
    Calculate Customer Churn Rate as a percentage.
    Formula: (Customers Lost / Total Customers) * 100
    """
    return (customers_lost / total_customers) * 100  # Return the churn rate as a percentage

# Function to calculate Average Order Value
def average_order_value(total_revenue, total_orders):
    """
    Calculate Average Order Value.
    Formula: Total Revenue / Total Orders
    """
    return total_revenue / total_orders  # Return the average order value

# Input values based on my ID
first_two_digits = 74  # First two digits of my ID
last_two_digits = 57  # Last two digits of my ID

# Call your designed functions here using the first two and last two digits of my ID
opm = operating_profit_margin(first_two_digits, last_two_digits)  # Calculate Operating Profit Margin
rpc = revenue_per_customer(first_two_digits, last_two_digits)  # Calculate Revenue per Customer
ccr = customer_churn_rate(last_two_digits, first_two_digits)  # Calculate Customer Churn Rate
aov = average_order_value(first_two_digits, last_two_digits)  # Calculate Average Order Value

# Print the results
print("Operating Profit Margin:", opm, "%")  # Print the Operating Profit Margin
print("Revenue per Customer:", rpc)  # Print the Revenue per Customer
print("Customer Churn Rate:", ccr, "%")  # Print the Customer Churn Rate
print("Average Order Value:", aov)  # Print the Average Order Value

# OUTPUT:
# Operating Profit Margin: 77.02702702702703 %
# Revenue per Customer: 1.2982456140350878
# Customer Churn Rate: 77.02702702702703 %
# Average Order Value: 1.2982456140350878

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np  # Import NumPy for numerical operations
from sklearn.linear_model import LinearRegression  # Import LinearRegression for building the regression model

# Data: Price and Demand
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)  # Convert prices to a 2D array for sklearn
demands = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])  # Demand values corresponding to the prices

# Create and fit the linear regression model
model = LinearRegression()  # Initialize the linear regression model
model.fit(prices, demands)  # Train the model using the price and demand data

# 1. Find the price that maximizes revenue
# Revenue = Price * Demand
# Since demand decreases linearly with price, I calculate revenue for each price and find the maximum
revenues = prices.flatten() * demands  # Calculate revenue for each price by multiplying price and demand
max_revenue_index = np.argmax(revenues)  # Find the index of the maximum revenue
max_revenue_price = prices[max_revenue_index][0]  # Get the price corresponding to the maximum revenue
max_revenue = revenues[max_revenue_index]  # Get the maximum revenue value

# 2. Predict the demand when the price is set at £52
predicted_demand = model.predict([[52]])[0]  # Use the trained model to predict demand for a price of £52

# Print the results
print("Price that maximizes revenue: £", max_revenue_price)  # Output the price that maximizes revenue
print("Maximum revenue: £", max_revenue)  # Output the maximum revenue
print("Predicted demand at £52: ", predicted_demand)  # Output the predicted demand when the price is £52

# OUTPUT:
# Price that maximizes revenue: £ 45
# Maximum revenue: £ 8550
# Predicted demand at £52:  158.17272727272726

##########################################################################################################################################################
# Question 4 - Debugging; Plotting and data visualization chart

import random  # Import the random module to generate random numbers
import matplotlib.pyplot as plt  # Import matplotlib for plotting the chart

# Generate 100 random numbers between 1 and your student ID number
max_value = 740098557  # My student ID is used as the maximum value for random number generation
random_numbers = [random.randint(1, max_value) for i in range(100)]  # Generate 100 random integers between 1 and max_value

# Plotting the numbers in a line chart
plt.plot(
    random_numbers,  # The list of random numbers to plot
    marker='o',  # Use circular markers for each data point
    markerfacecolor='green',  # Set the fill color of the markers to green
    markeredgecolor='red',  # Set the edge color of the markers to red
    linestyle='--',  # Use a dashed line to connect the data points
    label='Random Numbers',  # Add a label for the legend
    color='blue'  # Set the line color to blue
)

plt.title("Line Chart of 100 Random Numbers")  # Title describes the chart content
plt.xlabel("Index")  # The x-axis represents the index of the random numbers
plt.ylabel("Random Number")  # The y-axis represents the random number values
plt.legend()  # Display the label defined earlier in the legend
plt.grid(True)  # Enable grid lines on the chart
plt.show()  # Show the chart on the screen