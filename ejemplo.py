import numpy as np
f = open("data.csv","w")
c = np.random.uniform(10, 15, 300)
text = str(list(c))
print(text)
f.write(text)
