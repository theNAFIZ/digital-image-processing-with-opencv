import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

url = 'https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=12;type=trophy'
html = pd.read_html(url)

df = pd.DataFrame(html[0])

# Country Extract from player name
def country_def(name):
  spl = name.split("(")
  spl = spl[1].split(")")
  # print(spl[0])
  return spl[0]

# Push country column to DataFrame
p = []
for i in range(len(df)):
  p.append(country_def(df['Player'][i]))
df["Country"] = p

st.write(df)

plt.fill_between(df.Mat, df.Runs, color="skyblue", alpha=0.3)
plt.plot(df.Mat, df.Runs, color='skyblue', alpha=0.8)
plt.xticks(rotation=90)

plt.show()