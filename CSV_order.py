import pandas as pd
import sys
import re

def extract_phone_number(string):
    match = re.search(r"(\d+-\d+-\d+)", string)
    if match:
        return match.group(1)
    else:
        return None

# read the CSV file
df = pd.read_csv('LAW.csv')

for ind in df.index:
    names = str(df['File Name'][ind]).split(' ')
    df['first_name'][ind] = names[0] if len(names) > 0 else None
    df['last_name'][ind] = names[1] if len(names) > 1 else None
    df['phone'][ind] = extract_phone_number(str(df['phone'][ind]))
    updated_email=str(df['email'][ind]).split(' ')
    df['email'][ind] = updated_email[0] if len(updated_email) >= 1 else None


df.to_csv('NEW.csv', index=False)
