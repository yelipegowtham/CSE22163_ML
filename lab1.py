import numpy as np
import pandas as pd

# Load your dataset
data = pd.read_excel(r"C:\Users\year3\Downloads\Lab Session Data.xlsx")  # Read the first sheet if sheet_name is not specified

# Assume the dataset has columns: ['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)', 'Payment (Rs)']
A = data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values  # Input features
C = data['Payment (Rs)'].values  # Target prices

# Calculate the pseudo-inverse of A
A_pinv = np.linalg.pinv(A)

# Calculate the coefficients
X = A_pinv @ C

print("Coefficients for price prediction:")
print(X)

value1 = float(input("Enter quantity of Candies (#): "))
value2 = float(input("Enter quantity of Mangoes (Kg): "))
value3 = float(input("Enter quantity of Milk Packets (#): "))

new_data = np.array([[value1, value2, value3]])  # New feature values

predicted_price = new_data @ X

print(f"Predicted price: {predicted_price[0]:.2f} Rs")
