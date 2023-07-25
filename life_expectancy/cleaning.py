import pandas as pd

def read_tsv_to_dataframe(file_path):
    df = pd.read_csv(file_path, sep='\t', skiprows=1, na_values=':', index_col='geo\\time')
    
    df.dropna(axis=1, how='all', inplace=True)

    df = df.reset_index()
    df = pd.melt(df, id_vars=['geo\\time'], var_name='year', value_name='value')

    # Rename columns
    df.rename(columns={'geo\\time': 'region'}, inplace=True)

    # Split the 'year' column to separate 'unit', 'sex', and 'age' columns
    df[['unit', 'sex', 'age']] = df['year'].str.split(',', expand=True)
    df.drop(columns='year', inplace=True)

    return df

file_path = '/home/acbessa/assignments/life_expectancy/data/eu_life_expectancy_raw.tsv'
df = read_tsv_to_dataframe(file_path)


print(df)