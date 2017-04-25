import json
import nltk
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features

entity_types = set(['Anatomy', 'Drug', 'HealthCondition', 'JobTitle', 'Location', 'Person', 'NaturalEvent'])

def analyze(text, threshold=0.5):
    text = text.encode('ascii', errors='ignore')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='f482a680-b22f-44cb-90ec-f17f958e7efc',
        password='BLMaJkqErAkM')

    response = natural_language_understanding.analyze(
        text=text,
        features=[features.Entities(), features.Keywords(), features.Concepts(), features.Sentiment()])

    decoder = json.JSONDecoder()

    decoded_response = decoder.decode(json.dumps(response, indent=2))
    language = decoded_response["language"]
    keywords = decoded_response["keywords"]
    entities = decoded_response["entities"]
    concepts = decoded_response["concepts"]
    sentiment = decoded_response["sentiment"]

    keywords = sorted(keywords, key=lambda x:-x['relevance'])
    keywords = [keyword for keyword in keywords if keyword['relevance'] >= threshold]
    keywords = [keyword['text'] for keyword in keywords]

    entities = sorted(entities, key=lambda x:-x['relevance'])
    entities = [entity for entity in entities if entity['relevance'] >= threshold]
    entities = [(entity['type'], entity['text']) for entity in entities]

    concepts = sorted(concepts, key=lambda x:-x['relevance'])
    concepts = [concept for concept in concepts if concept['relevance'] >= threshold]
    concepts = [concept['text'] for concept in concepts]

    sentiment = (sentiment['document']['label'], sentiment['document']['score'])

if __name__ == "__main__":
    example_text = "I wasnt allowed to go to the toilet. Violence and abuse is a form of control. \
        He actually would not hide abuse from the children, sometimes he would have outbursts in front\
         of them and, somehow, I still believed it was better for me to stay for the good of the children, \
         not knowing that for children who witness the abuse it's as if they experience it themselves. I lost \
         the support of my own family, and friends. The emotional abuse gradually became more intense, and then \
         the physical abuse set in. Over time, it will get so stressful that you develop the physical symptoms, even \
         though you try to ignore it. Eventually, your body will accumulate enough stress that it manifests itself in \
         physical symptoms. I suffered from excessive bleeding and chronic fatigue, and when that happened, my colleague\
          picked it up because she was in a similar situation before. I tried to find a way to solve the problem on my own.\
           Eventually, the stress meant I was forced to leave my job as a tax accountant."
    analyze(example_text.encode('ascii', errors='ignore'))