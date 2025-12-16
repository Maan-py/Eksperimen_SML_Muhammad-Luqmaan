import pandas as pd
from sklearn.preprocessing import LabelEncoder, RobustScaler
from sklearn.model_selection import train_test_split
import os


def load_data(path: str) -> pd.DataFrame:
    """Load dataset dari CSV"""
    return pd.read_csv(path)


def preprocess_data(df: pd.DataFrame):
    """
    Melakukan preprocessing data:
    - Pisah fitur & label
    - Encoding kategorikal
    - Scaling numerik
    - Gabung kembali
    """

    selected_features = [
        "dur",
        "proto",
        "service",
        "state",
        "spkts",
        "dpkts",
        "sbytes",
        "dbytes",
        "rate",
        "sttl",
        "dttl",
        "sload",
        "dload",
        "ct_srv_src",
        "ct_state_ttl",
        "label",
    ]

    df = df[selected_features]

    df = df.drop_duplicates()

    # Pisahkan fitur dan label
    X = df.drop(columns=["label"])
    y = df["label"]

    # Identifikasi kolom
    categorical_cols = ["proto", "service", "state"]

    numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns

    # Encoding kategorikal
    encoder = LabelEncoder()

    for col in categorical_cols:
        X[col] = encoder.fit_transform(X[col])

    encoded_cat_cols = X.columns.tolist()
    X_cat = pd.DataFrame(X, columns=categorical_cols, index=X.index)

    # Scaling numerik (aman untuk outlier)
    scaler = RobustScaler()
    X_num = scaler.fit_transform(X[numerical_cols])

    X_num = pd.DataFrame(X_num, columns=numerical_cols, index=X.index)

    # Gabungkan
    X_processed = pd.concat([X_num, X_cat], axis=1)

    return X_processed, y


def split_data(X, y, test_size=0.2, random_state=42):
    """Stratified train-test split"""
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )


def save_processed_data(X, y, output_path: str):
    """Simpan dataset hasil preprocessing"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    processed_df = X.copy()
    processed_df["label"] = y

    processed_df.to_csv(output_path, index=False)
    print(f"Dataset preprocessing tersimpan di: {output_path}")


def main():
    INPUT_PATH = "UNSW_NB15_raw/UNSW_NB15_training-set.csv"
    OUTPUT_PATH = "preprocessing/UNSW_NB15_preprocessing/UNSW_NB15_preprocessed.csv"

    # Load data
    df = load_data(INPUT_PATH)

    if len(df) > 10000:
        df = df.groupby("label", group_keys=False).apply(
            lambda x: x.sample(frac=10000 / len(df), random_state=42)
        )

    # Preprocessing
    X_processed, y = preprocess_data(df)

    # Simpan hasil preprocessing
    save_processed_data(X_processed, y, OUTPUT_PATH)


if __name__ == "__main__":
    main()
