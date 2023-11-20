# project

OpenCV 예제 

getblue / getchar / FaceDetector

 프로젝트명 : Object Detection & Tracking Camera
수행기간
 2023. 09. 12 ~ 2023. 09. 22 (11일)

담당역할
 - 소프트웨어 구현(아두이노, python)
 - 카메라 장착
 - Servo motor 장착
 - 마이크로 컨트롤러 구현
수행목표
(일반목표) 
 - 눈, 코, 입 인식하여 얼굴추적 기능 개발
(기능목표)
 - 마이크로 컨트롤러 활용 pan / tilt 제어
 - OpenCV 이용 카메라 제어
사용 기술
- python 활용 
- OpenCV 활용 카메라 제어
- 마이크로컨트롤러 활용 서보모터 제어
세부수행내용
구 성 도

상세 내용
1) 목    적 : 눈, 코, 입 인식하여 얼굴 추적 구현
2) 개발환경 : 리눅스(우분투), python(OpenCV), C언어(arduino)
3) 주요 기능 
   3 - 1 servo motor를 이용한 pan tilt 제어
	 마이크로 컨트롤러를 활용해 servo motor를 장착 
              좌우(pan), 상하(tilt)구현
   3 - 2 얼굴인식 머신러닝
	 haarcascade_frontalface_alt.xml 파일이용하여 
              OpenCV 라이브러리에서 얼굴 인식을 수행하는 데 사용
# 구성도
   <img src="https://github.com/ckid132/Face_Detertor/blob/main/%EC%96%BC%EA%B5%B4%20%EC%B6%94%EC%A0%81.jpg"  width="400" height="400">

# 결과화면
<img src="https://github.com/ckid132/python-OpenCV-/blob/main/fd.png"  width="400" height="200">        <img src="https://github.com/ckid132/python-OpenCV-/blob/main/fd2.png"  width="400" height="200">
