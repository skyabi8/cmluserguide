import os
os.system("pip install pandas")

import pandas as pd
import random
import string

list_1 = [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(10)]
list_2 = [random.randint(1, 100) for _ in range(10)]

data = {'Column_1': list_1, 'Column_2': list_2}
df = pd.DataFrame(data)

print(df)