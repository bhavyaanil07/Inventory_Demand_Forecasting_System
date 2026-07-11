import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"])

    # Feature Engineering
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["Day_of_Week"] = df["Date"].dt.dayofweek

    # Drop Date
    df.drop(columns=["Date"], inplace=True)

    # Encode categorical columns
    categorical_columns = [
        "Product_Name",
        "Category",
        "Promotion",
        "Supplier"
    ]

    encoder = LabelEncoder()

    for column in categorical_columns:
        df[column] = encoder.fit_transform(df[column])

    return df