# 웹 대시보드 개발 프로젝트
####  
####  
#  👑 Top 1000 Movies by IMDB Rating 👑
###
# Preview
![preview1](https://user-images.githubusercontent.com/120348534/209481982-86104ea9-07cc-4f8f-b87e-620d5bbad9e5.PNG)
![preview2](https://user-images.githubusercontent.com/120348534/209481986-43e5c1e6-7387-4e3b-ba67-26087b8e08ab.PNG)
####
####
####
####
#
### 웹대시보드 URL
http://ec2-43-201-72-88.ap-northeast-2.compute.amazonaws.com:8501/
###
### 사용 언어
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
###  
### 라이브러리
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> 
###  
### 작업 도구
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/>
#
###
# 🔷 작업 과정 및 내용

###
##### 1. 데이터 출처
https://www.kaggle.com/
'kaggle'이라는 사이트에서 데이터를 찾았습니다.
영화 평점과 관련한 데이터 중에서 IMDb라는 공신력 있는 사이트에서 집계된 데이터를 선정했습니다.

###    
##### 2. 데이터 분석
'jupyter notebook'을 이용하여 데이터를 분석했습니다.
> ** (1) 데이터 결측값 처리 **
 `df.isna().sum()`
 -- 'Certificate'컬럼의 결측값 : 101 개
 -- 'Meta_score'컬럼의 결측값 : 157 개
 `df.dropna(inplace=True)`
 -- 결측 데이터 삭제
 
(2) 영화 평점 최상위/최하위 점수 파악
 -- 이미 top.1000으로 선정된 높은 평점의 영화들만 집계된 데이터였기 때문에 이 안에서의 점수 범위를 유저들에게 보여줄 필요가 있다고 생각했습니다.
(3) 영화 개봉년도 범위 확인
 -- 개봉년도의 범위를 파악하여 개봉년도가 적당한 수의 카테고리컬 데이터라면 유저들에게 년도별 데이터를 제공할 생각이었으나 생각보다 년도의 분포 범위가 넓어서 년도별 카테고리화는 하지 않았습니다.


###
##### 3. 분석이 완료되면, 웹 대시보드로 개발한다.

###
##### 5. 웹 대시보드는 비주얼스튜디오 코드로 개발한다.

###
##### 6. 주피터 노트북에서 분석한 코드를, 비주얼 스튜디오로 옮긴다.

###
##### 7. 인터랙티브한 대시보드를 위해서, 유저에게 데이터를 입력받도록 개발한다.
###
##### 8. 비하인드
머신러닝을 적용할 수 있을까?


첫 번째 난관
분석용 데이터 선정
https://www.bigdata-culture.kr/bigdata/user/main.do
처음으로 혼자 데이터 분석과 웹대시보드 작업을 시작하려 할 때에는 '문화빅데이터플랫폼'이라는 사이트에서 데이터를 찾기 시작했었습니다. 하지만 이 사이트의 데이터는 새로운 분석을 하기에는 조금 어려웠습니다. 왜냐하면 이 사이트에 올라오는 대부분의 데이터가 이미 분석이 완료된 결과에 대한 내용이었기 때문입니다.

두 번째 난관
GitHub - Actions 실패
매뉴얼대로 실행을 했음에도 불구하고 깃허브 액션즈에 오류게 발생했었습니다. 내용을 잘못 기입한 것 같아서 설정을 3~4번 다시 했었는데도 오류가 사라지지 않았습니다. 마지막 시도는 깃허브 레파지토리 이름을 바꾼 것입니다.
-- 변경 전 :  project-1_movie_top_1000
-- 변경 후 : project1_movie_top_1000
이렇게 바꾼 이유는 파이썬에서 변수명으로 허용되는 유일한 특수 기호는 언더바(_)라고 들었던 기억이 있어서였습니다. 혹시나 git을 실행할 때에도 이 파이썬의 룰과 관련이 있을까 해서 레파지토리 이름을 변경하고 클론/커밋/푸쉬를 모두 다시 해보았더니 깃허브 액션즈 오류가 사라졌습니다.




