import json
import requests

def getRepositories(gitHubUsername):
    repoSummaryList = []
    
    try:
        url = "https://api.github.com/users/" + gitHubUsername + "/repos"
    except TypeError:
        return "Username must be entered as a string"
        
    
    repoInfo = requests.get(url)
    JsonExtract = json.loads(repoInfo.content)

    for i in JsonExtract:
        commits = requests.get("https://api.github.com/repos/" + gitHubUsername + "/" + i['name'] + "/commits")
        JsonCommits = json.loads(commits.content)
        count = 0
        for j in JsonCommits:
            count = count + 1
        repoSummaryList.append([i['name'], count])
    return repoSummaryList