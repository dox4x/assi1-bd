import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned and transformed dataset
df = pd.read_csv('res_dpre.csv')

# Create a histogram of the 'meta_score' column
plt.hist(df['meta_score'], bins=20, color='skyblue')
plt.title('Meta Score Distribution')
plt.xlabel('Meta Score')
plt.ylabel('Frequency')

# Save the visualization as 'vis.png'
plt.savefig('vis.png')

# Show the visualization (optional)
plt.show()
