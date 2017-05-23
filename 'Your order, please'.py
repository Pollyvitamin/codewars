"""
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.
For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
"""
def order(sentence):
	if sentence:
		lst=sentence.split(' ')
		tmp_dict={}
		correct_dig='123456789'
		for item in lst:
			for element in item:
				if element in correct_dig:
					tmp_dict[element]=item
		tmp_lst=[]
		for key in sorted(tmp_dict.keys()):
			tmp_lst.append(tmp_dict[key])
			result=' '.join(tmp_lst)
		return result
	else:
		return sentence
