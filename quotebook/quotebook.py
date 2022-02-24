import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json("https://quotebook-dd68d-default-rtdb.asia-southeast1.firebasedatabase.app/quotes.json")
df.citation = df.citation.apply(lambda s: " ".join(s.lower().replace("also ", "").split(" ")[:2]).strip(",").replace("prannaya", "prannay").replace(".", "").strip().replace("i-shiang", "bobby").replace("i-shang", "bobby").title().replace("Oh Zhi", "Ozy").replace("Markys", "Markus").replace("Vikeam", "Vikram"))
plt.figure(figsize=(16, 8))
sns.countplot(y=df.citation, order=df.citation.value_counts().index)
plt.show()
