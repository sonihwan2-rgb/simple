


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

# 사인 곡선이 사용되는 실생활 분야 예시를 토글로 제시
with st.expander('사인 곡선이 사용되는 실생활 분야'):
	st.markdown('''
**1.  음파 및 소리**
사인 곡선은 소리의 파형, 음악 신호 등에서 기본적으로 사용됩니다.
''')
	memo1 = st.text_area('메모 남기기 (음파 및 소리)', key='memo1')
	st.markdown('''

**2.  전기 신호**
교류(AC) 전류의 파형은 사인 곡선 형태입니다.
''')
	memo2 = st.text_area('메모 남기기 (전기 신호)', key='memo2')
	st.markdown('''

**3.  진동 및 파동**
진자 운동, 스프링의 진동, 물결 등 다양한 물리적 진동 현상에서 사인 곡선이 나타납니다.
''')
	memo3 = st.text_area('메모 남기기 (진동 및 파동)', key='memo3')
	st.markdown('''

**4.  이미지 및 신호 처리**
주기적 신호 분석, 필터 설계 등에서 사인 곡선이 활용됩니다.
''')
	memo4 = st.text_area('메모 남기기 (이미지 및 신호 처리)', key='memo4')
	st.markdown('''

**5.  기상 데이터**
일교차, 계절 변화 등 주기적 자연 현상 분석에도 사용됩니다.
''')
	memo5 = st.text_area('메모 남기기 (기상 데이터)', key='memo5')

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
