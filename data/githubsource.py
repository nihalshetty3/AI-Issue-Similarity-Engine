
    
from github import Github
    
def load_github_docs(token , repo_name):
    g = Github(token)
    
    repo = g.get_repo(repo_name)
    
    issues = repo.get_issues(state="all")
    
    docs=[]
    
    for issue in issues:
        text = issue.title + " " + (issue.body if issue.body else "")
        docs.append(text)
         
    return docs
        

