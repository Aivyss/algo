# 동적계획법(Dynamic Programming)
- 문제를 쪼개서 작은 문제의 답을 구한 뒤, 그것을 취합하여 더 큰 문제의 답으로 도출하는 과정.
- 분할정복과 비슷함.

# 접근법(구현법)

|      | top-down    | bottom-up  |
|------|-------------|------------|
| 구현   | 재귀          | 반복문        |
| 저장방식 | memoization | tabulation |

## Memoization
- 이미 구한 부분문제의 답은 cache로 저장하고 가져다 쓴다 (중복연산방지).
- Lazy-Evaluation
## Tabulation
- 부분문제의 답은 미리 다 구해두는 방법.
- Eager-Evaluation
