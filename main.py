from fuzzywuzzy import fuzz

print(fuzz.ratio("Nigel is him", "him is Nigel"))
