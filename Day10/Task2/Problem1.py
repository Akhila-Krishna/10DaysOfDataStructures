def is_unique(st): 
	char_set = [False] * 128
 
	for i in range(0, len(st)): 
		val = ord(st[i]) 
		if char_set[val]: 
			return False

		char_set[val] = True

	return True

string1 = "aBcdeF"
print(is_unique(string1)) 
string2 = "nonunique"
print(is_unique(string2)) 
