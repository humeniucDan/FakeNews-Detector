from pre_procesing.article_extractor import extract_main_article
from processing.comparator import semantic_comparison
from processing.gemma3.gemma3 import extract_entity_relations
from processing.validator import article_text, validate_decide
from web_search.bs_web_scraper import search_web
from web_search.web_extractor import extract_text

# url = ''
# article_text = extract_text(url) #todo OK
# article_information = extract_main_article(article_text)
# OR PROVIDE THE TEXT AS IS
article_information = '[BREAKING] Lesbian Chinese Billionaires, Meng Mei Qi and Wu Xuan Yi, marry. Making them the richest couple alive.'
print(article_information)

statements = extract_entity_relations(article_information) #todo OK

validation_results = []
for statement in statements:
    statement_text = statement['entity1'] + ' ' + statement['relation'] + ' ' + statement['entity2']
    print(statement_text)
    statement_score = 0
    web_results = search_web(statement_text) #todo OK
    for url in web_results:
        validation_article_text = extract_text(url)
        validation_article_info = extract_main_article(validation_article_text)
        statement_score += validate_decide(statement_text, validation_article_info) + semantic_comparison(statement_text, validation_article_info)
        # statement_score += website_trust[result] * validate_decide(statement_text, validation_article_info)
    validation_results.append({'statement_text':statement_text, 'statement_score': statement_score})

for validation_res in validation_results:
    print(validation_res)
