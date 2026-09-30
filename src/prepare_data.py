from pathlib import Path
import pandas as pd

RANDOM_STATE = 42
MAX_DOCUMENTS = 10_000

RAW_PATH = Path("data/raw/complaints.csv")
OUTPUT_PATH = Path("data/processed/complaints_sample.csv")

COLUMNS = [
    "Complaint ID",
    "Date received",
    "Product",
    "Issue",
    "Consumer complaint narrative"
]

df = pd.read_csv(
    RAW_PATH,
    usecols=COLUMNS,
    low_memory=False
)

df = df.dropna(
    subset=["Consumer complaint narrative"]
).copy()

df["Consumer complaint narrative"] = (
    df["Consumer complaint narrative"]
    .astype(str)
    .str.strip()
)

df = df[
    df["Consumer complaint narrative"].str.len() >= 50
]

df = df.drop_duplicates(
    subset=["Consumer complaint narrative"]
)

if len(df) > MAX_DOCUMENTS:
    df = df.sample(
        n=MAX_DOCUMENTS,
        random_state=RANDOM_STATE
    )

df = df.reset_index(drop=True)

OUTPUT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print(f"{len(df)} Beschwerden gespeichert.")