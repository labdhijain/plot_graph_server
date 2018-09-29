#!/usr/bin/python

import matplotlib.pyplot as plt
import mpld3

data=['apple','banana','guava','grapes']
price=[180,30,90,60]


plt.xlabel("fruits")
plt.ylabel("price per kg")
plt.plot(data,price,label="market vlues of fruits")
plt.bar(data,price)
plt.legend()


mpld3.show()
