import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/naive-bayes-project-tutorial/main/playstore_reviews.csv"

df = pd.read_csv(url)

df.to_csv('reviews.csv', index=False)
print("Dataset saved as 'reviews.csv'")