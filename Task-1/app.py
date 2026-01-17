import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification

labels_map = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}

st.title("📰 News Topic Classifier (BERT)")

tokenizer = BertTokenizer.from_pretrained("news_bert_model")
model = BertForSequenceClassification.from_pretrained("news_bert_model")
model.eval()

text = st.text_area("Enter News Headline")

if st.button("Classify"):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )
    with torch.no_grad():
        outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    st.success(f"Predicted Category: **{labels_map[pred]}**")
