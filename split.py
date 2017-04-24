def newSplit(message, delimiter):
	result = []
	temp = ""
	for i in range(0, len(message)):
		if(message[i] == delimiter):
			if len(temp) > 0:
				result.append(temp)
				temp = ""
		else:
			temp += message[i]
		
	if(len(temp) > 0):
		result.append(temp)

	return result
	
""" usage: updatedSplit('"first,last",123,97124', ",") """
def updatedSplit(message, delimiter):
	final = []
	result = newSplit(message, "\"")
	if( len(result) == 1):
		result2 = newSplit(result[0], ",")
		final.extend(result2)
	else:
		final.append(result[0])
		result2 = newSplit(result[1], ",")
		final.extend(result2)
	return final
	
	
def split2(message, delimiter):
	result = []
	temp = ""
	quote_found = False

	for i in message:
		if quote_found == True:
			if i == '"':
				result.append(temp)
				temp = ""
				quote_found = False
			else:
				temp += i
				continue
		else:
			if i == '"':
				quote_found = True
				continue
			if i == delimiter:
				if temp:
					result.append(temp)
					temp = ""
			else:
				temp += i

	if temp:
		result.append(temp)

	return result
	
if __name__ == "__main__":
	print split2('"hello,world",123,456', ",")
	print newSplit("test,message,123333,456", ",")
	print newSplit("test,message-123333,456", "-")
	print updatedSplit('first,last,123,97124', ",")
	