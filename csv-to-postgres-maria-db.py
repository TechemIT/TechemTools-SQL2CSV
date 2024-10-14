import csv
import sys
import io
import re

def format_date(value):
    # Converte le date da MM/GG/AAAA a AAAA-MM-GG
    match = re.match(r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', value)
    if match:
        month, day, year = match.groups()
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    return value

def csv_to_sql(csv_file, table_name):
    with open(csv_file, 'r', encoding='utf-8-sig', errors='replace') as file:
        reader = csv.reader(file, delimiter=';')
        headers = next(reader)
        
        print(f"-- Inserimenti nella tabella `{table_name}`")
        for row in reader:
            columns = ', '.join(f'`{header.strip()}`' for header in headers)
            values = ', '.join(f"'{format_date(value).replace('\'', '\'\'')}'" for value in row)
            sql = f"INSERT INTO `{table_name}` ({columns}) VALUES ({values});"
            print(sql)

# Test della funzione format_date
test_dates = ['09/30/2021', '10/01/2020', '12/31/2022']
for date in test_dates:
    print(f"Test date: {date} -> {format_date(date)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilizzo: python script.py <file_csv> <nome_tabella>")
        sys.exit(1)

    csv_file = sys.argv[1]
    table_name = sys.argv[2]

    # Reindirizza l'output standard a un buffer che usa UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    csv_to_sql(csv_file, table_name)
