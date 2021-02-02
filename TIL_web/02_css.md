# CSS

Cascading Style Sheet

스타일, 레이아웃 등을 통해 HTML 문서를 표시하는 방법을 지정하는 언어

## 정의 방법

- 인라인

```css
<h1 style="color: blue; font-size: 100px">Hello</h1>
```

- 내부참조

```css
<style>
    h2 {
      color: red;
    }

```

- 외부참조(주로 `head` 태그에 많이 씀)

```css
<link rel="stylesheet" href="semantic.css">
```

## CSS 셀렉터 

- `#` : id

- `.` : class



### 우선순위

- `!important`

```css
<style>
    h2 {
      color: red !important;
    }
```

- 인라인 / id선택자 / class 선택자 / 요소 선택자
- 소스 순서



## Box model

- 구성 : *Margin > Border > Padding > Content*

- 노트북이 올려진 책상을 생각하자!
- 셀렉터에서 Border의 width, style, color는 한 줄에 쓸 수 있다!

```css
.border {
  border-width: 2px;
  border-style: dashed;
  border-color: black;
}
/* 위 코드는 아래와 같음 */

.border {
  border: 2px dashed black;
}
```

- 편의성을 위해 box-sizing을 border-box로 설정하면 좋음

```css
* {
  box-sizing: border-box;
}
```

- **마진상쇄** : 위 아래 요소의 마진이 겹칠 경우 아래 요소의 마진만 적용됨. 마진이 겹치면 주의해야 함

## Display

- `display: block` 

  - 줄바꿈
  - 안에 인라이 레벨 요소가 들어갈 수 있음

- `display: inline`

  - 줄바꿈X
  - width, height, margin-top(bottom) 지정 불가능
  - line-height로 여백 지정

  