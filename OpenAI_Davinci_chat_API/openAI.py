#!/usr/bin/env python3

# import os
import openai
import sys

userQuestion =  sys.argv[1]
#input("Enter your question:")

start_sequence = "\nAI: "
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=userQuestion,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

#print (response)

#print ("--------------------")


print(response["choices"][0]["text"])

# parse response:
#textOnlyResponse = json.loads(response)
#print(textOnlyResponse["choices"])

