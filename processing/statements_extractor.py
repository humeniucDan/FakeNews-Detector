from transformers import BertTokenizerFast, BertForTokenClassification
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "AventIQ-AI/named-entity-recognition-for-information-extraction"
model = BertForTokenClassification.from_pretrained(model_name).to(device)
tokenizer = BertTokenizerFast.from_pretrained(model_name)

# def extract_sops(text:str):
#     openie = pipeline("text2text-generation", model="aychang/bert-openie")
#  [   text = "[BREAKING] Lesbian Chinese Billionaires, Meng Mei Qi and Wu Xuan Yi, marry..."
#     output = openie(text)
#
#     return output

label_list = ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-MISC", "I-MISC"]

def predict_entities(text, model):
    tokens = tokenizer(text, return_tensors="pt", truncation=True)
    tokens = {key: val.to(device) for key, val in tokens.items()}  # Move to CUDA

    with torch.no_grad():
        outputs = model(**tokens)

    logits = outputs.logits  # Extract logits
    predictions = torch.argmax(logits, dim=2)  # Get highest probability labels

    tokens_list = tokenizer.convert_ids_to_tokens(tokens["input_ids"][0])
    predicted_labels = [label_list[pred] for pred in predictions[0].cpu().numpy()]

    final_tokens = []
    final_labels = []
    for token, label in zip(tokens_list, predicted_labels):
        if token.startswith("##"):
            final_tokens[-1] += token[2:]  # Merge subword
        else:
            final_tokens.append(token)
            final_labels.append(label)

    for token, label in zip(final_tokens, final_labels):
        if token not in ["[CLS]", "[SEP]"]:
            print(f"{token}: {label}")

if __name__ == "__main__":
    print(device)
    sample_text = "Lesbian Chinese Billionaires, Meng Mei Qi and Wu Xuan Yi, marry. Making them the richest couple alive"
    predict_entities(sample_text, model)