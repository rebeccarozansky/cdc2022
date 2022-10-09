import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100

df = pd.read_csv("data6.csv")

data = np.concatenate((spread, center, flier_high, flier_low))

labels = ("Original Tweet", 'Average of Account')


fig1, ax1 = plt.subplots()
ax1.set_title('Original Tweet vs. Average Sentiment of Account')
ax1.boxplot([df["Original"],df["Average"]])
plt.xticks(np.arange(len(labels))+1,labels)
ax1.set_ylabel('Sentiment Value')

plt.show()
