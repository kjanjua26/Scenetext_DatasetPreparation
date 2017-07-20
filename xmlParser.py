import xml.etree.ElementTree as ET
import sys
from PIL import Image
import os
"""
A script to extract the bounding box and associate the ground truth with it
accordingly. Scraps data off of xml files.  

"""
def crop(cropImgName, xLoc, yLoc, width, height):
    croppedImg = img.crop((xLoc, yLoc, xLoc + width, yLoc + height))
    croppedImg.save(cropImgName)
filelist = os.listdir('/Users/Janjua/Desktop/TUKL Work/Real Time Scene Text Datasets/KAIST/Digital_Camera/shadow')
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if (fichier.endswith(".xml")):
        fileName, extension = fichier.split('.')
        print fileName
        file = ('/Users/Janjua/Desktop/TUKL Work/Real Time Scene Text Datasets/KAIST/English/Digital_Camera/shadow/' + fileName + '.xml')
        img = Image.open('/Users/Janjua/Desktop/TUKL Work/Real Time Scene Text Datasets/KAIST/English/Digital_Camera/shadow/' + fileName + '.jpg')
        
        tree = ET.parse(file)
        root = tree.getroot()
        for x in root:
            name = x.find('imageName').text
         """
          The txtName is the name of the text which we need while ex
          represents the extension which we discard. 
        
        """
       txtName,ex = name.split(".")
    
        for x in root:
            for y in x:
                if y.tag == "words":
                    count = 0
                    for word in y:
                        count = count + 1
                        print count
                        finaltxtName = txtName + "_" + str(count) + ".gt.txt"
                        cropImgName = txtName + "_" + str(count) + ".png"
                        textFile = open(finaltxtName, "w+")
                        xLoc = word.attrib["x"]
                        yLoc = word.attrib["y"]
                        width = word.attrib["width"]
                        height = word.attrib["height"]
                        print "x Location: ", xLoc
                        print "y Location: ", yLoc
                        print "Width: ", width
                        print "Height: " , height
                        print type(xLoc)
                        croppedImg = img.crop((int(xLoc), int(yLoc), int(xLoc) +
                        int(width), int(yLoc) + int(height)))
                        croppedImg.save(cropImgName)
                        for w in word:
                            c = ' '.join([w.attrib["char"]])
                            s = ""
                            for a in  w.attrib["char"]:
                                s += w.attrib["char"]
                            textFile.write(s)
                            
        textFile.close()
