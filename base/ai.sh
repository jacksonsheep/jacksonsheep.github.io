if [ -n "$@" ];then
echo $@
#curl -X POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions -H "Authorization: Bearer sk-dfb4196dc2d14942acf3c9c1fb327f99" -H "Content-Type: application/json" -d '{
#    "model": "qwen-plus",
#    "messages": [
#        {
#            "role": "system",
#            "content": "You are a helpful assistant."
#        },
#        {
#            "role": "user",
#            "content": "$@"
#        }
#    ]
#}'
else
  echo 'input question invaild'
fi
