from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Number of rows to generate
n_rows = 10000

# Create empty lists for each column
transaction_ids = []
customer_ids = []
product_lists = []
product_category_lists = []
total_purchase_amounts = []
purchase_dates = []
payment_methods = []
customer_ages = []
customer_genders = []
customer_locations = []
previous_purchases = []
accounts_created = []

# Generate fake data
for _ in range(n_rows):
    transaction_ids.append(fake.uuid4())
    customer_ids.append(fake.uuid4())
    product_lists.append([fake.bs() for _ in range(random.randint(1, 5))])  # 1 to 5 products
    product_category_lists.append([fake.catch_phrase() for _ in range(random.randint(1, 5))])  # 1 to 5 categories
    total_purchase_amounts.append(round(random.uniform(5.0, 200.0), 2))
    purchase_dates.append(fake.date_this_decade())
    payment_methods.append(random.choice(['Credit Card', 'PayPal', 'Cash']))
    customer_ages.append(random.randint(18, 65))
    customer_genders.append(random.choice(['Male', 'Female']))
    customer_locations.append(fake.city())
    previous_purchases.append(random.randint(0, 10))
    accounts_created.append(random.choice([0, 1]))

# Create a DataFrame
df = pd.DataFrame({
    'TransactionID': transaction_ids,
    'CustomerID': customer_ids,
    'ProductList': product_lists,
    'ProductCategoryList': product_category_lists,
    'TotalPurchaseAmount': total_purchase_amounts,
    'PurchaseDate': purchase_dates,
    'PaymentMethod': payment_methods,
    'CustomerAge': customer_ages,
    'CustomerGender': customer_genders,
    'CustomerLocation': customer_locations,
    'PreviousPurchases': previous_purchases,
    'AccountCreated': accounts_created
})

# Save the DataFrame to a CSV file
df.to_csv('fake_sales_data.csv', index=False)

print("Fake data generated and saved to 'fake_sales_data.csv'")
