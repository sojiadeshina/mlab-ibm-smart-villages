import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features

def analyze():
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='f482a680-b22f-44cb-90ec-f17f958e7efc',
        password='BLMaJkqErAkM')

    response = natural_language_understanding.analyze(
        text="I was a prisoner in my own home. I couldn't look out the window. \
        My mom was in the hospital for surgery. I couldn't go to the hospital to see my mother unless he was with me..\
        I wasn't allowed to have a cell phone. His excuse was he was afraid to lose me cause he loved me so much and that \
        was his way of showing me that he loved me",
        features=[features.Entities(), features.Keywords(), features.Concepts(), features.Sentiment()])

    decoder = json.JSONDecoder()

    decoded_response = decoder.decode(json.dumps(response, indent=2))

if __name__ == "__main__":
    analyze()