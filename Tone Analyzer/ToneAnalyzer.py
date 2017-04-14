#########################################################################################################################
#
#
# API End Point: https://gateway.watsonplatform.net/tone-analyzer/api/v3
#
#
# Lennart Frantzell 
# 4/14/2017
##########################################################################################################################3

import json
import sys
from watson_developer_cloud import ToneAnalyzerV3
import credentials
from credentials import tone_analyzer

#		
# The code for the input and formatted output functions Come from 
# https://bruceelgort.com/2016/06/07/using-ibm-watson-tone-analyzer-with-python/		
#

def textinput():
    inputtext = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
    if len(inputtext) >= 1:
        if inputtext == 'q'.lower():
            print ("Quitting")
            sys.exit(1)
        return inputtext
		
def formatedoutput(data):
    print ("----------------------------------------------------------------------")
    print("Output from the Watson Tone Analyzer Service running on IBM Bluemix: \n")
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
        print()
    print()		
		
###########################################################################
#
# Main
#
###########################################################################	
		
inputtext = textinput()		
    
data = json.dumps(tone_analyzer.tone(inputtext), indent=2)
data = json.loads(str(data))

formatedoutput(data)

