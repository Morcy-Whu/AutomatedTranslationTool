#!/usr/bin/env python3
# translator.py
from transformers import MarianMTModel, MarianTokenizer
import sys

# 1. 加载模型（只加载一次）
model_name = "Helsinki-NLP/opus-mt-zh-en"
tokenizer = MarianTokenizer.from_pretrained(model_name,local_files_only=True)
model = MarianMTModel.from_pretrained(model_name,local_files_only=True)


def translate(text: str) -> str:
    """
    Translate a Chinese string into English using MarianMT.

    Args:
        text (str): Text to translate.
    Returns:
        str: Translated English text.
    """

    # 模型的输入必须是列表，因此把单个字符串放进 list
    src_text = [text]

    # 编码文本
    inputs = tokenizer(src_text, return_tensors="pt", padding=True)

    # 生成翻译结果
    translated = model.generate(**inputs)

    # 解码输出
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

    result = " ".join(tgt_text)

    return result

# -------------------------------
# 命令行入口
# -------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py \"要翻译的文本\"")
        sys.exit(1)

    input_text = sys.argv[1]
    output = translate(input_text)
    print(output)