# Analysis(MapName_Mirama)

![그림1. whitezone의 중심](images/Untitled.png)

그림1. whitezone의 중심

![그림2. alive_user들의 기하학적 중심점](images/Untitled%201.png)

그림2. alive_user들의 기하학적 중심점

![그림3. whitezone의 중심과 alive_user들의 중심의 거리](images/Untitled%202.png)

그림3. whitezone의 중심과 alive_user들의 중심의 거리

```
주제 : 게임 '배틀그라운드'의 한 매치 내의 생존자의 기하학적 중심과 whitezone 생성 위치의 통계적 상관성 분석
주제 선정 이유 : 배틀그라운드를 자주 플레이하는 유저로서, 게임의 승패에 큰 영향을 미치는 자기장(whitezone)의 위치가 무작위로 생성되는지, 
아니면 생존자들의 위치를 기반으로 생성되는지에 대해 궁금증이 생겼습니다. 이러한 의문을 해결하기 위해 상관분석을 통해 '유저들의 기하학적 중심과 가까운 거리일수록, 실제 whitezone의 중심이 생성되는 빈도가 높은지'를 검증하기 위한 데이터 수집, 처리 파이프라인을 구축하고, 모은 데이터를 바탕으로 상관분석을 수행하는 것을 주제로 선정하게 되었습니다.
맵 별로, 페이즈 별로 whitezone의 생성 알고리즘이 다를 수 있기 때문에, Miramar맵을 기준으로, 각 페이즈 별로 총 8개의 분석을 수행했습니다.

# 데이터 선정 과정
- 한 명의 유저의 데이터로부터 시작해서, 한 매치를 지정하고 그 데이터를 DB에 저장을 합니다.(Mapname: Mirama) 해당 매치에 참여한 유저 중 랜덤으로 한 명을 뽑아서 해당 유저가 플레이 한 게임중 Mapname이 'Mirama'인 매치 데이터를 가져와서 DB에 저장합니다. 위 작업을 반복하여 다양한 매치 데이터를 랜덤으로 계속해서 뽑습니다. 결과적으로 이는, 무선표집의 형태로 설명할 수 있습니다.
 
# 데이터 분석 과정
1. 상관분석 수행을 위한 상관분석 메소드 후보 선정
- 피어슨
  - 선형 상관계수 측정
  - 데이터가 정규 분포를 따를때 사용
  - 두 변수 간의 선형관계 측정
- 스피어만
  - 데이터 분포에 대한 가정이 필요없음
  - 데이터가 정규분포를 따르지 않아도 유용함
2. 상관분석 메소드 선택을 위한 데이터의 정규성 검정 : 데이터의 정규분포 여부확인
 - X축 : 일정 거리 단위로 자른 범위를 index 순서로 라벨링한 값 (비율척도)
 - y축 : 해당 label에 해당하는 빈도수 (비율척도)
 - 시각화 : 히스토그램, QQ플롯, BOX 플롯
 - 통계적 방법 : 샤피로-윌크 테스트, 콜모그라브-스미노프 테스트
 - H0(귀무가설): 미라마에서 각 페이즈 당 살아있는 유저들의 기하학적 중심의 위치와 whitezone의 중심의 위치는 상관관계가 없다.
 - H1(대립가설): 미라마에서 각 페이즈 당 살아있는 유저들의 기하학적 중심의 위치와 whitezone의 중심의 위치는 상관관계가 있다.
  - P-value : 값이 작을수록 귀무가설 기각 근거 강해짐
  - alpha(유의수준) : 귀무가설을 기각하는 기준이 되는 값 0.05 또는 0.01

 ## 귀무가설과 대립가설을 반대로 정의한 이유
 - 분석에서 일반적으로 우리가 입증하고자 하는 가설을 대립가설로 설정합니다.
 귀무가설은 보통 "효과가 없다" 또는 "차이가 없다"와 같이 부정적인 진술을 담고 있으며, 분석을 통해 이를 기각하려고 합니다.
 반면, 대립가설은 "효과가 있다", "차이가 있다"와 같이 긍정적인 진술을 담고 있어서, 데이터를 통해 이를 증명하려고 합니다.
 따라서, 우리가 증명하고자 하는 관계나 효과를 대립가설로 설정하고, 이를 입증하기 위해 데이터 분석을 수행하는 것이 일반적입니다.
```

- 그림3 의 히스토그램(x축: 각 페이즈마다, 일정한 거리 단위로 자른 값의 인덱스 순서. 페이즈 별로 whitezone이 줄어드는 비율만큼 범위도 축소함. y축: 해당 label에서의 빈도수)

![Untitled](images/Untitled%203.png)

![Untitled](images/Untitled%204.png)

## 정규분포 확인

1. 샤피로-윌크 검정

![Untitled](images/Untitled%205.png)

1. QQ-plot

![Untitled](images/Untitled%206.png)

![Untitled](images/Untitled%207.png)

[각 Phase별 분석]

1. **Phase 1**:
    - QQ 플롯에서 대부분의 데이터 점들이 대각선에 가까이 분포하고 있으나, 꼬리 부분에서 대각선에서 벗어나 있는 점들이 있습니다.
    - 이는 Phase 1의 데이터가 전체적으로 정규분포에 근접하지만, 극단값(outlier)에서 정규분포를 따르지 않는다는 것을 의미합니다.
2. **Phase 2**:
    - QQ 플롯에서 중간 구간의 데이터 점들은 대각선에 가깝게 분포하고 있으나, 꼬리 부분에서 대각선에서 벗어나 있습니다.
    - Phase 2의 데이터는 중심부에서는 정규분포를 따르지만, 극단값에서는 정규분포를 따르지 않습니다.
3. **Phase 3**:
    - 중간 구간의 데이터 점들이 대각선에 근접하지만, 극단값에서 벗어나 있는 경향이 있습니다.
    - Phase 3의 데이터는 중심부에서는 정규분포에 가깝지만, 꼬리 부분에서는 정규분포를 따르지 않습니다.
4. **Phase 4**:
    - 중간 구간의 데이터 점들이 대각선에 가깝게 분포하지만, 끝부분에서 벗어나는 경향이 있습니다.
    - Phase 4의 데이터는 중심부에서는 정규분포를 따르지만, 극단값에서는 정규분포를 따르지 않습니다.
5. **Phase 5**:
    - 중간 구간의 데이터 점들이 대각선에서 벗어나고 있으며, 꼬리 부분에서 대각선에서 크게 벗어나 있습니다.
    - Phase 5의 데이터는 정규분포를 따르지 않는다는 것을 나타냅니다.
6. **Phase 6**:
    - QQ 플롯에서 데이터 점들이 대각선에서 크게 벗어나고 있습니다.
    - 이는 Phase 6의 데이터가 정규분포를 따르지 않는다는 것을 의미합니다.
7. **Phase 7**:
    - 데이터 점들이 대각선에서 크게 벗어나고 있습니다.
    - Phase 7의 데이터는 정규분포를 따르지 않는 것으로 보입니다.
8. **Phase 8**:
    - 데이터 점들이 대각선에서 벗어나 있으며, 특히 극단값에서 크게 벗어나고 있습니다.
    - Phase 8의 데이터는 정규분포를 따르지 않는 것으로 보입니다.

### 결론:

- 모든 Phase에서 QQ 플롯을 보면, 중간 구간에서는 대체로 대각선에 근접하지만 꼬리 부분에서 크게 벗어나는 경향이 있습니다.
- 이는 모든 Phase의 데이터가 정규분포를 따르지 않음을 시사합니다.
- 이는 샤피로-윌크 검정 결과와도 일치합니다.
- 따라서 모든 Phase에서 데이터는 정규분포를 따르지 않는 것으로 분석됩니다.

상관관계 분석을 위해 정규분포를 알아본 결과 정규분포를 따르지 않기에 상관분석은 스피어만 상관분석으로 결정하였음. 

## 상관관계 검증

![Untitled](images/Untitled%208.png)

### 각 페이즈별 분석 결과:

- **Phase 1:**
    - 상관계수: -0.640572376133425
    - p-value: 4.490554635969112e-05
    - 해석: 유의미한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 유의미한 음의 상관관계가 존재합니다.
- **Phase 2:**
    - 상관계수: -0.6434290218175496
    - p-value: 4.0480149725718794e-05
    - 해석: 유의미한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 유의미한 음의 상관관계가 존재합니다.
- **Phase 3:**
    - 상관계수: -0.7489504124696674
    - p-value: 3.488211673978302e-07
    - 해석: 강한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 강한 음의 상관관계가 존재합니다.
- **Phase 4:**
    - 상관계수: -0.7350075512021718
    - p-value: 7.412121803432713e-07
    - 해석: 강한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 강한 음의 상관관계가 존재합니다.
- **Phase 5:**
    - 상관계수: -0.7321263032134597
    - p-value: 8.611463651503739e-07
    - 해석: 강한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 강한 음의 상관관계가 존재합니다.
- **Phase 6:**
    - 상관계수: -0.6048640678104168
    - p-value: 0.0001511163942786868
    - 해석: 유의미한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 유의미한 음의 상관관계가 존재합니다.
- **Phase 7:**
    - 상관계수: -0.5892087551875876
    - p-value: 0.00024606444617736344
    - 해석: 유의미한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 유의미한 음의 상관관계가 존재합니다.
- **Phase 8:**
    - 상관계수: -0.7006037456435822
    - p-value: 3.9598520616432805e-06
    - 해석: 강한 음의 상관관계가 있습니다. 즉, 히스토그램의 x값(거리)과 y값(빈도수) 간에 강한 음의 상관관계가 존재합니다.

### 결론:

- 각 페이즈의 상관계수가 모두 음수이고, p-value가 0.05보다 작아 귀무가설(H0)을 기각할 수 있습니다. 이는 살아있는 유저들의 위치와 자기장 중심의 위치 간에 유의미한 음의 상관관계가 있음을 의미합니다.
- 상관계수가 음수라는 것은 거리가 멀어질수록 빈도수가 줄어드는 경향이 있음을 나타냅니다.
- 따라서, Miramar 맵의 각 페이즈의 whitezone의 생성 위치는 유저들이 몰린 곳에서 멀어질수록 빈도수가 낮아진다는 상관관계를 보입니다.