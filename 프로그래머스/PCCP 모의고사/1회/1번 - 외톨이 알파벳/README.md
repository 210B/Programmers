# [PCCP 모의고사 #1] 1번 - 외톨이 알파벳

[문제 링크](https://school.programmers.co.kr/learn/courses/15008/lessons/121683) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.28 ms

### 구분

프로그래밍 강의 > PCCP 모의고사 1회

### 채점결과

<p>채점 결과</p>
<p>정확성: 100.0</p>
<p>합계: 100.0 / 100.0</p>

### 문제 설명

<p>알파벳 소문자로만 이루어진 어떤 문자열에서, 2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 외톨이 알파벳이라고 정의합니다.</p>
<p>문자열 "edeaaabbccd"를 예시로 들어보면,</p>
<ul>
<li>a는 2회 이상 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
"ede(aaa)bbccd"</li>
<li>b, c도 a와 같은 이유로 외톨이 알파벳이 아닙니다.</li>
<li>d는 2회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
"e(d)eaaabbcc(d)"</li>
<li>e도 d와 같은 이유로 외톨이 알파벳입니다.</li>
</ul>

<p>문자열 "eeddee"를 예시로 들어보면,</p>
<ul>
<li>e는 4회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
"(ee)dd(ee)"</li>
<li>d는 2회 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
"ee(dd)ee"</li>
</ul>
<p>문자열 input_string이 주어졌을 때, 외톨이 알파벳들을 알파벳순으로 이어 붙인 문자열을 return 하도록 solution 함수를 완성해주세요. 만약, 외톨이 알파벳이 없다면 문자열 "N"을 return 합니다.</p>

<h5>제한사항</h5>

<ul>
<li>1 ≤ input_string의 길이 ≤ 2,600</li>
<li>input_string은 알파벳 소문자로만 구성되어 있습니다..</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>input_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"edeaaabbccd"</td>
<td>"de"</td>
</tr>
<tr>
<td>"eeddee"</td>
<td>"e"</td>
</tr>
<tr>
<td>"string"</td>
<td>"N"</td>
</tr>
<tr>
<td>"zbzbz"</td>
<td>"bz"</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
<ul>
<li>문제의 예시와 같습니다.</li>
<li>외톨이 알파벳인 e, d를 알파벳순으로 이어 붙여 문자열을 만들면 "de"가 됩니다.</li>
</ul></p>
<p>입출력 예 #2<br>
모든 문자들이 한 번씩만 등장하므로 외톨이 알파벳이 없습니다.</p>
<p>입출력 예 #3<br>
문제의 예시와 같습니다.</p>
<p>입출력 예 #4<br>
외톨이 알파벳인 z, b를 알파벳순으로 이어 붙여 문자열을 만들면 "bz"가 됩니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
