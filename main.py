import pandas as pd

print("==================================================")
print("🎬 DATA SCIENCE PROJECT 1: MOVIE GENRE FILTER")
print("==================================================\n")

# DATA SOURCE INITIALIZATION: storing the raw unstructured streaming data inside a python dictionary
movie_raw_data = {
    'Movie_Title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Hangover', 'Superbad', 'La La Land'],
    'Genre': ['Sci-Fi', 'Action', 'Sci-Fi', 'Comedy', 'Comedy', 'Romance'],
    'IMDb_Rating': [8.8, 9.0, 8.6, 7.7, 7.6, 8.0]
}
# DATA INGESTION PIPELINE : transforming the raw disctionary into a structured pandas dataFrame grid
df = pd.DataFrame(movie_raw_data)

print("📋 --- THE COMPLETE MOVIE DATASET ---")
print(df.to_string(index=False))
print("-" * 50)
# CONDITIONAL DATA FILTERING:  Extracting target records based on genre and  absolute rating threshold
selected_genre = 'Sci-Fi'
filtered_results = df[(df['Genre'] == selected_genre) & (df['IMDb_Rating'] > 8.5)]

print(f"\n🚀 --- RECOMMENDED {selected_genre.upper()} MOVIES (> 8.5 Rating) ---")
print(filtered_results[['Movie_Title', 'IMDb_Rating']].to_string(index=False))
print("==================================================")
