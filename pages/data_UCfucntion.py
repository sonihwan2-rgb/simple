import matplotlib.font_manager as fm
font_path = './font/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.text_area(
		'함수 입력 예시 (파이썬 문법)',
		'''
예시)
	x**2 + 2*x : x**2는 $x^2$ (x의 제곱)을 의미합니다.
		np.sin(np.pi*x) : np.sin은 sin 함수, np.pi는 $\pi$를 의미합니다.
		np.exp(x) + x : np.exp(x)는 $\exp(x)$ (지수함수)를 의미합니다.

사용 가능한 연산자: +, -, *, /, **
사용 가능한 함수: np.sin, np.cos, np.exp, np.log 등 numpy 함수
''',
		height=140,
		disabled=True
)

st.title('닫힌구간 [0, 1]에서 실수로 가는 함수 입력')

# 실함수 입력 네모칸
user_func_str = st.text_input('실함수를 입력하세요 (예: x**2 + 2*x)', value='x')



# 입력된 함수 시각화
try:
	x = np.linspace(0, 1, 100)
	y = [eval(user_func_str, {'x': xi, 'np': np}) for xi in x]
	fig, ax = plt.subplots()
	ax.plot(x, y)
	ax.set_xlabel('x', fontproperties=fontprop)
	ax.set_ylabel('f(x)', fontproperties=fontprop)
	ax.set_title('입력한 함수의 그래프', fontproperties=fontprop)
	ax.grid(True)
	# 눈금에도 한글 폰트 적용
	for label in (ax.get_xticklabels() + ax.get_yticklabels()):
		label.set_fontproperties(fontprop)
	st.pyplot(fig)

	# 결과 확인 버튼


	# 버튼 클릭 시마다 결과를 즉시 갱신하도록 변경

	if st.button('결과 확인'):
		# 하이네-코시 정리: 닫힌구간에서 연속이면 평등연속
		is_continuous = True
		for i in range(len(x)-1):
			if not np.isfinite(y[i]) or not np.isfinite(y[i+1]):
				is_continuous = False
				break
			if abs(x[i+1] - x[i]) > 0:
				slope = abs(y[i+1] - y[i]) / abs(x[i+1] - x[i])
				if slope > 1e6:  # 급격한 변화(불연속)로 간주
					is_continuous = False
					break

		# 립시츠 연속 조건: |f(x)-f(y)| <= L|x-y| 인 L 존재
		lipschitz_const = max([abs(y[i+1] - y[i]) / abs(x[i+1] - x[i]) for i in range(len(x)-1)])
		is_lipschitz = np.isfinite(lipschitz_const) and lipschitz_const < 1e6

		if is_continuous:
			st.success('이 함수는 [0,1]에서 평등연속입니다.', icon="✅")
			with st.expander('평등연속인 이유'):
				st.markdown('''
**하이네-코시 정리:** 닫힌구간에서 연속인 함수는 항상 평등연속입니다. 입력한 함수는 [0,1]에서 연속이므로 평등연속입니다.
''')
			if is_lipschitz:
				with st.expander('추가 설명: 립시츠 연속 조건'):
					st.markdown(f'''이 함수는 립시츠 상수 L={lipschitz_const:.3f}로 립시츠 연속이므로, 평등연속입니다.''')
		else:
			st.error('이 함수는 [0,1]에서 평등연속이 아닙니다.', icon="❌")
			with st.expander('평등연속이 아닌 이유'):
				st.markdown('''
함수값이 무한대가 되거나, 구간 내에 불연속점이 존재하여 평등연속이 아닙니다. 예를 들어 1/x는 x=0에서 정의되지 않아 평등연속이 아닙니다.
''')

except Exception as e:
	st.error(f'함수 입력 오류: {e}')
