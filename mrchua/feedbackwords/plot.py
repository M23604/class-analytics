import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Retrieval
arr = np.array(sorted(np.loadtxt("data.txt", dtype=int), key=lambda x:x[0]))

# Figure 1: Ordered by Class Register Number
fig, ax = plt.subplots(2, 2, figsize=(16, 16))
sns.regplot(arr[:, 0], arr[:, 1:].sum(axis=1), ax=ax[0, 0]).set(title="Total Sum")
sns.regplot(arr[:, 0], arr[:, 1], ax=ax[0, 1]).set(title="Insights")
sns.regplot(arr[:, 0], arr[:, 2], ax=ax[1, 0]).set(title="Application of ML")
sns.regplot(arr[:, 0], arr[:, 3], ax=ax[1, 1]).set(title="Evaluation")
plt.suptitle("Ordered by Class Register Number")

# Figure 2: Ordered by CS Register Number
fig, ax = plt.subplots(2, 2, figsize=(16, 16))
fakeX = np.arange(1,arr.shape[0]+1)
sns.regplot(fakeX, arr[:, 1:].sum(axis=1), ax=ax[0, 0]).set(title="Total Sum")
sns.regplot(fakeX, arr[:, 1], ax=ax[0, 1]).set(title="Insights")
sns.regplot(fakeX, arr[:, 2], ax=ax[1, 0]).set(title="Application of ML")
sns.regplot(fakeX, arr[:, 3], ax=ax[1, 1]).set(title="Evaluation")
plt.suptitle("Ordered by CS Register Number")

# Plot
plt.show()

