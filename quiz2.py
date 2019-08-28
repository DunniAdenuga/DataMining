import os
import time
from operator import itemgetter

movies = {}
users = {}

ratings = {} # keeps track of number of ratings
ratings1 = {} # keeps track of sum of ratings


# the most number of ratings and best rating
# check if rating was made in date range
# key - movieId
# just update 2 dictionaries (movieID, count of ratings) and (movieID, sum of ratings)

movieFile = open(os.path.join('./Archive2/', 'movies.dat'), 'r')
movieLines = movieFile.readlines()
for line in movieLines:
    stripResult = line.split('::')
    movies[stripResult[0]] = stripResult[1]

movieFile.close()

ratingsFile = open(os.path.join('./Archive2/', 'ratings.dat'), 'r')
ratingsLines = ratingsFile.readlines()
for line in ratingsLines:
    stripLine = line.split('::')
    ratingTime = time.localtime(stripLine[3])
    if(ratingTime.tm_year == 2000) and (ratingTime.tm_mon == 8 or ratingTime.tm_mon == 9):
        if stripLine[1] in ratings:
            ratings[stripLine[1]] = ratings[stripLine[1]] + 1
            ratings1[stripLine[1]] = ratings[stripLine[1]] + stripLine[2]
        else:
            ratings[stripLine[1]] = 1
            ratings1[stripLine[1]] = stripLine[2]
ratingsFile.close()

mostRatingsSorted = sorted(ratings.items(), key=itemgetter(1), reverse=True)
bestRatingsSorted = sorted(ratings1.items(), key=itemgetter(1), reverse=True)

i = 0
j = 0

print("Top 10 Movies with Most Ratings: " + '\n')
while i < 10:
    print(movies[mostRatingsSorted[i][0]])
    print('\n')
    i = i + 1

print("Top 10 Movies with Best Ratings: " + '\n')
while j < 10:
    print(movies[bestRatingsSorted[i][0]])
    print('\n')
    j = j + 1
