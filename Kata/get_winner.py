from collections import Counter

def get_winner(ballots):
  res = Counter(ballots)
  for candidate, count in res.most_common(1):
    if count > len(ballots)/2:
      return candidate

print(get_winner(["A", "A", "A", "B", "B"]))