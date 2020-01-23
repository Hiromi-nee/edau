def check_unique(df, threshold=3):
    """
    Check unique values in a dataframe.
    df: dataframe
    threshold: minimum about of unique values to not flag out.
    """
    counts = {}
    insuf_cols = []
    has_empty_cols = []
    cols = df.columns.values
    for col in cols:
        uniq_vals = df[col].unique() 
        count_uniq = len(uniq_vals)
        print("%20s: %5d" % (col, count_uniq), end=" ")
        counts[col] = count_uniq
        if count_uniq <= threshold:
            insuf_cols.append(col)
            print(uniq_vals, end= " ")
        if '' in uniq_vals:
            print("Has empty", end=" ")
            has_empty_cols.append(col)
        print("")
    return counts, insuf_cols, has_empty_cols
