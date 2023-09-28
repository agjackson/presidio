from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

#for the specific list part
from presidio_analyzer import PatternRecognizer

# redacts PII: credit card numbers, names, locations, phone numbers, SSNs, 
# and financial data

#titles_list = ["Sir","Ma'am","Madam","Mr.","Mrs.","Ms.","Miss","Dr.","Professor",]

#titles_recognizer = PatternRecognizer(supported_entity="TITLE", deny_list=titles_list)

text="This is Will, he's my son. My name is Jessica. His name is Mr. Jones and his phone number is 212-555-5555. I suspect Professor Plum, in the Dining Room, with the candlestick in Chicago. When Dad was the VP for IBM, he told Anthony that he would leave the company for 12 years to go to Indonesia."


#result = titles_recognizer.analyze(text, entities=["TITLE"])
#print(f"Result:\n {result}")


# Set up the engine, loads the NLP module (spaCy model by default) 
# and other PII recognizers
analyzer = AnalyzerEngine()
#analyzer.registry.add_recognizer(titles_recognizer)

# Call analyzer to get results
results = analyzer.analyze(text=text,language='en')

print(results)

# Analyzer results are passed to the AnonymizerEngine for anonymization

anonymizer = AnonymizerEngine()
 
anonymized_text = anonymizer.anonymize(text=text,analyzer_results=results)

print(anonymized_text)