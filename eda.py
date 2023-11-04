import pandas as pd

# Load the dataset
df = pd.read_csv('res_dpre.csv')  # Replace 'your_dataset.csv' with your dataset file path

# Insight 1: Summary Statistics
insight1 = "Insight 1: Summary Statistics\n\n"
summary_stats = df.describe()
insight1 += str(summary_stats)

# Insight 2: Value Counts
insight2 = "\n\nInsight 2: Value Counts\n\n"
value_counts = df['platform'].value_counts()  # Replace 'column_of_interest' with the column you're interested in
insight2 += str(value_counts)

# Insight 3: Correlation for Numeric Columns
insight3 = "\n\nInsight 3: Correlation for Numeric Columns\n\n"
numeric_columns = df.select_dtypes(include=['number'])  # Select only numeric columns
correlation_matrix = numeric_columns.corr()
insight3 += str(correlation_matrix)

# Save Insights as Text Files
with open('eda-in-1.txt', 'w') as file1:
    file1.write(insight1)

with open('eda-in-2.txt', 'w') as file2:
    file2.write(insight2)

with open('eda-in-3.txt', 'w') as file3:
    file3.write(insight3)
