import google.generativeai as genai
genai.configure(api_key="AIzaSyCREuLlm06oh3JvY43m2tYRDkKJ15adPiI")

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_similarity(github_doc , jira_doc):
    prompt = f"""
    
    You are analyzing content from two different sources.
    Determine whether these two peices of contents are related 
    and explain the relationship briefly.
    
    GitHub content: {github_doc}
    
    Jira Content : {jira_doc}
    
    Explaination:
    """
    
    response = model.generate_content(prompt)
    return response.text