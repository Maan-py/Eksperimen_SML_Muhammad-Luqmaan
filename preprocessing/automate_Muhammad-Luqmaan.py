import pandas as pd
from sklearn.preprocessing import OneHotEncoder, RobustScaler
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
    # Pisahkan fitur dan label
    X = df.drop(columns=["label"])
    y = df["label"]

    # Identifikasi kolom
    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
    numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

    # Encoding kategorikal
    encoder = OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore")
    X_cat = encoder.fit_transform(X[categorical_cols])
    cat_feature_names = encoder.get_feature_names_out(categorical_cols)

    X_cat = pd.DataFrame(X_cat, columns=cat_feature_names, index=X.index)

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
    # ===============================
    # PATH (SESUAIKAN)
    # ===============================
    INPUT_PATH = "UNSW_NB15_raw/UNSW_NB15_training-set.csv"
    OUTPUT_PATH = "preprocessing/UNSW_NB15_preprocessing/UNSW_NB15_preprocessed.csv"

    # Load data
    df = load_data(INPUT_PATH)

    # (Opsional) Sampling ke 10.000 data
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
