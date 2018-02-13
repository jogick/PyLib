
def Hemming(data):

	mask = []
	i = 0
	c = 1
	while i < 10:
		if c == 1<<i:
			i += 1
		else:
			mask.append(c)
		c += 1
	
	mask_index = 0;	
	Hemmings_code = [0,0,0,0,0,0,0,0,0]
	
	for i in data:
		for bit in range(0,8):
			b = i >> bit & 0x01
			for mb in range(8):
				if (mask[mask_index] & (1<<mb)) != 0:
					Hemmings_code[mb] ^= int(b)
			mask_index += 1;

	HemCodeStr = ''	
	for i in Hemmings_code[::-1]:
		HemCodeStr += str(i)
		
	ret_str = hex(int(HemCodeStr, 2)) + " " + bin(Hemmings_code[0] ^ Hemmings_code[1] ^ Hemmings_code[2] ^ Hemmings_code[3] ^ Hemmings_code[4] ^ Hemmings_code[5] ^ Hemmings_code[6] ^ Hemmings_code[7])
	return ret_str
