import random

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']

min_len = min(len(boys), len(girls))

results = [(random.sample(boys, 1)[0], random.sample(girls, 1)[0]) for _ in range(min_len)]

print("نتایج ازدواج:")
for result in results:
    print(result)
