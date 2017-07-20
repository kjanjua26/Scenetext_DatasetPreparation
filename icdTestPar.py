file = open('Test_gt.txt', "r")
for line in file: 
    imgname,text = line.split(' ')
    text = text[1:-3]
    imgname,ext = imgname.split('.')
    fileName = imgname + ".gt.txt"
    print text,
    groundTruth = open(fileName, "w+")
    groundTruth.write(text)
    groundTruth.close()
    
    
