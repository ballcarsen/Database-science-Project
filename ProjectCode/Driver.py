#Carsen Ball, Kirby Overman
#Data base, data science code for project
#12/4/17
from ProjectCode import question1, question2, question3, question4, question5
#import mysql.connector as mc
import csv
#Configure the data base connnection
'''
config = {
    'user' : 'root',
    'password' : 'sqlpass',
    'host' : '127.0.0.1',
    'database' : 'imbd',
    'raise_on_warnings' : True
}

conn = mc.connect(**config)
cursor = conn.cursor()

#Queries question1, creates CSV
result1 = cursor.execute(
    """SELECT m.budget, hc.person, sub.person, r.average_rating, m.production_production_index, sub.id, sub.average_rating 
            FROM movie m 
            JOIN has_crew hc ON m.production_production_index=hc.p_id 
            JOIN rating r ON m.production_production_index=r.production_production_index 
            JOIN (SELECT crew.person AS 'person', mov.production_production_index AS 'id', ra.average_rating AS 'average_rating' 
            FROM movie mov 
            JOIN has_crew crew ON mov.production_production_index=crew.p_id 
            JOIN rating ra ON mov.production_production_index=ra.production_production_index) sub 
            ON m.production_production_index=sub.id 
            WHERE hc.role LIKE 'Director';""")

with open('question1.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result1.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)

#Queries question2
result2 = cursor.execute("""SELECT sub1.a1, sub2.a2, sub3.a3, m.num_faces_in_poster, m.revenue
        FROM movie m
        JOIN has_crew hc ON m.production_production_index=hc.p_id
        JOIN
        (SELECT p.fb_likes AS a1, p.person_id AS person
        FROM person p LIMIT 1) sub1 ON hc.person=sub1.person
        JOIN
        (SELECT p.fb_likes AS a2, p.person_id AS person
        FROM person p LIMIT 1) sub2 ON hc.person=sub1.person
        JOIN
        (SELECT p.fb_likes AS a3, p.person_id AS person
        FROM person p LIMIT 1) sub3 ON hc.person=sub1.person;""")

#Writes a csv for question 2
with open('question2.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result2.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)

#Queries question 3
result3 = cursor.execute("""SELECT r.imbd_score, r.meta_score, m.revenue
                    FROM ratings r 
                    JOIN movie m ON r.production_production_index=m.production_production_index;""")

#Writes a csv for question 3
with open('question3.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result3.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)

#Queries question 4
result4 = cursor.execute("""SELECT sub1.a1, sub2.a2, sub3.a3, m.num_faces_in_poster, m.revenue, m.budget
        FROM movie m
        JOIN has_crew hc ON m.production_production_index=hc.p_id
        JOIN
        (SELECT p.fb_likes AS a1, p.person_id AS person
        FROM person p LIMIT 1) sub1 ON hc.person=sub1.person
        JOIN
        (SELECT p.fb_likes AS a2, p.person_id AS person
        FROM person p LIMIT 1) sub2 ON hc.person=sub1.person
        JOIN
        (SELECT p.fb_likes AS a3, p.person_id AS person
        FROM person p LIMIT 1) sub3 ON hc.person=sub1.person;""")

#Writes question 4
with open('question4.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result1.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)

#Queries question 5
result5 = cursor.execute("""Select Epi.rating, S.rating
    From
    ((Select T.tv_show_id AS tv_show, R.average_rating AS rating
    From rating as r, tv_show as T
    Where T.production_production_index = R.production_production_index) as S
    Join
    (Select E.rating, E.tv_show_tv_show_id AS tv_id
    From episode as E) as Epi
    on Epi.tv_id = S.tv_show)
    Where Epi.rating is not null and S.rating is not null;""")

#Writes question 5
with open('question5.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in result5.fetchall():
        i = list(i)
        print(i)
        write.writerow(i)
'''
#question1.run()
question2.run()
question3.run()
#question4.run()
#question5.run()