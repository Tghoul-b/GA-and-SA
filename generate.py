import numpy as np
with open ('./data/data4.txt','w') as f:
    for i in range(1000):
        x=np.random.randint(100)
        y=np.random.randint(100)
        f.write(str(x))
        f.write(' ')
        f.write(str(y))
        f.write('\n')