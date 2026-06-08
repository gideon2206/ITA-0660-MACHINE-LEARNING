sales = [1000, 1200, 1400, 1600]

growth = (sales[-1] - sales[0]) / (len(sales)-1)

future_sale = sales[-1] + growth

print("Predicted Future Sales =", future_sale)
