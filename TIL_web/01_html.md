# HTML

Hyper Text Markup Language

태그를 이용해 정보를 구조화



## 문서 작성 시작

VScode에서 !를 입력하고 tab을 누르면 다음과 같이 된다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

- `<!DOCTYPE html>` : 문서 형식 지정
- `<html>` : 실제 문서가 작성되는 자리
- `<head>` : 문서 제목, 참조, 메타데이터 설정 등, 브라우저에 보이지 않는다.
- `<body>` : 웹 브라우저에 출력되는 요소

## 요소 element

![html tag](https://poiemaweb.com/img/tag.png)

하나의 요소는 시작태그와 종료태그, 그리고 콘텐츠로 이루어짐

여러 요소가 중첩될 수 있다!  **Nested Element**

## 속성 attribute

![html attribute](https://poiemaweb.com/img/html-attribute.png)

요소의 성질, 특징을 정의. 시작태그에 위치하며 key=value 형태로 사용한다.



## 시맨틱 태그

코드의 가독성을 높이고 유지보수를 쉽게 하기 위해  브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확히 설명하는 역할을 하는 태그.

header, nav, aside, section, article, footer 등

![시맨틱 태그](https://poiemaweb.com/img/building-structure.png)



> 출처 : [poiemaweb](https://poiemaweb.com/html5-syntax)



