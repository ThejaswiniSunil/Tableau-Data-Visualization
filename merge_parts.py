import pandas as pd, pathlib

data = pathlib.Path("data")
total = 0
for m in range(1, 7):
    stem = f"2020{m:02d}-citibike-tripdata"
    parts = sorted(data.glob(f"{stem}_*.csv"))
    df = pd.concat(
        (pd.read_csv(p, encoding="ISO-8859-1", low_memory=False) for p in parts),
        ignore_index=True,
    )
    df.to_csv(data / f"{stem}.csv", index=False, encoding="ISO-8859-1")
    total += len(df)
    print(stem, len(parts), "parts ->", len(df), "rows")

print("Total rows:", total)
print("Columns:", list(df.columns))
