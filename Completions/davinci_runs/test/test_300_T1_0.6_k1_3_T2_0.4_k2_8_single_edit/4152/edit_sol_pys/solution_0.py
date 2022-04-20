import numpy as np
import pandas as pd


def read_file(file_name):
    df = pd.read_csv(file_name, sep='\t', header=None)
    return df


def to_list(df):
    return df.values.tolist()


def to_array(df):
    return df.values


def to_np(df):
    return np.array(df)


def to_dataframe(df):
    return pd.DataFrame(df)


def to_series(df):
    return pd.Series(df)


def to_dict(df):
    return df.to_dict()


def to_dict_list(df):
    return df.to_dict('list')


def to_dict_records(df):
    return df.to_dict('records')


def to_dict_split(df):
    return df.to_dict('split')


def to_dict_series(df):
    return df.to_dict('series')


def to_dict_index(df):
    return df.to_dict('index')


def to_dict_orient(df):
    return df.to_dict(orient='dict')


def to_dict_orient_list(df):
    return df.to_dict(orient='list')


def to_dict_orient_records(df):
    return df.to_dict(orient='records')


def to_dict_orient_split(df):
    return df.to_dict(orient='split')


def to_dict_orient_series(df):
    return df.to_dict(orient='series')


def to_dict_orient_index(df):
    return df.to_dict(orient='index')


def to_json(df):
    return df.to_json()


def to_json_orient(df):
    return df.to_json(orient='dict')


def to_json_orient_records(df):
    return df.to_json(orient='records')


def to_json_orient_index(df):
    return df.to_json(orient='index')


def to_json_orient_split(df):
    return df.to_json(orient='split')


def to_json_orient_table(df):
    return df.to_json(orient='table')


def to_json_orient_values(df):
    return df.to_json(orient='values')


def to_json_orient_columns(df):
    return df.to_json(orient='columns')


def to_json_orient_series(df):
    return df.to_json(orient='series')


def to_json_orient_records_lines(df):
    return df.to_json(orient='records', lines=True)


def to_json_orient_index_lines(df):
    return df.to_json(orient='index', lines=True)


def to_json_orient_split_lines(df):
    return df.to_json(orient='split', lines=True)


def to_json_orient_table_lines(df):
    return df.to_json(orient='table', lines=True)


def to_json_orient_values_lines(df):
    return df.to_json(orient='values', lines=True)


def to_json_orient_columns_lines(df):
    return df.to_json(orient='columns', lines=True)


def to_json_orient_series_lines(df):
    return df.to_json(orient='series', lines=True)


def to_json_orient_records_lines_date_format(df):
    return df.to_json(orient='records', lines=True, date_format='iso')


def to_json_orient_index_lines_date_format(df):
    return df.to_json(orient='index', lines=True, date_format='iso')


def to_json_orient_split_lines_date_format(df):
    return df.to_json(orient='split', lines=True, date_format='iso')


def to_json_orient_table_lines_date_format(df):
    return df.to_json(orient='table', lines=True, date_format='iso')


def to_json_orient_values_lines_date_format(df):
    return df.to_json(orient='values', lines=True, date_format='iso')


def to_json_orient_columns_lines_date_format(df):
    return df.to_json(orient='columns', lines=True, date_format='iso')


def to_json_orient_series_lines_date_format(df):
    return df.to_json(orient='series', lines=True, date_format='iso')


def to_json_orient_records_lines_date_format_date_unit(df):
    return df.to_json(orient='records', lines=True, date_format='iso', date_unit='s')


def to_json_orient_index_lines_date_format_date_unit(df):
    return df.to_json(orient='index', lines=True, date_format='iso', date_unit='s')


def to_json_orient_split_lines_date_format_date_unit(df):
    return df.to_json(orient='split', lines=True, date_format='iso', date_unit='s')


def to_json_orient_table_lines_date_format_date_unit(df):
    return df.to_json(orient='table', lines=True, date_format='iso', date_unit='s')


def to_json_orient_values_lines_date_format_date_unit(df):
    return df.to_json(orient='values', lines=True, date_format='iso', date_unit='s')


def to_json_orient_columns_lines_date_format_date_unit(df):
    return df.to_json(orient='columns', lines=True, date_format='iso', date_unit='s')


def to_json_orient_series_lines_date_format_date_unit(df):
    return df.to_json(orient='series', lines=True, date_format='iso', date_unit='s')
