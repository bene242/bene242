import pandas as pd
import numpy as np
import random
import openpyxl

# Funktion zum Erstellen eines DataFrames mit Zufallswerten
def create_random_dataframe(rows, cols, min_value, max_value):
    data = np.random.randint(min_value, max_value, size=(rows, cols))
    df = pd.DataFrame(data)
    return df

# Erstellen der beiden DataFrames
df1 = create_random_dataframe(3, 14, 100, 3000)
df2 = create_random_dataframe(3, 14, 100, 3000)

# Funktion zum Schreiben der DataFrames in eine Excel-Datei
def write_to_excel(df1, df2, filename):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='Tabelle1', index=False)
        df2.to_excel(writer, sheet_name='Tabelle2', index=False)

# Schreiben der DataFrames in eine Excel-Datei
write_to_excel(df1, df2, 'tabellen.xlsx')

# Ausgabe der DataFrames zur Überprüfung
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
