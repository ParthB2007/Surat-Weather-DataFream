import pandas as pd



def cleaningdata(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Dropping useless Colum

    clean = df.drop('PRECTOTCORR', axis=1)

    # renaming Head Cell
    clean.rename(columns={'MO': 'MONTH', 'DY': 'DAY', 'TS': 'Surface Temp', 'WD10M': 'Wind Direction', 'PS': 'Pressure',
                          'WS10M': 'Wind Speed'}, inplace=True)
    clean['Date'] = clean['DAY'].astype(str) + '-' + clean['MONTH'].astype(str) + '-' + clean['YEAR'].astype(str)

    # setting Date as index AND Dropping YEAR MONTH DAY cells


    columns_titles = ["Date", "Surface Temp", "Wind Direction", "Pressure", "Wind Speed"]
    clean = clean.reindex(columns=columns_titles)
    clean.to_csv(output_csv, index=False)


intput_csv = "data.csv"
output_csv = "cleaned_data.csv"

cleaningdata(intput_csv, output_csv)
