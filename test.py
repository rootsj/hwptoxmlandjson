import collections

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(collections.Counter(participant))
print(collections.Counter(completion))
print(collections.Counter(participant) - collections.Counter(completion))