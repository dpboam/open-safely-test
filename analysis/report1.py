import pandas as pd

data = pd.read_csv("output/input.csv")

fig1 = data.imd2.plot.hist().get_figure()
fig1.savefig("output/descriptive1.png")