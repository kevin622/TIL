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
  - `div / ul, ol, li / p / hr / form` 등

- `display: inline`

  - 줄바꿈X
  - width, height, margin-top(bottom) 지정 불가능
  - line-height로 여백 지정
  - `span / a / img / input, label` 등




- 속성에 따른 수평 정렬 : `margin-right: auto` `text-align: left`
- `display: inline-block` : 한 줄에 표시, width, height, margin 지정 가능
- `display: None` 아무것도 표시 안 함, 공간조차 사라짐

##  Position

- `static` : 디폴트, 기준위 좌측상단, 부모 요소 위치 기준
- 좌표 프로퍼티를 통해 이동 가능한 포지션
  - `relative` : 상대 위치, static 위치 기준, 자리를 남겨두고 이동
  - `absolute` : 절대 위치, static이 아닌 가장 가까운 조상 요소 위치 기준, 자리를 비워두고 이동
  - `fixed` : 고정위치, 브라우저 기준



## 레이아웃 Layout

### Float

- 이미지 주변으로 텍스트를 둘러싸는 레이아웃을 위해 사용
- 이미지가 아닌 다른 요소에도 적용 가능
- `absolute` 처럼 자신의 위치를 없앤다.

속성

- `none` : default
- `left` : 요소를 왼쪽으로 띄움 <==> `right`

```css
.left {
  float: left;
}
```

> 참고: 네이버의 홈화면 탭은 float 를 이용한다.



### Flexbox

1차원 단방향 레이아웃 / 요소 간 공간 배분과 정렬

_상자를 흔들어서 내부를 정렬한다고 생각하자!_

[Flexbox Froggy](https://flexboxfroggy.com/#ko)

- 요소
  - Flex Container (부모 요소)
  - Flex Item (자식 요소)
- 축
  - Main Axis (메인 축)
  - Cross Axis (교차 축)

```css
.flex-container {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-around;
  align-items: center
}
```

- `flex-direction` : 메인 축 방향 변경
  - `row`, `row-reverse`, `column`, `column-reverse`
- `justify-content` : 메인 축 정렬
  - `flex-start`, `flex-end`, `center`, `space-between`, `space-evenly` , `space-around`
- `align-items` / `align-content` / `align-self` : 교차 축 정렬
  - `flex-start`, `flex-end`, `center`, `stretch`, `baseline`
  - `space-between`, `space-around` (align-content)
  - `auto`(align-self)
- 기타 :`flex-wrap` /  `flex-flow` / `order`

```html
<div class="flex-container">
  <div>
    First item
  </div>
  <div>
    Second item
  </div>
</div>
```

