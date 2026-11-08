import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data= pd.DataFrame({
    "x":[1,2,3,4],
    "y":[5,10,7,15]
    })
print(data.head())

#_______Annotation_______


plt.figure(figsize=(6,4))
plt.plot(data["x"],data["y"],marker="o")
plt.annotate("Lowest",
             xy=(1,5),
             xytext=(1.5,6),
             arrowprops=dict(facecolor="black"))

plt.show()

#_______________
