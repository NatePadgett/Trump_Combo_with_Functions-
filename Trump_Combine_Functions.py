import random

#Open four files to work with
TRUMPS = open('TRUMPS.txt')
TimeTRUMPS = open('Trump_Truth_Falsehood_Interview.txt')
TRUMPS_Frequent = open('TRUMPS_Words2.txt')
TimeTRUMPS_Frequent = open('Trumps_Interview_Words2.txt')

#create a list for storing lines from the Trump interviews
TRUMPSlist = []

#create a list of all frequently used words from both word frequency files
TRUMPS_Frequent_words = []

###
#attempting to break up loops that parse down the text files into discrete functions.
def lineStrip1(file1, file2, list1):
	list1 = []
	for line in file1 or file2:
		line = line.strip()
		return line
		##list1.append(line)
		##return list1

def lineStrip2(file1, file2, list1, list2):
	list1 = []
	list2 = []
	for line in file1 or file2:
		line = line.strip()
		for word in list1:
			if word in line:
				return line 
				##list2.append(line)
				##return list2

#printing functions to test them.
print lineStrip1(TRUMPS_Frequent, TimeTRUMPS_Frequent, TRUMPS_Frequent_words)

print lineStrip2(TRUMPS, TimeTRUMPS, TRUMPS_Frequent_words, TRUMPSlist)
###

#loop over lines in both frequency files and add lines to frequency list
for line in TRUMPS_Frequent or TimeTRUMPS_Frequent:
	line = line.strip()
	TRUMPS_Frequent_words.append(line)

#print TRUMPS_Frequent_words

#loop over lines in both interview files
for line in TRUMPS or TimeTRUMPS:
	line = line.strip()
	#loop over words in frequency list
	for word in TRUMPS_Frequent_words:
		#if a word in the frequency list appears in a line in the interview files
		#all the line to TRUMPSlist
		if word in line:		
			TRUMPSlist.append(line)

print TRUMPSlist

#store a random sampling of lines in TRUMPSlist
sampling = random.sample(TRUMPSlist, 10)

#print the sampled lines as strings
print '\n'. join(sampling)

