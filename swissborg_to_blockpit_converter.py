import pandas as pd

# File-Paths
input_file = './swissborg_export.csv'
template_file = './blockpit_template.csv'
output_file = './converted_blockpit_import.csv'

# Read data
input_data = pd.read_csv(input_file)

# Function to merge transaction pairs and process other transactions
def merge_transactions(df):
    merged_data = []
    grouped = df.groupby('Time in UTC')
    
    for time, group in grouped:
        if len(group) == 2 and 'Sell' in group['Type'].values and 'Buy' in group['Type'].values:
            sell = group[group['Type'] == 'Sell'].iloc[0]
            buy = group[group['Type'] == 'Buy'].iloc[0]
            merged_data.append({
                'Date (UTC)': pd.to_datetime(sell['Time in UTC']).strftime('%d.%m.%Y %H:%M:%S'),
                'Integration Name': 'SwissBorg',
                'Label': 'Trade',
                'Outgoing Asset': sell['Currency'],
                'Outgoing Amount': sell['Gross amount'],
                'Incoming Asset': buy['Currency'],
                'Incoming Amount': buy['Gross amount'],
                'Fee Asset (optional)': buy['Currency'] if buy['Fee'] > 0 else '',
                'Fee Amount (optional)': buy['Fee'],
                'Comment (optional)': sell['Note'],
                'Trx. ID (optional)': ''
            })
        else:
            for _, row in group.iterrows():
                if row['Type'] == 'Withdrawal':
                    merged_data.append({
                        'Date (UTC)': pd.to_datetime(row['Time in UTC']).strftime('%d.%m.%Y %H:%M:%S'),
                        'Integration Name': 'SwissBorg',
                        'Label': 'Withdrawal',
                        'Outgoing Asset': row['Currency'],
                        'Outgoing Amount': row['Gross amount'],
                        'Incoming Asset': '',
                        'Incoming Amount': '',
                        'Fee Asset (optional)': row['Currency'] if row['Fee'] > 0 else '',
                        'Fee Amount (optional)': row['Fee'],
                        'Comment (optional)': row['Note'],
                        'Trx. ID (optional)': ''
                    })
                elif row['Type'] == 'Deposit':
                    merged_data.append({
                        'Date (UTC)': pd.to_datetime(row['Time in UTC']).strftime('%d.%m.%Y %H:%M:%S'),
                        'Integration Name': 'SwissBorg',
                        'Label': 'Deposit',
                        'Outgoing Asset': '',
                        'Outgoing Amount': '',
                        'Incoming Asset': row['Currency'],
                        'Incoming Amount': row['Gross amount'],
                        'Fee Asset (optional)': row['Currency'] if row['Fee'] > 0 else '',
                        'Fee Amount (optional)': row['Fee'],
                        'Comment (optional)': row['Note'],
                        'Trx. ID (optional)': ''
                    })
                else:
                    print(f"Warning: Unknown transaction type {row['Type']} for time {time}")
    
    return pd.DataFrame(merged_data)

# Merge transaction pairs and process other transactions
merged_data = merge_transactions(input_data)

# Write converted data to the template
merged_data.to_csv(output_file, index=False)

print(f'Data successfully converted and saved to {output_file}.')