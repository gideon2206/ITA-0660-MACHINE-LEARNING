actual =    ['Yes','No','Yes','Yes','No']
predicted = ['Yes','No','Yes','No','No']

tp = tn = fp = fn = 0

for a, p in zip(actual, predicted):
    if a == 'Yes' and p == 'Yes':
        tp += 1
    elif a == 'No' and p == 'No':
        tn += 1
    elif a == 'No' and p == 'Yes':
        fp += 1
    elif a == 'Yes' and p == 'No':
        fn += 1

print("Confusion Matrix")
print("[[", tp, fp, "],")
print(" [", fn, tn, "]]")

accuracy = ((tp + tn) / len(actual)) * 100

print("\nAccuracy =", accuracy, "%")
