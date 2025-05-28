from pre_procesing.article_extractor import extract_main_article
from processing.comparator import semantic_comparison
from processing.gemma3.gemma3 import extract_entity_relations
from processing.validator import validate_decide
from web_search.bs_web_scraper import search_web
from web_search.web_extractor import extract_text

# Input Section
# url = ''
# article_text = extract_text(url)  # TODO: Uncomment if using a URL
# article_information = extract_main_article(article_text)

# OR provide the article text directly
article_information = """
CAlin Georgescu a iesit presedintele Romaniei.
"""

print("\n======================")
print("🔍 Original Article Information")
print("======================")
print(article_information, flush=True)

# Extract Entity Relations
print("\n======================")
print("🔍 Extracting Entity-Relation Statements")
print("======================")
statements = extract_entity_relations(article_information)

for statement in statements:
    statement_text = statement['entity1'] + ' ' + statement['relation'] + ' ' + statement['entity2']
    print(f"➡️ Statement: {statement_text}")

# Validation Section
print("\n======================")
print("✅ Validating Statements via Web Search")
print("======================")
validation_results = []

for statement in statements:
    statement_text = statement['entity1'] + ' ' + statement['relation'] + ' ' + statement['entity2']
    print(f"\n--- Validating: {statement_text} ---")

    statement_score = 0
    web_results = search_web(statement_text)
    print(f"🔗 Found {len(web_results)} web results.")

    for url in web_results:
        print(f"🌐 Checking URL: {url}")
        validation_article_text = extract_text(url)
        validation_article_info = extract_main_article(validation_article_text)

        validation_score = float(validate_decide(statement_text, validation_article_info))
        semantic_comparison_score = float(semantic_comparison(statement_text, validation_article_info))
        score = validation_score + semantic_comparison_score
        print(f"📊 Intermediate Score from this source: {score}")

        statement_score += score

    validation_results.append({
        'statement_text': statement_text,
        'statement_score': statement_score
    })

# Final Results
print("\n======================")
print("📋 Final Validation Results")
print("======================")
for res in validation_results:
    print(f"\n📝 Statement: {res['statement_text']}")
    print(f"✅ Final Score: {res['statement_score']}")
