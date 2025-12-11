from transformers import MarianMTModel, MarianTokenizer

# 选择语言模型，比如中译英
model_name = "Helsinki-NLP/opus-mt-zh-en"


tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


src_text = ["你好，世界！", "我喜欢使用人工智能模型。"]


inputs = tokenizer(src_text, return_tensors="pt", padding=True)


translated = model.generate(**inputs)


tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

result = " ".join(tgt_text)
print(result)

# Output
# Hello, world! I like to use artificial intelligence models.