
def dedup_most_recent(listings):

    best_by_address = {}

    for listing in listings:
        address = listing["address"]

        if address not in best_by_address:
            best_by_address[address] = listing

        elif listing ["listed_date"] > best_by_address[address]["listed_date"]:
            best_by_address[address] = listing

    return list (best_by_address.values())




#Test

listings = [
    {"address": "12 Smith St", "price": 800000, "listed_date": "2026-01-10"},
    {"address": "5 Jones Ave", "price": 650000, "listed_date": "2026-02-01"},
    {"address": "12 Smith St", "price": 820000, "listed_date": "2026-03-15"},  # re-listed, newer
    {"address": "5 Jones Ave", "price": 640000, "listed_date": "2026-01-20"},  # older, should be dropped
]

print (dedup_most_recent(listings))
