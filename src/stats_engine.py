def compute_damage_by_work_type(df, start_date, end_date):
    filtered = df[
        (df["date"] >= start_date) &
        (df["date"] <= end_date)
    ]

    result = (
        filtered.groupby("work_type")
        .size()
        .sort_values(ascending=False)
    )

    return result.to_dict()