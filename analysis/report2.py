import pandas as pd

data = pd.read_csv("output/input.csv")

fig2 = data.imd3.plot.hist().get_figure()
fig2.savefig("output/descriptive2.png")