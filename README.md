# 📐 직관적 수학·지식 시각화 랩 (Intuitive Math Lab)

> 어려운 수식 대신 눈과 손가락으로 만지는 수학의 아름다움  
> **🌐 라이브 인터랙티브 체험**: [https://kwonflower831-cell.github.io/math-lab/](https://kwonflower831-cell.github.io/math-lab/)

100% 클라이언트 사이드 순수 HTML5 Canvas 엔진으로 구현된 인터랙티브 수학 원리 시각화 교구입니다.  
별도의 설치나 외부 라이브러리 없이 모바일 스마트폰과 PC 브라우저에서 60fps로 매끄럽게 동작합니다.

---

## 🎨 주요 시각화 모듈 (Interactive Modules)

### 1. 🍕 초등 분수 교구 (피자 & 막대 분할 모델)
전체 조각 중 선택된 조각의 비율을 직관적으로 확인하고 기약분수 약분 및 백분율을 실시간으로 탐색합니다.
![Fraction Pizza](math_visual_gifs/01_fraction_pizza.gif)

### 2. ⚪ 단위원과 삼각함수 ($\sin, \cos, \tan$)
단위원을 회전하는 동경 벡터의 수직 높이($\sin$, 주황)와 수평 밑변($\cos$, 청록)이 실시간 파동으로 전개됩니다.
![Trigonometry Wave](math_visual_gifs/02_trig_unit_circle.gif)

### 3. 🌀 피보나치 수열과 황금 나선 (Golden Spiral)
$1, 1, 2, 3, 5, 8, 13\dots$ 정사각형 타일들이 시계방향으로 증식하며 황금비($\Phi \approx 1.618$) 나선 곡선을 그립니다.
![Fibonacci Spiral](math_visual_gifs/03_fibonacci_spiral.gif)

### 4. 🎱 갈톤 보드 (정규분포 핀볼 시뮬레이션)
상단에서 떨어진 구슬들이 핀에 부딪히며 좌우 50% 확률로 튕겨 바닥에 가우스 종형 곡선(중심극한정리)을 형성합니다.
![Galton Board](math_visual_gifs/04_galton_normal_distribution.gif)

### 5. 📐 3D 플라톤 정다면체 탐색기 (Euler's Formula $V - E + F = 2$)
정사면체, 정육면체, 정팔면체, 정십이면체, 정이십면체를 마우스나 스마트폰 터치 드래그로 360도 자유자재 회전시키며 오일러 불변성을 확인합니다.
![3D Polyhedron](math_visual_gifs/05_polyhedron_3d.gif)

### 6. 🌊 피타고라스 정리: 유체 회전 증명 ($a^2 + b^2 = c^2$)
밑변($a^2$)과 높이($b^2$)의 사각형에 채워진 푸른 유체가 빗변의 거대한 사각형($c^2$)으로 남김없이 쏟아져 면적의 보존을 증명합니다.
![Pythagoras Fluid](math_visual_gifs/06_pythagoras_fluid.gif)

---

## 🚀 기술 스택 & 특징
- **Pure Web Standards**: HTML5, Canvas 2D API, CSS3 Glassmorphism
- **Zero Dependencies**: Three.js, React, Tailwind 등 외부 번들 없이 단 1개의 독립형 HTML 파일로 작동
- **Mobile Touch Ready**: 스마트폰 터치 제스처(`touchmove`)를 통한 3D 회전 제어
- **Ultra Lightweight**: 전 모듈을 포함한 단일 파일 용량 45KB 미만
