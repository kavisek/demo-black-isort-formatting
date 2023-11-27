import numpy as np
import pandas as pd


def main():
    # Step 1: Data Creation
    # Create a sample NumPy array with random data
    data = np.random.rand(10, 3)  # 10 rows, 3 columns

    # Step 2: Convert to Pandas DataFrame
    df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3"])

    # Step 3: Data Aggregation
    # Example: Compute mean of each column
    aggregated_data = df.mean()

    # Step 4: Save Aggregated Data to a file
    aggregated_data.to_csv("aggregated_data.csv")

    # Step 5: Print Final Output
    print("Aggregated Data:")
    print(aggregated_data)


if __name__ == "__main__":
    main()
