import pandas as pd
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv('res_dpre.csv')

# Select columns suitable for K-means (e.g., 'meta_score' and 'user_review')
selected_columns = ['meta_score', 'user_review']

# Create a K-means model with k=3
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df[selected_columns])

# Get the count of records in each cluster
cluster_counts = df['cluster'].value_counts()

# Save the cluster counts to a text file
cluster_counts.to_csv('k.txt', header=['count'], index_label='cluster', sep='\t')

# Print the cluster counts to the console (optional)
print(cluster_counts)
