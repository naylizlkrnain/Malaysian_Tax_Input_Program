import pandas as pd
import os

def verify_user(ic_number, password):

    if len(ic_number) == 12 and ic_number.isdigit():
        last_four_digits = ic_number[-4:]
        if password == last_four_digits:
            return True
    return False

def calculate_tax(income, tax_relief):

    chargeable_income = income - tax_relief

    if chargeable_income <= 0:
        return 0.0

    if chargeable_income <= 5000:
        tax = 0
    elif chargeable_income <= 20000:
        tax = (chargeable_income - 5000) * 0.01
    elif chargeable_income <= 35000:
        tax = 150 + (chargeable_income - 20000) * 0.03
    elif chargeable_income <= 50000:
        tax = 600 + (chargeable_income - 35000) * 0.08
    elif chargeable_income <= 70000:
        tax = 1800 + (chargeable_income - 50000) * 0.13
    else:
        tax = 4400 + (chargeable_income - 70000) * 0.21

    return round(tax, 2)


def save_to_csv(data, filename="tax_records.csv"):

    df_new = pd.DataFrame([data])

    if not os.path.exists(filename):
        df_new.to_csv(filename, index=False)
    else:
        df_new.to_csv(filename, mode='a', header=False, index=False)

def read_from_csv(filename="tax_records.csv"):

    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return None