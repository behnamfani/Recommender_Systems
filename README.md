# Recommender_Systems
Use collaborative filtering to recommend TV shows

## Description
Recommender systems suggest personalized items to users. There are two main types:
* Collaborative Filtering:
  * User-Based: Recommends items based on similar users' preferences.
  * Item-Based: Recommends items similar to those the user has interacted with.
* Content-Based Filtering:
Recommends items based on their features and matches them to a user's profile. It's less affected by the "cold start" problem but may miss unexpected preferences.

In this project, given a dataset of various TV shows and a user-item matrix, the top 10 TV shows are recommended to the *user 500* using both user-user and item-item collaborative filtering.

## Dataset
matrix.txt consists of a user-item matrix with 9985 users and 563 shows where element_{ij} means the user 1 likes show j. items.txt file includes the name of the shows with the same order as the columns of the mentioned matrix.

# Results

Top 10 most popular TV shows:
Rank | Show | Likes
-----|------|------
1 | ”Family Guy” | 5361
2 | ”FOX 28 News at 10pm” | 5301
3 | ”2009 NCAA Basketball Tournament” | 4849
4 | ”NBC 4 at Eleven” | 4553
5 | ”Two and a Half Men” | 4442
6 | ”Everybody Loves Raymond” | 4271
7 | ”Today” | 4267
8 | ”Access Hollywood” | 4254
9 | Law & Order: Special Victims Unit” | 4122
10|  ”NBC 4 Today ” | 4083

Top 10 TV recommended shows based on *user-user collaborative filtering*:
Rank | Show | Similar Users’ likes
-----|------|------
1 | ”CSI: NY” | 32
2 | ”2009 NCAA Basketball Tournament” | 32
3 | ”NBC 4 at Eleven” | 30
4 | ”FOX 28 News at 10pm” | 28
5 | ”CBS Evening News” | 28
6 | ”Wow Wow Wubbzy” | 24
7 | ”NCIS” | 24
8 | ”Today” | 23
9 | ”Law & Order: Special Victims Unit” | 23
10 | ”Family Guy” | 23


Top 10 TV recommended shows based on *item-item collaborative filtering*:
Rank | Show | Similar Item’ scores
-----|------|------
1 | ”FOX 28 News at 10pm” | 43
2 | ”Access Hollywood” | 37
3 | ”Family Guy” | 36
4 | ”Today” | 34
5 | ”NBC 4 at Eleven” | 33
6 | ”Everybody Loves Raymond” | 33
7 | ”2009 NCAA Basketball Tournament” | 32
8 | ”American Idol” | 30
9 | ”Two and a Half Men” | 30
10 | ”Law & Order: Special Victims Unit” | 29
