# coding / encoding

s = 'cafe'
print(len(s))

b = s.encode('utf8')
print(b)
print(len(b))

print(b.decode('utf8'))

# bytes and  bytearray

cafe = bytes('cafe', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1])
