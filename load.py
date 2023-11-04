import pandas as pd
import argparse

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Load a dataset from a file.")
    parser.add_argument("file_path", type=str, help="Path to the dataset file")

    args = parser.parse_args()
    file_path = args.file_path

    # Load the dataset
    dataset = load_dataset(file_path)

    if dataset is not None:
        print("Dataset loaded successfully.")
        print(dataset.head())  # You can perform any desired operations on the dataset here

if __name__ == "__main__":
    main()
