import csv
import sqlite3
dBase = "database.db"
conn = sqlite3.connect("database.db")

result1 = conn.execute("SELECT mov.Budget, mov.Nconst, history.Nconst, mov.User_Rating, mov.Tconst, history.Tconst, history.User_Rating from (SELECT M.User_Rating, H.Nconst, M.Tconst, M.Budget FROM  MOVIE as M, HAS_DIRECTORS as H WHERE M.Tconst = H.Tconst and H.Nconst NOT LIKE \"\\N\") as  mov JOIN (SELECT H.Nconst, M.Tconst, M.User_Rating FROM  MOVIE as M, HAS_DIRECTORS as H WHERE M.Tconst = H.Tconst and H.Nconst NOT LIKE \"\\N\") as history on history.Nconst = mov.Nconst ORDER BY mov.Nconst;")

with open('question1.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result1.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)

result2 = conn.execute("SELECT M.Act_1_Likes, M.Act_2_Likes, M.Act_3_Likes, M.Face_number, M.Revenue FROM MOVIE as M WHERE Act_3_Likes and Act_2_Likes and Act_1_Likes and Revenue and Face_number is not null;")

with open('question2.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result2.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)

result3 = conn.execute("SELECT M.User_Rating, M.Critic_Rating, M.Revenue FROM MOVIE as M WHERE User_Rating and Critic_Rating and Revenue is not null;")

with open('question3.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result3.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)

result4 = conn.execute("SELECT M.Act_1_Likes, M.Act_2_Likes, M.Act_3_Likes, M.Director_Likes, M.Revenue, M.Budget FROM MOVIE as M WHERE Revenue and Act_1_Likes and Act_2_Likes and Act_3_Likes is NOT NULL ;")
with open('question4.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result4.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)
result5 = conn.execute("SELECT epi.Rating, sea.SeasonR, epi.Econst, sea.Tconst from( SELECT E.Econst, S.Tconst as SeasonT, R.Avg_Rating as Rating FROM  EPISODE as E, SEASON as S, HAS_EPISODE as H, RATINGS as R WHERE E.Econst = H.Econst and S.Tconst = H.Season_Tconst and E.Econst = R.Tconst ) as epi JOIN ( SELECT S.Tconst, R.Avg_Rating as SeasonR FROM SEASON as S, RATINGS as R WHERE S.Tconst = R.Tconst ) as sea on epi.SeasonT = sea.Tconst ORDER BY sea.Tconst;")

with open('question5.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result5.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)
conn.close()