import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#한글 폰트 적용
import matplotlib.font_manager as fm

# 파일 불러오기
df = pd.read_csv('./hospital.csv', encoding='cp949')

# 한글 폰트 설정
font_path = './NanumGothic.ttf'  # 한글 폰트 파일 경로
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())

# 의료센터별 갯수 구하기
center_values = df['업무구분명'].value_counts()

# 의료센터별 갯수 파이차트로 나타내기
labels = center_values.index.tolist()
labels = [label.encode('cp949').decode('cp949') for label in labels]
counts = center_values.values

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontproperties': fontprop})
ax.axis('equal')  # 원형 모양 유지
ax.set_title('기관구분별 분포',fontproperties=fontprop)
st.pyplot(fig)


# 소재지도로명주소 문자열 분리
df['소재지도로명주소'].str.split(" ")

# 소재지도로명주소 시,군 단위 문자 추출
df['소재지'] = df['소재지도로명주소'].str.split(" ", expand=True)[1]
df.head(3)

# 소재지별 의료기관 업무구분 분류
df_center = df.copy()
df_center = df_center.groupby(['소재지', '업무구분명']).count()
df_center = df_center.pivot_table(index=['소재지', '업무구분명'], values=['병원명/센터명'])
df_center = df_center.iloc[:, :1]

# 인덱스 재설정
df_center.reset_index()

# 소재지별 의료기관 업무구분 bar차트
fig = px.bar(df_center.reset_index(), x='소재지', y='병원명/센터명', color='업무구분명')
fig.update_layout(
    title='의료기관별 소재지 및 업무구분',
    font=dict(color='black')
)
colors = ['red', 'blue', 'green', 'purple']
for i, bar in enumerate(fig.data):
    bar.marker.color = colors[i % len(colors)]

st.plotly_chart(fig)
