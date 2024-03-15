# -*- coding: utf-8 -*-
"""scalar visualization

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vn0zgylxvEv1TPvrK1a67wvx-om_i8uy
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

data=pd.DataFrame({
    "x":np.random.rand(100),
    "y":np.random.rand(100),
    "value":np.random.rand(100)
    })

cmap="viridis"
alpha=1

plt.figure(figsize=(6,6))
plt.scatter(data["x"],data["y"],c=data["value"],cmap=cmap,alpha=alpha)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatterplot with Colormap")
plt.colorbar(label="value")
plt.show()

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

data=pd.DataFrame(np.random.rand(10,10))

plt.figure(figsize=(8,6))
plt.contour(data.values)
plt.show()

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

data=pd.DataFrame(np.random.rand(10,10))

x=np.arange(data.shape[0])
y=np.arange(data.shape[1])
x,y=np.meshgrid(x,y)

fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,data.values,cmap='viridis')