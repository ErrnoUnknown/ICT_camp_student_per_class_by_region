# ICT 창업가 캠프 프로젝트

## 프로젝트 개요
지역 및 나이별 한 학급당 평균 학생 수를 Python의 Folium 라이브러리를 이용하여 시각화 프로젝트입니다.

## 참고
* ```지역 및 나이별 한 학급당 평균 학생 수``` 데이터는 이하 ```학생 수```로 표기합니다.
* ```대한민국 시도별 JSON``` 데이터는 이하 ```시도별 JSON```으로 표기합니다.

## 사용 데이터 출처
* [시도별 JSON](https://blog.naver.com/PostView.naver?blogId=ppoiu5706&logNo=222451249924)
* [학생 수](https://www.schoolinfo.go.kr/ng/go/pnnggo_a01_l2.do)

## 데이터 전처리
* [시도별 JSON to Geojson 변환](https://products.aspose.app/gis/conversion/json-to-geojson)
* [학생 수 전처리](https://colab.research.google.com/drive/1XNI1SzwEjydQRyaZEu2YM5fI_n8ia5ve)
  * ```heatmap_data.to_excel('avg_students_per_class_by_age.xlsx')``` 코드 추가 후 데이터를 내보내기 및 다운로드했습니다.
* ```시도별 Geojson```과 ```학생 수```의 지역명 중, 불일치하는 항목은 ```시도별 Geojson```의 기준에 맞게 변경하였습니다.

## 실행 환경
* Python 3.11.7 환경에서 실행했습니다.
* 필요 라이브러리는 ```setup/requirements.txt```에 명시되어있습니다.

## 사용 방법
* ```main.py```를 실행해줍니다.
* 스크립트가 정상적으로 실행되었을 경우, ```map``` 폴더 안에 시각화된 지도가 HTML 형태로 저장됩니다.

## Config 기능
* ```config/config.yml```을 활용하여 시각화 옵션을 손쉽게 변경할 수 있도록 구현하였습니다.
* ```config/config.yml```의 자세한 설명은 [이곳](config_guide.md)를 참고해주세요.
