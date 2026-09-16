def second_highest_avg_suburb(listings):

    counts = {}
    prices = {}

    for listing in listings:
        suburb = listing ["suburb"]
        price = listing.get("price", 0)

        prices [suburb] =  prices.get(suburb, 0) + price
        counts [suburb] =  counts.get(suburb, 0) + 1

    averages = {}

    for suburb in prices:

        averages [suburb] = prices [suburb] / counts [suburb]

    sorted_values = sorted (averages.values() , reverse= True)

    if len(sorted_values) <2:
        return None
    
    Second_highest = sorted_values [1]

    for suburb, ave in averages.items():

        if ave == Second_highest:
            return suburb
        


#Test


listings = [
    {"suburb": "Richmond", "price": 850000},
    {"suburb": "Richmond", "price": 900000},
    {"suburb": "Fitzroy", "price": 1200000},
    {"suburb": "Fitzroy", "price": 1100000},
    {"suburb": "Carlton", "price": 700000},
    {"suburb": "Carlton", "price": 750000},
]

print (second_highest_avg_suburb(listings))


