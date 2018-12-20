from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import (Features, 
	EntitiesOptions, KeywordsOptions, ConceptsOptions, CategoriesOptions,
		SentimentOptions, MetadataOptions, RelationsOptions,
			EmotionOptions, SemanticRolesOptions )
import sys
from watson_developer_cloud import WatsonApiException
query = sys.argv[1]
# If service instance provides API key authentication
service = NaturalLanguageUnderstandingV1(
	version='2018-03-19',
	## url is optional, and defaults to the URL below. Use the correct URL for your region.
	url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-03-19',
	iam_apikey='HfH04bddep26QPQIJ7rxI55zPpdF0B0IWr-oBl3R4AAJ')

# service = NaturalLanguageUnderstandingV1(
#     version='2018-03-16',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     # url='https://gateway.watsonplatform.net/natural-language-understanding/api',
#     username='YOUR SERVICE USERNAME',
#     password='YOUR SERVICE PASSWORD')
import os
metadocs_path = f'./{query}/meta-docs/'
try:
	os.mkdir(metadocs_path)
except FileExistsError:
	pass
fnames = sorted(os.listdir(f'{query}/docs/'), key=lambda x: int(x.split('-')[1].split('.')[0]))
for f in fnames:
	print(f)
	try:
		response = service.analyze(
			text=open(f'./{query}/docs/' + f, 'r').read(),
			features=Features(entities=EntitiesOptions(),
			keywords=KeywordsOptions(),
			concepts=ConceptsOptions(),
			categories=CategoriesOptions(),
			sentiment=SentimentOptions(),
			emotion=EmotionOptions(),
		#   semantic_roles=SentimentOptions()
		#   relations=RelationsOptions()
		#   metadata=MetadataOptions(),
			)).get_result()
	except WatsonApiException as ex:
		print(f"Failed with status code   {str(ex.code)}: {ex.message}")
	resp = json.dumps(response, indent=2)
	fjson = open(metadocs_path + f"{f.split('.')[0]}.json", 'w')
	fjson.write(resp)
	fjson.close()