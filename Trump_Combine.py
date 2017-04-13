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

#loop over lines in both frequency files and add lines to frequency list
for line in TRUMPS_Frequent or TimeTRUMPS_Frequent:
	line = line.strip()
	TRUMPS_Frequent_words.append(line)

#loop over lines in both interview files
for line in TRUMPS or TimeTRUMPS:
	line = line.strip()
	#loop over words in frequency list
	for word in TRUMPS_Frequent_words:
		#if a word in the frequency list appears in a line in the interview files
		#all the line to TRUMPSlist
		if word in line:		
			TRUMPSlist.append(line)

#store a random sampling of lines in TRUMPSlist
sampling = random.sample(TRUMPSlist, 10)

#print the sampled lines as strings
print '\n'. join(sampling)

