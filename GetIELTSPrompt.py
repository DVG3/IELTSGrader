import requests
from bs4 import BeautifulSoup 
import json
url = "https://www.examword.com/ielts-practice/speaking-exam-question"

def GetPrompts():
    html = requests.get(url)
    s = BeautifulSoup(html.content,'html.parser')
    questions = {"alltests":[]}
    with open("AllPrompts.json","w") as f:
        for i in range(1,60 + 1):
            task = s.find(id=f"side2CoreFilerRef{i}")
            task_id = task.find("div").text[-1]
            task_prompts = task.get_text(separator="\n")
            task_prompts = task_prompts[23:task_prompts.find("Recent Tests:")-1].split('\n')
            print(task_prompts)
            #task_prompts = list(map(lambda x: x.get_text(strip=True),task.find_all("li")))
            questions["alltests"].append({"task_id":task_id, "task_prompts":task_prompts})
        f.write(json.dumps(questions))





