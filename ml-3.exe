data = [
['Sunny','Hot','High','Weak','No'],
['Sunny','Hot','High','Strong','No'],
['Overcast','Hot','High','Weak','Yes'],
['Rain','Mild','High','Weak','Yes'],
['Rain','Cool','Normal','Weak','Yes'],
['Rain','Cool','Normal','Strong','No'],
['Overcast','Cool','Normal','Strong','Yes'],
['Sunny','Mild','High','Weak','No'],
['Sunny','Cool','Normal','Weak','Yes'],
['Rain','Mild','Normal','Weak','Yes']
]

print("Decision Tree (ID3)")
print()

print("Outlook")
print("├── Overcast → Yes")
print("├── Sunny")
print("│   ├── High Humidity → No")
print("│   └── Normal Humidity → Yes")
print("└── Rain")
print("    ├── Strong Wind → No")
print("    └── Weak Wind → Yes")

# New Sample
outlook = "Sunny"
humidity = "Normal"

if outlook == "Overcast":
    result = "Yes"
elif outlook == "Sunny":
    if humidity == "High":
        result = "No"
    else:
        result = "Yes"
else:
    result = "Yes"

print("\nPrediction:", result)
