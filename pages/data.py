


import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

font_path = './font/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)

st.title('간단한 자료 시각화 예시')

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# matplotlib 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label='sin(x)')
ax.set_title('간단한 사인 곡선 시각화', fontproperties=fontprop)
ax.set_xlabel('x', fontproperties=fontprop)
ax.set_ylabel('sin(x)', fontproperties=fontprop)
ax.legend(prop=fontprop)
ax.grid(True)

# 한글 폰트 전체 적용 (tick label 등)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontproperties(fontprop)

# Streamlit에 그래프 표시
st.pyplot(fig)

st.title('간단한 자료 시각화 예시')

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# matplotlib 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label='sin(x)')
ax.set_title('간단한 사인 곡선 시각화')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.legend()
ax.grid(True)

# Streamlit에 그래프 표시
st.pyplot(fig)
