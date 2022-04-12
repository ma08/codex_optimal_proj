
import numpy as np
import pandas as pd

def read_data(filename):
    df = pd.read_csv(filename, sep='\t', header=None)
    return df

def get_data(df):
    return df.values

def get_column(df, col):
    return df.values[:,col]

def get_row(df, row):
    return df.values[row,:]

def get_column_names(df):
    return df.columns.values

def get_row_names(df):
    return df.index.values

def get_shape(df):
    return df.shape

def get_size(df):
    return df.size

def get_data_type(df):
    return df.dtypes

def get_info(df):
    return df.info()

def get_describe(df):
    return df.describe()

def get_head(df, n):
    return df.head(n)

def get_tail(df, n):
    return df.tail(n)

def get_sample(df, n):
    return df.sample(n)

def get_unique(df):
    return df.unique()

def get_nunique(df):
    return df.nunique()

def get_value_counts(df):
    return df.value_counts()

def get_sort_values(df, col):
    return df.sort_values(col)

def get_sort_index(df):
    return df.sort_index()

def get_count(df):
    return df.count()

def get_mean(df):
    return df.mean()

def get_median(df):
    return df.median()

def get_min(df):
    return df.min()

def get_max(df):
    return df.max()

def get_std(df):
    return df.std()

def get_var(df):
    return df.var()

def get_skew(df):
    return df.skew()

def get_corr(df):
    return df.corr()

def get_cov(df):
    return df.cov()

def get_abs(df):
    return df.abs()

def get_cummin(df):
    return df.cummin()

def get_cummax(df):
    return df.cummax()

def get_cumsum(df):
    return df.cumsum()

def get_cumcount(df):
    return df.cumcount()

def get_diff(df):
    return df.diff()

def get_pct_change(df):
    return df.pct_change()

def get_tshift(df):
    return df.tshift()

def get_all(df):
    return df.all()

def get_any(df):
    return df.any()

def get_idxmax(df):
    return df.idxmax()

def get_idxmin(df):
    return df.idxmin()

def get_isnull(df):
    return df.isnull()

def get_notnull(df):
    return df.notnull()

def get_dropna(df):
    return df.dropna()

def get_fillna(df):
    return df.fillna()

def get_replace(df):
    return df.replace()

def get_interpolate(df):
    return df.interpolate()

def get_melt(df):
    return df.melt()

def get_pivot(df):
    return df.pivot()

def get_pivot_table(df):
    return df.pivot_table()

def get_stack(df):
    return df.stack()

def get_unstack(df):
    return df.unstack()

def get_wide_to_long(df):
    return df.wide_to_long()

def get_concat(df):
    return df.concat()

def get_merge(df):
    return df.merge()

def get_join(df):
    return df.join()

def get_append(df):
    return df.append()

def get_groupby(df):
    return df.groupby()

def get_agg(df):
    return df.agg()

def get_transform(df):
    return df.transform()

def get_apply(df):
    return df.apply()

def get_pipe(df):
    return df.pipe()

def get_filter(df):
    return df.filter()

def get_query(df):
    return df.query()

def get_loc(df):
    return df.loc()

def get_iloc(df):
    return df.iloc()

def get_at(df):
    return df.at()

def get_iat(df):
    return df.iat()

def get_ix(df):
    return df.ix()

def get_get_value(df):
    return df.get_value()

def get_set_value(df):
    return df.set_value()

def get_to_csv(df):
    return df.to_csv()

def get_to_excel(df):
    return df.to_excel()

def get_to_hdf(df):
    return df.to_hdf()

def get_to_json(df):
    return df.to_json()

def get_to_msgpack(df):
    return df.to_msgpack()

def get_to_pickle(df):
    return df.to_pickle()

def get_to_sql(df):
    return df.to_sql()

def get_to_stata(df):
    return df.to_stata()

def get_to_sparse(df):
    return df.to_sparse()

def get_to_string(df):
    return df.to_string()

def get_to_timestamp(df):
    return df.to_timestamp()

def get_to_xarray(df):
    return df.to_xarray()

def get_to_clipboard(df):
    return df.to_clipboard()

def get_to_period(df):
    return df.to_period()

def get_to_numpy(df):
    return df.to_numpy()

def get_to_records(df):
    return df.to_records()

def get_to_dict(df):
    return df.to_dict()
