import pandas as pd


def load_data():
    df = pd.read_csv('files/olympics.csv', header=1)
    df = df[0:len(df)-1]

    for name in df.columns:
        if '01 !' in name:
            df.rename(columns={name: name.replace('01 !', 'Gold')}, inplace=True)
        elif '02 !' in name:
            df.rename(columns={name: name.replace('02 !', 'Silver')}, inplace=True)
        elif '03 !' in name:
            df.rename(columns={name: name.replace('03 !', 'Bronze')}, inplace=True)
    list_a = df.index.values
    names= []
    for e in list_a:
        names.append(e.split('\xc2\xa0')[0])
    df.index = names
    return df

def first_country(df):
    return df.iloc[0]

def gold_medal(df):
    return df['Gold'].idxmax()


def biggest_difference_in_gold_medal(df):
    sum_gold = df['Gold']
    win_gold = df['Gold.1']
    diff = sum_gold-win_gold
    return diff.idxmax()

def get_points(df):
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
    return df['Points']
load_data()
first_country(load_data())
gold_medal((load_data()))
biggest_difference_in_gold_medal(load_data())
get_points(load_data())
#first_country(df)["# Summer"])
# print(gold_medal(df))
# print(biggest_difference_in_gold_medal(df))
# print(get_points(df))
