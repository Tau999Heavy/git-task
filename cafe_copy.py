menu = ["Coffee", "Rooibos", "Pie", "Quiche"]

stock_dict = {"Coffee" : 30,
              "Rooibos" : 45,
              "Pie" : 11,
              "Quiche" : 22}


price_dict = {"Coffee" : 17,
              "Rooibos" : 14,
              "Pie" : 30,
              "Quiche" : 30}

total_stock = 0

for item in menu:
   product_value = (stock_dict[item] * price_dict [item])
   total_stock += product_value

print(f"Your total stock is worth {total_stock} Rand")


