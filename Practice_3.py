def rolling_average(data, window):

    num = len(data) - window + 1

    rollings = []

    for n in range (num):
        chunk = data [n:n+window]
        ave = sum(chunck)/window
        rollings.append(rolling)

    return rollings

#TESt
daily_counts = [10, 12, 8, 15, 20, 18, 14, 16, 22, 19]

print (rolling_average(daily_counts, window = 3))

