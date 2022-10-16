# SQL Challenges

For all those challenges, I decided not to use SQL queries to solve them but only operations with the sql file using python.

## Counting Heads

For this challenge we are provided a .sql file containing table creation and values insertion to the tables.

We are asked to find the number of users contained in this database.

We can notice that at line 390 the user values are pushed to the `users` table.

We just have to count the number of opening parenthesis in this line to know how many users were added to the db.

The answer here is 2400.

(see extract_nb_players.py for source code)

## The Faculty

For the same database, we are asked the number of users that are not students.

We can notice at line 233 that the id for the role `Student` is 1 : </br> ```INSERT INTO `roles` VALUES (5,'Adjunct Professor'),(8,'Administration'),(4,'Associate Professor'),(2,'Instructor'),(3,'Professor'),(6,'Research Assistant'),(7,'Research Associate'),(1,'Student');```

We can also notice a table `roles_assigned` handles the assignments between roles and users.

The values for this table are pushed line 262 with the following syntax : `(assignment_id, user_id, role_id)`

With a python script we just have to count the number of values that don't end with the value 1 (which means that they are not students).

The python script is available (extract_nb_not_students.py).

The answer is 627

## Let's hash it out !

This challenge is a bit different from the others !

Here we are asked to find which user from the database is being targeted by DEADFACE, a hint is given to look at Ghost Twon (DEADFACE's social medium).

This challenge will then mix SQL and OSINT considerations.

First we extract the usernames (it would have worked if we had extracted emails too) of all the users of the database and write them to a file (using extract_usernames.py for the line containing user values).

Then we will use the scrapper (the way the scrapper works is discussed in OSINT section) I developped that will crawl Ghost Town's articles, extract raw HTML and will try to find some keywords in those articles.

The keywords we will use here are the usernames we have extracted from the database.

My scraper tells me he found the username `nikia.manderfield` at the following url : [Ghost Town Article](https://ghosttown.deadface.io/t/ready-set-go/50)

And that's what we are looking for ! The hackers give a list of emails of tagetted users including `nikia.manderfield@easternstateuniversity.com`, which is the email for the user `nikia.manderfield`.

We go back to the sql file, find the id of the user (using the same line we used to extract usernames) : `1440`.

We then go to line 156 where the passwords values are pushed, and we find the hash of this user's password : `b487af41779cffb9572b982e1a0bf83f0eafbe05`.

## Fall Classes

Here we are asked how many unique Fall classes exist in this database.

First we can notice a table which name is `term_courses`, this table conatins the terms associated with a given course.

One of those list of terms contains `FALL2022`, `2022-08-01`, `2022-11-25` and `Fall semester 2022`, I considered that these terms were refering to Fall classes. The id of theese keywords is 2 (can be found line 352).

The values of the `term_courses` table are pushed at line 324, the format is `(term_courses_id, course_id, term_id, instructor)`.

We are interseted in the unique values of `course_id` and `term_id` where `term_id` equals 2.

With the python script extract_fall_courses.py, we can find the answer : 405