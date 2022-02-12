
import string
LOWERCASE_OFFSET = ord("a")
ALPHABEST = string.ascii_lowercase[:16]

def b16_decode(enc):
	dec = ""
	for i in range(0, len(enc), 2):
		n1 = ord(enc[i]) - LOWERCASE_OFFSET
		n2 = ord(enc[i+1]) - LOWERCASE_OFFSET
		dec += chr((n1 << 4) + n2)
	return dec
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABEST[(t1 + t2) % len(ALPHABEST)]
enc = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"
for key in ALPHABEST:
	resultT = ""
	for i,c in enumerate(enc):
		resultT+= shift(c, key[i% len(key)])
	
	flag = b16_decode(resultT)
	print(flag)