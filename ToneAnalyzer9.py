# 
# https://bruceelgort.com/2016/06/07/using-ibm-watson-tone-analyzer-with-python/
#
# Documentation: Tone Analyzer getting started: https://www.ibm.com/watson/developercloud/doc/tone-analyzer/getting-started.html
#
# API End Point: https://gateway.watsonplatform.net/tone-analyzer/api/v3
#
#
#
##########################################################################################################################3

import json
import sys
from watson_developer_cloud import ToneAnalyzerV3
import credentials
from credentials import tone_analyzer

def textinput():
    inputtext = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
    if len(inputtext) >= 1:
        if inputtext == 'q'.lower():
            print ("Quitting")
            sys.exit(1)
        return inputtext
		
def formatedoutput(data):
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
        print()
    print()		
		
###########################################################################
#
#
#
###########################################################################	
		
inputtext = textinput()		
    
data = json.dumps(tone_analyzer.tone(inputtext), indent=2)

data = json.loads(str(data))

formatedoutput(data)

