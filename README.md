# RegEx(Regular-Expression)
1. 정규 표현식 (Regular Expression)

- 정규 표현식에 대해 조사하고, 본인의 깃허브에 public 프로젝트로 등록하여 정리하시오.

- 정규 표현식이 왜 필요한지, 파이썬에서의 기본 사용법, 코드 예제가 필수로 포함되어야 함

<h2> 1️⃣ 정규 표현식이란❓ (Regular Expression) </h2>
 복잡한 문자열에서 우리가 원하는 특정한 패턴을 찾아 처리할 경우 유용하게 사용 가능한 일종 기법이며, 파이썬 뿐만이 아닌 모든 언어에서 공통적으로 사용한다.

<h2> 2️⃣ 정규 표현식의 필요성❗ </h2>
 특정한 조건에 맞는 문자를 추출할 경우, 코드 작성 시 길고 복잡한 절차를 거치게 되지만 정규식을 사용한다면 훨씬 직관적이고 간단하게 작성이 가능하기 때문에
 효율성을 위해 주로 사용한다.

<h2> 3️⃣ 파이썬에서의 기본 사용법⭕ </h2>
 <b> ① 파이썬은 정규 표현식을 지원하기 위해 re 모듈을 제공한다. </b><br>
  👉패턴 객체를 이용하는 4가지 방법<br>
   - <b>re.match()</b> : 문자열의 처음부터 정규식과 매치되는지 조사한다. | match의 결과로 match객체 혹은 None을 리턴해준다. <br>
   - <b>re.search()</b> : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다. | match 메서드와 search 메서드는 문자열의 처음부터 검색할지의 여부에 따라 다르게 사용해야 한다. <br>
   - <b>re.findall()</b> : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다. <br>
   - <b>re.finditer()</b> : 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다. | finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 리턴한다. <br>
  👉match 객체의 메서드<br>
   - <b>match.group()</b> : 매치된 문자열을 리턴한다.<br>
   - <b>match.start()</b> : 매치된 문자열의 시작 위치를 리턴한다.<br>
   - <b>match.end()</b> : 매치된 문자열의 끝 위치를 리턴한다.<br>
   - <b>match.span()</b> : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.<br>
<br>
<b> ② 문자 </b><br>
 👉메타문자<br>
 정규 표현식에서 사용하는 메타문자에는 다음과 같은 것들이 있다.<br>
<b> . ^ $ * + ? { } [ ] | \ ( ) </b><br>
<br>

<b>Dot(.)</b> <br>
정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.<br>
a.b는 "aab" 또는 "a0b"와 같이 a와 b사이에 어떤 문자가 들어가도 모두 매치됨을 의미한다.<br>

<b>반복(별표시)</b><br>
'별표시' 바로 앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다는 의미이다.<br>
0번 이상도 매치가 가능하다.<br>

<b>반복(+)</b><br>
+문자 바로 앞에 있는 문자가 최소 1번이상 반복될 수 있다는 의미이다.<br>
별표시 반복과는 최소 횟수 이상으로 구분하여 사용한다.<br>

<b>반복({m,n}, ?)</b><br>
{ }를 이용하면 반복 횟수를 고정할 수 있다.<br>
1) {m} : 반드시 m번 반복해야 매치<br>
2) {m,n} : m~n회 반복해야 매치<br>
3) {?} : ?앞에 있는 문자가 0번 혹은 1번(있거나 없거나) 사용될 경우 매치<br>

<b>문자 클래스 []</b><br>
문자 클래스로 만들어진 정규 표현식은 "[ ] 사이의 문자들과 매치" 라는 의미를 갖는다.<br>
[  ]안의 두 문자 사이에 존재하는 하이픈(-)은 두 문자 사이의 범위를 의미한다.<br>
<b>❗자주 사용하는 문자 클래스❗</b><br>
 - <b>\d</b> : 숫자와 매치<br>
 - <b>\D</b> : 숫자가 아닌 것과 매치<br>
 - <b>\s</b> : whitespace 문자와 매치<br>
 - <b>\S</b> : whitespace 문자가 아닌 것과 매치<br>
 - <b>\w</b> : 문자 + 숫자와 매치<br>
 - <b>\W</b> : 문자 + 숫자가 아닌 문자와 매치<br>
