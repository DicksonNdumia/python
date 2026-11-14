import random
from collections import defaultdict

text = "i love coding i love python i love ai coding is fun ai is powerful"

words = text.split()
print(words)

# build "what comes next" map
model = defaultdict(list)


for i in range(len(words) - 1):
    model[words[i]].append(words[i + 1])

# generate text
current = "i"
output = [current]

for _ in range(10):
    next_words = model.get(current, None)
    if not next_words:
        break
    current = random.choice(next_words)
    output.append(current)

print(" ".join(output))
