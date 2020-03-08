from collections import deque

# good for operation from both side of array, but not from inside

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
dq.extend([11, 12, 13])
