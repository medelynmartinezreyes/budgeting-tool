from csv import DictReader
from typing import TypedDict

class Spending(TypedDict):
    Date: str
    Amount: float
    Category: str
    Description: str


with open("spending.csv", 'r') as file:
    
    data = DictReader(file)
    selected_data: list[Spending] = [
        {
            'Date': row['Transaction Date'],
            'Description': row['Description'],
            'Category': row['Category'],
            'Amount': float(row['Amount'])
        }
        for row in data
    ]
    
print(selected_data)