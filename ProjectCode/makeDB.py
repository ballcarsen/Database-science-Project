import pandas
import sqlite3

sDatabaseName = "database.db"
conn = sqlite3.connect(sDatabaseName)
#result = conn.execute('SELECT * FROM IMDB')
#print(result.fetchone())
imdb_path = "~/Desktop/Database/title.basics.tsv"
person_path = "~/Desktop/Database/name.basics.tsv"
episode_path = "~/Desktop/Database/title.episode.tsv"
ratings_path = "~/Desktop/Database/title.ratings.tsv"
crew_path = "~/Desktop/Database/Processed Datasets/crew.csv"
genre_path = "~/Desktop/Database/Processed Datasets/genres.csv"
principle_path = "~/Desktop/Database/Processed Datasets/principals.csv"
prof_path = "~/Desktop/Database/Processed Datasets/professions.csv"
kaggle_path = "~/Desktop/Database/Processed Datasets/tconst_kaggle.csv"

df = pandas.read_csv(imdb_path, low_memory=False, sep='\t', header=0)
df = df.drop(['genres'], axis=1)
df.columns = ['Tconst', 'Title_type', 'Primary_title', 'Original_title', 'Is_adult', 'Start_year', 'End_year', 'Runtime']
df['Start_year'] = pandas.to_numeric(df['Start_year'], errors='coerce')
df['End_year'] = pandas.to_numeric(df['End_year'], errors='coerce')
df['Runtime'] = pandas.to_numeric(df['Runtime'], errors='coerce')
df.to_sql("SEASON", conn, if_exists="replace", index=False)


df = pandas.read_csv(episode_path, low_memory=False, sep='\t', header=0)
df = df.drop(['parentTconst'], axis=1)
df.columns = ['Econst', 'Season_Num', 'Episode_Num']
df['Season_Num'] = pandas.to_numeric(df['Season_Num'], errors='coerce')
df['Episode_Num'] = pandas.to_numeric(df['Episode_Num'], errors='coerce')
df.to_sql("EPISODE", conn, if_exists='replace', index=False)

df = pandas.read_csv(episode_path, low_memory=False, sep='\t', header=0)
df = df.drop(['seasonNumber'], axis=1)
df = df.drop(['episodeNumber'], axis=1)
df.columns = ['Econst', 'Season_Tconst']
df.to_sql("HAS_EPISODE", conn, if_exists='replace', index=False)

df = pandas.read_csv(ratings_path, low_memory=False, sep='\t', header=0)
df.columns = ['Tconst', 'Avg_rating', 'Num_votes']
df.to_sql("RATINGS", conn, if_exists="replace", index=False)
# TODO Remove NULL Nconst from HAS_DIRECTORS/WRITERS
df = pandas.read_csv(crew_path, low_memory=False, header=0)
df = df.drop(['writers'], axis=1)
df.columns = ['Tconst', 'Nconst']
df.to_sql("HAS_DIRECTORS", conn, if_exists="replace", index=False)

df = pandas.read_csv(crew_path, low_memory=False, header=0)
df = df.drop(['directors'], axis=1)
df.columns = ['Tconst', 'Nconst']
df.to_sql("HAS_WRITERS", conn, if_exists="replace", index=False)


df = pandas.read_csv(principle_path, low_memory=False, header=0)
df.columns = ['Tconst', 'Nconst']
df.to_sql("HAS_ACTORS", conn, if_exists="replace", index=False)


df = pandas.read_csv(kaggle_path, low_memory=False, header=0, error_bad_lines=False)
df = df.drop(['primaryTitle'], axis=1)
df = df.drop(['startYear'], axis=1)
df = df.drop(['director_name'], axis=1)
df = df.drop(['num_critic_for_reviews'], axis=1)
df = df.drop(['duration'], axis=1)
df = df.drop(['actor_2_name'], axis=1)
df = df.drop(['gross'], axis=1)
df = df.drop(['genres'], axis=1)
df = df.drop(['actor_1_name'], axis=1)
df = df.drop(['movie_title'], axis=1)
df = df.drop(['num_voted_users'], axis=1)
df = df.drop(['cast_total_facebook_likes'], axis=1)
df = df.drop(['actor_3_name'], axis=1)
df = df.drop(['plot_keywords'], axis=1)
df = df.drop(['movie_imdb_link'], axis = 1)
df = df.drop(['num_user_for_reviews'], axis=1)
df = df.drop(['title_year'], axis=1)
df = df.drop(['aspect_ratio'], axis=1)
df = df.drop(['Rank'], axis = 1)
df = df.drop(['Title'], axis=1)
df = df.drop(['Genre'], axis=1)
df = df.drop(['Description'], axis=1)
df = df.drop(['Actors'], axis=1)
df = df.drop(['Year'], axis=1)
df = df.drop(['Runtime (Minutes)'], axis=1)
df = df.drop(['Rating'], axis=1)
df = df.drop(['Votes'], axis=1)
df = df.drop(['Director'], axis=1)
df.columns = ['Tconst', 'Color', 'Director_Likes', 'Act_3_Likes','Act_1_Likes','Face_number', 'Language', 'Country', 'Content_rating', 'Budget', 'Act_2_Likes', 'User_Rating', 'FB_likes', 'Revenue', 'Critic_Rating']
df['Face_number'] = pandas.to_numeric(df['Face_number'], errors='coerce')
df['Budget'] = pandas.to_numeric(df['Budget'], errors='coerce')
df['FB_likes'] = pandas.to_numeric(df['FB_likes'], errors='coerce')
df['Director_Likes'] = pandas.to_numeric(df['Director_Likes'], errors='coerce')
df['Act_3_Likes'] = pandas.to_numeric(df['Act_3_Likes'], errors='coerce')
df['Act_1_Likes'] = pandas.to_numeric(df['Act_1_Likes'], errors='coerce')
df['Act_2_Likes'] = pandas.to_numeric(df['Act_2_Likes'], errors='coerce')
df['User_Rating'] = pandas.to_numeric(df['User_Rating'], errors = 'coerce')
df.to_sql("MOVIE", conn, if_exists="replace", index=False)

conn.close()
