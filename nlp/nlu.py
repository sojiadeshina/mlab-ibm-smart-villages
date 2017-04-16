import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='f482a680-b22f-44cb-90ec-f17f958e7efc',
    password='BLMaJkqErAkM')

response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords(), features.Concepts()])

print(json.dumps(response, indent=2))