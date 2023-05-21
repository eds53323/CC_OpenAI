import os
import openai 

openai.api_key = "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"

messages=[
        {"role": "system", "content": "you're a doctor"},
]
def chat(text):
    global messages
    messages.append({"role": "user", "content": text})
    return openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )["choices"][0]["message"]["content"]

result = chat( "血壓量測結果 高血壓300 低血壓30 是否正常? 有甚麼須注意的事情")
print(result)
conda config --show-sources
