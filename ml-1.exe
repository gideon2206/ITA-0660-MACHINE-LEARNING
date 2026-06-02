# FIND-S Algorithm

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initialize hypothesis
hypothesis = data[0][:-1]

print("Initial Hypothesis:")
print(hypothesis)

for example in data:
    if example[-1] == 'Yes':
        for i in range(len(hypothesis)):
            if hypothesis[i] != example[i]:
                hypothesis[i] = '?'

print("\nFinal Hypothesis:")
print(hypothesis)
