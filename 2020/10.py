input = """35
111
135
32
150
5
106
154
41
7
27
117
109
63
64
21
138
98
40
71
144
13
66
48
12
55
119
103
54
78
65
112
39
128
53
140
77
34
28
81
151
125
85
124
2
99
131
59
60
6
94
33
42
93
14
141
92
38
104
9
29
100
52
19
147
49
74
70
84
113
120
91
97
17
45
139
90
116
149
129
87
69
20
24
148
18
58
123
76
118
130
132
75
110
105
1
8
86"""

lines = sorted(int(x) for x in input.split("\n"))

from collections import defaultdict

# Question 1

lines.insert(0, 0)
distribution = defaultdict(int)
distribution[3] += 1
for i, line in enumerate(lines[1:]):
    diff = line - lines[i]
    distribution[diff] += 1

print(distribution[1]*distribution[3])

# Question 2

adapters = set(lines)
memo = {}
def arrangements(num):
    if num in memo:
        return memo[num]
    reachable = [num + x for x in range(1, 4) if num + x in adapters]
    if len(reachable) == 0:
        memo[num] = 1
        return 1
    result = sum(arrangements(x) for x in reachable)
    memo[num] = result
    return result

print(arrangements(0))