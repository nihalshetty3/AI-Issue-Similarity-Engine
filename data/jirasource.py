

from jira import JIRA
def load_jira_docs(server , email , token):
    
    jira = JIRA(
        server=server,
        basic_auth = (email , token)
    )
    
    issues = jira.search_issues("project = SCRUM order by created DESC" , maxResults=50)
    
    docs=[]
    
    for issue in issues:
        summary = issue.fields.summary
        description= issue.fields.description
        
        text = summary + " "+(description if description else "")
        
        docs.append(text)
        
    return docs
    
    