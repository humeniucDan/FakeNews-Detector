import json

from langchain_core.prompts import ChatPromptTemplate
from models import gemma3

template = """
YOU ARE AN ENTITY RELATIONSHIP EXTRACTOR

Extract from the following text the entities and the relations and return them in a JSON format like the example bellow:

The brown dog and the white cat are running in the yard. 
[
  {{
    "entity1":"The Dog",
    "entity2":"the yard", 
    "relation":"running" 
  }},
  {{
    "entity1":"The Dog",
    "entity2":"brown",
    "relation":"is"
  }},

  {{
    "entity1":"The cat",
    "entity2":"the yard", 
    "relation":"running" 
  }},
  {{
    "entity1":"The cat",
    "entity2":"white",
    "relation":"is"
  }},
] 

{news_article}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | gemma3.gemma3_model

def extract_entity_relations(news_article:str):
    text_results = chain.invoke({'news_article': news_article})
    text_json = text_results.strip('`').removeprefix("json\n").removesuffix("```")
    parsed_list = json.loads(text_json)
    return parsed_list

news_article = "[BREAKING] Lesbian Chinese Billionaires, Meng Mei Qi and Wu Xuan Yi, marry. Making them the richest couple alive."
parsed_list = extract_entity_relations(news_article)

print("Successfully parsed data:")
for item in parsed_list:
    print(item)
