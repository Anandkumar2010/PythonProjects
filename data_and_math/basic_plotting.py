import matplotlib.pyplot as plt

x = [2010, 2020 , 2025]
y1 = [230 , 360 , 390  ]
y3 = [90 , 130 , 240]
y4 = [380, 470, 670]
line_style = dict(marker="o",
             markersize=15,
             markerfacecolor="yellow",
             markeredgecolor="orange",
             linestyle="solid",
             linewidth=3,
         )
plt.title("Class Size", fontsize=27, family="arial", fontweight="bold", color="red")
plt.xlabel("Year", fontsize=20, family="arial", fontweight="bold", color="darkblue")
plt.ylabel("Students", fontsize=20, family="arial", fontweight="bold", color="darkblue")

plt.plot(x,y1,color="blue",**line_style)
plt.plot(x,y3,color="violet",**line_style)
plt.plot(x,y4,color="purple", **line_style)


plt.show()
