# 웹 대시보드 개발 프로젝트  
#
#  👑 Top 1000 Movies by IMDB Rating 👑
#
### 사용 언어

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

### 라이브러리 

<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> 

### 작업 도구

<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/>

#
#
# 웹대시보드 URL
http://ec2-43-201-72-88.ap-northeast-2.compute.amazonaws.com:8501/
#
# Preview
![preview1](https://user-images.githubusercontent.com/120348534/209481982-86104ea9-07cc-4f8f-b87e-620d5bbad9e5.PNG)
![preview2](https://user-images.githubusercontent.com/120348534/209481986-43e5c1e6-7387-4e3b-ba67-26087b8e08ab.PNG)
#  
#  
#  
#  


###
# 작업 과정 및 내용  
  
###  
###  
##### 1. 데이터 출처  
https://www.kaggle.com/  
'kaggle'이라는 사이트에서 데이터를 찾았습니다.  
영화 평점과 관련한 데이터 중에서 IMDb라는 공신력 있는 사이트에서 집계된 데이터를 선정했습니다.

#####  
#####  

##### 2. 데이터 분석  

**'jupyter notebook'** 을 이용하여 데이터를 분석했습니다.  

#####  

**(1) 데이터 결측값 처리**  
```python
df.isna().sum()
```  
 `'Certificate'컬럼의 결측값 : 101 개`    
 `'Meta_score'컬럼의 결측값 : 157 개`  
```python
df.dropna(inplace=True)
```
 `결측 데이터 삭제  `
```python
df.reset_index(inplace=True)
```
`인덱스 초기화`
 
#####  

**(2) 영화 평점 최상위/최하위 점수 파악**  
```python
    df['IMDB_Rating'].max()
    df['IMDB_Rating'].min()
```
` - top.1000 최상위 점수 : 9.3  `  
` - top.1000 최하위 점수 : 7.6  `
  이미 top.1000으로 선정된 높은 평점의 영화들만 집계된 데이터였기 때문에 이 안에서의 점수 범위를 유저들에게 보여줄 필요가 있다고 생각했습니다.  

#####  

**(3) 영화 개봉년도 범위 확인**  
```python
year = df['Released_Year'].unique()
year = sorted(year)
```  
` 분포 : 1920, 1921, 1922, 1924, 1925 . . . ~ `
 개봉년도의 범위를 파악하여 개봉년도가 적당한 수의 카테고리컬 데이터라면 유저들에게 년도별 데이터를 제공할 생각이었으나 생각보다 년도의 분포 범위가 넓어서 년도별 카테고리화는 하지 않았습니다.

#####  

**(4) 영화 장르 구분**
![2](https://user-images.githubusercontent.com/120348534/209503391-f63bda20-4884-4356-85ba-e5c0d2033c43.PNG)
#####  
#####  
#####  
#####  
이와 같이 영화별로 장르가 1개씩이 아닌 여러개가 섞여 있었습니다. 이 데이터에서는 몇 종류의 장르 값이 있는지 구분하기가 어려웠습니다. 그래서 일단 값을 분리하여 장르의 유니크 값을 구했습니다.
```python
`Genre = df['Genre'].unique()`
`Genre_list = []`  
`   for data in Genre :`   
`   Genre_list.extend(data.split(','))`  
```
` 장르 하나씩 쪼개기 `
```python
Genre_list = set(Genre_list)
Genre_list = list(Genre_list)
```
`데이터 타입 변환을 통해 중복값 제거하기`
이렇게 최종적으로 장르 리스트를 저장하려고 했으나, 같은 장르 이름임에도 불구하고 공백이 들어가 있어서 중복 데이터로 걸러지지 못한 값들이 보였습니다. 그래서 공백을 제거하여 다시 작업해주었습니다.
```python
임시리스트 = []
for data in Genre_list :
    임시리스트.append(data.replace(' ',''))
Genre_list = list(set(임시리스트))
```
`Genre_list`
`= ['Mystery',
 'Crime',
 'Action',
 'Adventure',
 'Musical',
 'Horror',
 'Western',
 'Family',
 'Sci-Fi',
 'Comedy',
 'Biography',
 'Animation',
 'War',
 'Film-Noir',
 'Thriller',
 'Sport',
 'Romance',
 'History',
 'Music',
 'Drama',
 'Fantasy']`
이렇게 장르의 종류는 21개로 구분되었습니다.

#####  

**(5) 영화 러닝타임 범위 확인**
```python
df.sort_values('Runtime')
df.sort_values('Runtime', ascending=False)
```
`모든 영화의 러닝타임 데이터는 99분으로 동일.`
따라서 러닝타임과 관련하여 데이터를 분석하는 것은 의미가 없다고 판단했습니다.

#####  

**(6) top.1000영화에 가장 많이 참여한 감독**
```python
df['Director'].value_counts()
```
`Steven Spielberg     13`
`Martin Scorsese      10`
`Alfred Hitchcock      9`
`.`
`.`
`.`
위 결과를 토대로, 감독별 영화 리스트를 가져오면 어떨까 하는 아이디어를 얻었습니다.
```python
df.loc[ df['Director']=='Steven Spielberg', ]
```
`streamlit 작업 시 사용하기로 결정` 

#####  

**(7) 영화 장르별 비중 확인**
`미리 만들어 놓은 'Genre_list' 활용`
```python
df['Genre'].str.contains('Comedy').sum()
```
`161`
```python
(161/714) * 100
```
` ( 161(해당 장르가 사용된 영화 수) / (전체 영화 수) )  * 100 `
테스트를 위해 한 가지 장르에 대해서만 비율 값을 구해보았습니다.
위와 같이 모든 장르의 비율을 구하기 위해 함수를 생성했습니다.
```python
genre_percent = []
for genre in Genre_list :
    genre_sum = df['Genre'].str.contains(genre).sum()
    percent = (genre_sum/714) * 100
    genre_percent.append(percent)
```
결과 값을 여러 곳에 활용하기 위해 데이터 프레임으로 만들었습니다.
```python
df_genre = pd.DataFrame()
df_genre['Genre'] = Genre_list
df_genre['%'] = genre_percent
df_genre.sort_values('%', ascending=False, inplace=True) # 내림차순 정렬
df_genre = df_genre.reset_index().drop('index', axis=1) # 인덱스 초기화
```
#####  

**(8) 차트 데이터 가공**

```python
genre_values = list(df_genre['Genre'].values)
per_values = list(df_genre['%'].values)
genre_values.reverse()
per_values.reverse()
```

```python
colors = sb.color_palette('RdBu', len(genre_values))
plt.barh(genre_values, per_values, color=colors)
plt.title("Movie proportions by genre")
plt.ylabel("The genre of the movie")
plt.tight_layout
plt.show()
```

#####  
#####  


##### 3. 웹 대시보드 개발

#####  

**'Visual Studio Code'** 를 이용하여 웹 대시보드를 개발했습니다.  

#####  

**유저에게 제공할 데이터 및 기능**
- 'IMDB'와 메타스코어(Meta score)'에 대한 용어 설명
- 영화에 사용된 장르 비율 => 그래프
- 명작이 많이 탄생한 년도 => 그래프
- 장르별 영화 목록 (검색 기능 포함)
- 감독별(작품 수가 많은 감독) 영화 리스트
- 유저가 선택한 장르의 영화를 보여주는 기능
- 위 결과에 대한 정렬 기능 (제목순, 평점순)
- 상세 검색을 통해 선택한 영화 1개에 대한 상세 정보 제공

#####  
#####  

##### (비하인드)
#####  
**첫 번째 난관**
분석용 데이터 선정
https://www.bigdata-culture.kr/bigdata/user/main.do
처음으로 혼자 데이터 분석과 웹대시보드 작업을 시작하려 할 때에는 '문화빅데이터플랫폼'이라는 사이트에서 데이터를 찾기 시작했었습니다. 하지만 이 사이트의 데이터는 새로운 분석을 하기에는 조금 어려웠습니다. 왜냐하면 이 사이트에 올라오는 대부분의 데이터가 이미 분석이 완료된 결과에 대한 내용이었기 때문입니다.
#####  
**두 번째 난관**
GitHub - Actions 실패
매뉴얼대로 실행을 했음에도 불구하고 깃허브 액션즈에 오류게 발생했었습니다. 내용을 잘못 기입한 것 같아서 설정을 3~4번 다시 했었는데도 오류가 사라지지 않았습니다. 마지막 시도는 깃허브 레파지토리 이름을 바꾼 것입니다.
-- 변경 전 :  project-1_movie_top_1000
-- 변경 후 : project1_movie_top_1000
이렇게 바꾼 이유는 파이썬에서 변수명으로 허용되는 유일한 특수 기호는 언더바(_)라고 들었던 기억이 있어서였습니다. 혹시나 git을 실행할 때에도 이 파이썬의 룰과 관련이 있을까 해서 레파지토리 이름을 변경하고 클론/커밋/푸쉬를 모두 다시 해보았더니 깃허브 액션즈 오류가 사라졌습니다.
#####  
**세 번째 난관**
차트 구현 미숙  
주피터 노트북에서 구현되던 차트가 streamlit에서 뜻대로 되지 않았던 것들이 몇 개 있었습니다. 예쁜 차트를 넣고 싶은 마음이 있었기 때문에 데이터 변동성이 크게 없는 차트는 주피터노트북에서 이미지로 저장하여 streamlit으로 출력했습니다.
#####  






