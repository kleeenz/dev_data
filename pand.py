import pandas as pd

def Dframe(new_row):

    df = pd.read_csv("python hands-on - dataset.csv")

    #this checks if a new row was added to the dataframe, will the column obsolete stil output the True or false based on the input provided
    df = df.append(new_row, ignore_index=True)
    df["obsolete"] = df["date"].apply(lambda x: x<"2021-01-01")

    print(df)

    Json_data = df.to_json(r'C:\Users\hp\Desktop\python pandas\new_data.json')

n = {"date": "2017-01-01", "sku": 102020208, "warehouse_location": "enugu", "quantity": 44}

Dframe(n)










