import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Make sure to download movies.csv from Kaggle or create your own CSV file with columns: Title, Genre, Year, Rating, Votes, Revenue (Millions)
data = pd.read_csv('movie.csv')

# Display first 5 rows
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Data Cleaning: Check for missing values
print("\nMissing values in dataset:")
print(data.isnull().sum())

# Drop rows with missing critical data (optional)
data.dropna(subset=['Rating', 'Genre', 'Year'], inplace=True)

# Top 10 highest-rated movies
top_movies = data.sort_values(by='Rating', ascending=False).head(10)
print("\nTop 10 Highest-Rated Movies:")
print(top_movies[['Title', 'Rating', 'Year', 'Genre']])

# Count of movies per genre
movies_per_genre = data['Genre'].value_counts()
print("\nMovies per Genre:")
print(movies_per_genre)

# Visualization: Number of movies per genre
plt.figure(figsize=(12,6))
sns.barplot(x=movies_per_genre.index, y=movies_per_genre.values)
plt.title('Number of Movies per Genre')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Average rating per year
avg_rating_per_year = data.groupby('Year')['Rating'].mean().reset_index()
plt.figure(figsize=(12,6))
sns.lineplot(x='Year', y='Rating', data=avg_rating_per_year)
plt.title('Average Movie Rating per Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.show()

# Scatter plot: Revenue vs Rating
plt.figure(figsize=(10,6))
sns.scatterplot(x='Revenue (Millions)', y='Rating', data=data)
plt.title('Revenue vs Rating')
plt.xlabel('Revenue (Millions)')
plt.ylabel('Rating')
plt.show()

# Optional: Save cleaned dataset
# data.to_csv('movies_cleaned.csv', index=False)

print("\nProject Completed Successfully!")
