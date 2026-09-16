
def count_features(listings):

    final_features_count = {}


    for listing in listings:

        features = listing ["features"]

        for each in features:

            final_features_count[each] = final_features_count.get(each, 0)+1

    return final_features_count



# test

listings = [
    {"address": "12 Smith St", "features": ["pool", "garage"]},
    {"address": "5 Jones Ave", "features": ["garage", "solar"]},
    {"address": "8 King Rd", "features": ["pool", "solar", "garage"]},
    {"address": "3 Queen St", "features": ["pool"]},
]

print (count_features(listings))