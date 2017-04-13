# CTEC 121 Intro to Programming and Problem Solving
# Bruce Elgort / Clark College
# Using IBM Watson's Tone Analyzer to detect and interpret emotional, social, and writing cues found in text.
# February 26, 2016
# Version 1.0
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

from watson_developer_cloud import ToneAnalyzerV3
tone_analyzer = ToneAnalyzerV3(
    username = '483f622d-06ab-44a8-bdfc-d8582c1c2d0c',
    password = 'IuTz4eCmxrf5',
    version='2016-05-19 ')
    
text='A word is dead when it is said, some say. Emily Dickinson'	
 
print ("https://www.ibm.com/watson/developercloud/doc/tone-analyzer/understand-tone.html")
print ("Joy, Fear, Sadness, Discust, Anger")
 
 
print(json.dumps(tone_analyzer.tone(text), indent=2))
print ("=======================================================================")

myparsed_json = json.dumps(tone_analyzer.tone(text), indent=2)

print ("############ MyParsedJSON ############################################################################")

myparsed_json = json.loads(myparsed_json)

print ("MyParsedJSON")


