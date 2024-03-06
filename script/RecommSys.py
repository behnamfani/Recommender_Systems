import numpy as np

thresh_user = 0.4
thresh_item = 0.3


def popular(data, item):
    # We need the sum of each of the first 100 columns and the finding the top 10
    sum = np.zeros(100)
    for j in range(100):
        sum[j] = np.sum(data[:, j])
    sort = np.argsort(sum)
    print('Top 10 most popular TV shows')
    for j, i in enumerate(sort[:len(sort) - 11:-1]):
        print(j + 1, '. ', item[i], '--> likes = ', int(sum[i]))
    print()


def user_user(data, item):
    global thresh_user
    target = data[499, :]
    sim = []
    # Computing cos_similarity between target and its neighbors. If the similarity >= threshold --> add it to sim array
    for j, i in enumerate(data):
        cos_sim = np.dot(target, i)/(np.linalg.norm(target)*np.linalg.norm(i))
        if cos_sim >= thresh_user and j != 499:
            sim.append(j)
    # We add the scores of similar users and sort them to find top 10 TV shows
    sum = np.zeros(100)
    for i in sim:
        sum = sum + data[i, :100]
    sort = np.argsort(sum)
    print('Top 10 TV shows based on user-user collaborative filtering')
    for j, i in enumerate(sort[:len(sort) - 11:-1]):
        print(j + 1, '. ', item[i], '--> Similar Users\' likes = ', int(sum[i]))
    print()


def item_item(data, item):
    global thresh_item
    sum = np.zeros(100)
    for k in range(100):
        # Computing cos_similarity between target (item k) and its neighbors. If the similarity >= threshold --> add it
        # to sim array
        target = data[:, k]
        sim = []
        for j in range(100, len(item)):
            i = data[:, j]
            cos_sim = np.dot(target, i) / (np.linalg.norm(target) * np.linalg.norm(i))
            if cos_sim >= thresh_item:
                sim.append(j)
        # We add the scores of similar item for user 500
        s = 0
        for i in sim:
            s = s + data[499, i]
        sum[k] = s
    # sort them sums of scores to find top 10 TV shows
    sort = np.argsort(sum)
    print('Top 10 TV shows based on item-item collaborative filtering')
    for j, i in enumerate(sort[:len(sort) - 11:-1]):
        print(j + 1, '. ', item[i], '--> Similar Item\' scores = ', int(sum[i]))
    print()


# Reading data
a = []
# user-item matrix
file1 = open('matrix.txt', 'r')
for line in file1:
    array = line.split()
    a.append(array)

a = np.array(a)
data = a.astype(np.float)

# items
item = []
file2 = open('items.txt', 'r')
for line in file2:
    l = line.replace("\n", "")
    item.append(l)

# 10 popular item
popular(data, item)
# User-user collaborative filtering
user_user(data, item)
# Item-item collaborative filtering
item_item(data, item)
