import pandas as pd

data = pd.read_csv("output/input.csv")

fig = data.imd1.plot.hist().get_figure()
fig.savefig("output/descriptive.png")

