def df_get_row_by_column_value(df, column_name, value):
    matched_rows = df.loc[df[column_name] == value]

    if not matched_rows.empty:
        return matched_rows.iloc[0]

    return None
