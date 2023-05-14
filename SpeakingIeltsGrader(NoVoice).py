import requests as r
import json
import random




url = "https://api.voicegpt.us/v1/histories/test-user-get-chatGPT-stream"

headers = {
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2M2U3YmZmZmUwYTk5ZGZiNDk3NzBmOTAiLCJpYXQiOjE2ODM5OTI4MzEsImV4cCI6MTY4NDg1NjgzMX0.Z3XdOeb6R3x-iThLMkmR4YR_jsNtoZkeulQqYUfRokU",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0"
}

body = {
    "data":"hi",
    "type":"CHAT"
}

with open("AllPrompts.json","r") as f:
    allpromts = json.loads(f.read())

choice = random.choice(allpromts["alltests"])
print("Part ",choice["task_id"], ": ")
result = "rate my part " +choice["task_id"]+" speaking IELTS with following questions and answer how many out of ten and evaluate it:\n"

if choice["task_id"] == "1" or choice["task_id"] == "3":
    for prompt in choice["task_prompts"]:
        print(prompt)
        result += "Question: " + prompt + "\nAnswer: "
        speech = input("Your answer:\n")
        result +=  speech + "\n\n"
        print("\n")
else:
    print(*choice["task_prompts"],sep="\n")
    result += "Question:\n" + '\n'.join(choice["task_prompts"]) + "\nAnswer:\n"
    speech = input("Your answer:\n")
    result += speech + "\n\n"
    print("\n")

body["data"] = result
res = r.request("POST",url,json=body,headers=headers).content.decode("utf-8").split('\n\n')


print("\nAI IELTS GRADER:")
speech = ""
for ans in res[1:-3]:
    val = json.loads(ans[6:])
    print(val["choices"][0]["delta"]["content"],end="")
    speech += val["choices"][0]["delta"]["content"]
