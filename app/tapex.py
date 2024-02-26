from transformers import TapexTokenizer, BartForConditionalGeneration
import pandas as pd

model_name = "microsoft/tapex-large-finetuned-wtq"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = TapexTokenizer.from_pretrained(model_name)


def execute_query(query, data):
    table = pd.DataFrame.from_records(data)
    table = table.astype(str)

    queries = [query]

    encoding = tokenizer(table=table, query=queries, padding=True, return_tensors="pt", truncation=True)
    outputs = model.generate(**encoding)
    ans = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return ans[0]
