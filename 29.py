# what is series in pandas

#  Pandas Series is like a column in a table.

#   It is a one-dimensional array holding data of any type.

#exp

import pandas as pd

dict1 = {
    "name": ["Nafees", "Ahmad", "Ezsnippet"],
    "marks": [92, 94, 91],
    "country": ["Pakistan", "Germany", "India"]
}

s1 = pd.Series(dict1)
print(s1)
