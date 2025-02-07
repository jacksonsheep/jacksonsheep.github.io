import os
from openai import OpenAI
from json import loads
from sys import argv

client = OpenAI(
    api_key="sk-dfb4196dc2d14942acf3c9c1fb327f99",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

if len(argv) < 2:
  mode = "qwen-plus"
else:
  mode = argv[1]
question=input('Q:')
if question :
  completion = client.chat.completions.create(
      model= mode, #"qwen-plus", # deepseek-r1
      messages=[
          {'role': 'system', 'content': 'You are a helpful assistant.'},
          {'role': 'user', 'content': question}
      ],
  )
  test = completion.model_dump_json()
else :
  test = '{"id":"chatcmpl-e64e2874-2bb6-97a3-8e9a-e5150281535a","choices":[{"finish_reason":"stop","index":0,"logprobs":null,"message":{"content":"我是来自阿里云的超大规模语言模型，我叫通义千问。","refusal":null,"role":"assistant","audio":null,"function_call":null,"tool_calls":null}}],"created":1739187847,"model":"qwen-plus","object":"chat.completion","service_tier":null,"system_fingerprint":null,"usage":{"completion_tokens":17,"prompt_tokens":22,"total_tokens":39,"completion_tokens_details":null,"prompt_tokens_details":{"audio_tokens":null,"cached_tokens":0}}}'

print(test)
body=loads(test)
print('\nAns: '+ body["choices"][0]["message"]["content"])
print('usage:' + str(body["usage"]["total_tokens"]))

