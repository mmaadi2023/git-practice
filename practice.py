def average_price_by_suburb(listings):
    """
    listings: list of dicts, each like:
        {"suburb": "Richmond", "price": 850000}
    Returns: dict of {suburb: average_price}
    """
    totals = {}
    counts = {}

    for listing in listings:
        suburb = listing["suburb"]
        price = listing.get("price")

        if price is not None and price > 0:
            totals[suburb] = totals.get(suburb, 0) + price
            counts[suburb] = counts.get(suburb, 0) + 1

    averages = {}
    for suburb in totals:
        averages[suburb] = totals[suburb] / counts[suburb]

    return averages


listings = [
    {"suburb": "Richmond", "price": 850000},
    {"suburb": "Richmond", "price": None},
    {"suburb": "Fitzroy", "price": -100},
    {"suburb": "Fitzroy", "price": 900000},
]

result = average_price_by_suburb(listings)
print(result)