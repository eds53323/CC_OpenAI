# pip install --upgrade openai
import os
import openai

openai.api_key = "sk-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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="血壓量測結果 高血壓190 低血壓30 是否正常? 有甚麼須注意的事情",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response) 1234 no4 no5 no6 no7 


print(response["choices"][0]["text"])
