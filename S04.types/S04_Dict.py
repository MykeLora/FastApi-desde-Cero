def process_items(prices: dict[str,float]):
    for item_name,item_price in prices.items():
        print(item_name,item_price)

process_items({'Mause gaming': 2500.50})            