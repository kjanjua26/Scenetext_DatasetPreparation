file = open("/Users/Janjua/Desktop/TUKL Work/Real Time Scene Text Datasets/Oxford VGG/annotation_test.txt", "r")
lines = file.readlines()
lengthLines = len(lines) #prints the number of lines in the text file.
print lengthLines

for line in lines:
	name, instance = line.split(" ")
	instance = instance.replace(" ", "")
	symbol,text = name.split("./") #the symbol is ./ where it is split
	extra, string = text.split("_", 1) #splits the string at first occurence of "_"
	gtText,additional = string.split("_")
	#print "The Ground truth is: ", gtText
	fileName,ex = additional.split(".")
	fileName = fileName + ".gt.txt"
	print fileName, ": ", gtText
	#Open the text file. 
	textFile = open(fileName, "w+")
	textFile.write(gtText)
	textFile.close()

