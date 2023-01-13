#!/usr/bin/env python3

import os
import openai
import sys

userQuestion =  sys.argv[1]

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI: "
restart_sequence = "\nHuman: "

userQuestion = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "+userQuestion+"\nAI:"

response = openai.Completion.create(
  model="text-babbage-001",
  prompt=userQuestion,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

print(response["choices"][0]["text"])


