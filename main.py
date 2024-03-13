import pandas as pd
import random


# Read the data from the csv file
df = pd.read_csv('cereal_data.csv')


# Define mappings for company and type
company_mapping = {'A': 'American Home Food Products',
                   'G': 'General Mills',
                   'K': 'Kelloggs',
                   'N': 'Nabisco',
                   'P': 'Post',
                   'Q': 'Quaker Oats',
                   'R': 'Ralston Purina'}

type_mapping = {'C': 'Cereal - Cold', 'H': 'Cereal - Hot'}

# Map the single character representations to their string formats
df['mfr'] = df['mfr'].map(company_mapping)
df['type'] = df['type'].map(type_mapping)

# Rename the 'mfr' column to 'company'
df.rename(columns={'mfr': 'company'}, inplace=True)

# Add a new column 'vendor_id' with a constant value of 2
# New column for weight with const value of 'oz'
# Random from the set of weights
# Random from the set of selling prices
# Random from the threshold
weights = {'9', '12', '18', '24'}
selling_prices = {'2.99', '4.99', '3.99', '5.99', '7.29', '8.59'}
df['vendor_id'] = 2
df['weight_measurement'] = 'oz'
df['product_weight'] = df['name'].apply(lambda x: random.choice(list(weights)))
df['product_selling_price'] = df['name'].apply(lambda x: random.choice(list(selling_prices)))
df['threshold_amount'] = df['name'].apply(lambda x: random.randrange(4, 10))


def generate_product_barcode():
    # Generate the middle digits of the barcode
    middle_digits = ''.join(random.choices('0123456789', k=6))
    
    # Concatenate '1' as the first digit and the middle digits with dashes
    product_barcode = f'1-{middle_digits[:3]}-{middle_digits[3:]}'
    
    return product_barcode

# Use the function above to randomly generate barcodes of the same length using the format: 
#  1-xxx-xxx
# always start with a 1
df ['product_barcode'] = df['name'].apply(lambda x: generate_product_barcode())
print(df[['name', 'company', 'type', 'vendor_id', 'product_weight', 'product_selling_price', 'threshold_amount', 'product_barcode']])

# Reorganize the data frame so it is properly formatted to be inserted into the MySQL database
df = df[['vendor_id', 'product_barcode', 'name', 'product_weight', 'product_selling_price', 'weight_measurement', 'company', 'type', 'threshold_amount']]
print(df)