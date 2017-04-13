import sys
import FileReader

#store file from command line in variable file
file = sys.stdin

#pair down the contents to make the results manageable. Developer changes 
#the boundaries
for word, count in FileReader.sysIn(file):
	if count < 150 and count > 30:
		print word #+ " : " + str(count)
