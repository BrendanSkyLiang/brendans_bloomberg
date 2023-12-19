def find_col_index(df, target_value, row_index):
    """
    Finds the column indexes of a value in a specific row of a pandas dataframe.

    Args:
    df: The pandas dataframe.
    target_value: The value to search for.
    row_index: The index of the specific row.

    Returns:
    A list of column indexes where the target value is found, or an empty list if not found.
    """
    row = df.loc[row_index]
    indexes = row[row == target_value].index.tolist()
    if len(indexes) > 0:
        return indexes
    else:
        raise ValueError(f"target value {target_value} is not in range")