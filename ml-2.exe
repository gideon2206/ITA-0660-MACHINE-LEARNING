concepts = [
['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
['Sunny','Warm','High','Strong','Warm','Same','Yes'],
['Rainy','Cold','High','Strong','Warm','Change','No'],
['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

specific_h = concepts[0][:-1]
general_h = [['?' for i in range(len(specific_h))]
             for i in range(len(specific_h))]

for h in concepts:

    if h[-1] == "Yes":
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                specific_h[x] = '?'
                general_h[x][x] = '?'

    elif h[-1] == "No":
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                general_h[x][x] = specific_h[x]
            else:
                general_h[x][x] = '?'

print("Specific Hypothesis:")
print(specific_h)

print("\nGeneral Hypothesis:")
for g in general_h:
    print(g)
