def countCharacterType(str): 
	vowels = 0
	consonant = 0
 
	for i in range(0, len(str)): 	
		ch = str[i] 
		if ( (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') ): 
			ch = ch.lower() 
			if (ch == 'a' or ch == 'e' or ch == 'i'
						or ch == 'o' or ch == 'u'): 
				vowels += 1
			else: 
				consonant += 1	 
	print (consonant) 

 
str = "Welcome to Educative!"
countCharacterType(str) 

