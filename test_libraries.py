import numpy as np
import pandas as pd
numbers=np.array([10,20,30,40,50])
print("Numpy array:",numbers)
print("sum:",np.sum(numbers))

data={
    "Name":["Ravi","sita","Mammu"],
    "Marks":[85,90,95]
}
df=pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)