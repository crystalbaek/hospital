import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('./hospital.csv', encoding='cp949')


df['소재지도로명주소'].str.split(" ")
df['시군'] = df['소재지도로명주소'].str.split(" ", expand=True)[1]

center_values = df['업무구분명'].value_counts()
labels = center_values.index
counts = center_values.values

# 파이차트 그리기
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # 원형 모양 유지
plt.title('기관구분별 분포')
plt.show()

