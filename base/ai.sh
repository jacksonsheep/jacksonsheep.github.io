#!/bin/bash

model="qwen-plus"
prompt="You are a helpful assistant."

if  [ $# -ne 0 ];then
   request="$*"
   json_obj=$(printf '{"model": "%s", "messages": [{"role": "system","content": "%s"},{"role": "user","content": "%s"}]}' "$model" "$prompt" "$request")
   #echo "$json_obj"
   curl -X POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions -H "Authorization: Bearer sk-dfb4196dc2d14942acf3c9c1fb327f99" -H "Content-Type: application/json" -d "$json_obj"
else
  echo 'error: input question invaild'
fi
