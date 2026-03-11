import ollama
def explain_similarity_ollama(github_doc , jira_doc):
    prompt = f"""
    You are analyzing information from two different sources.
    Determine whether the following two contents are related 
    and breifly explain the relationship between them.
    
    Github content: {github_doc}
    Jira content : {jira_doc}
    
    Explaination:
    """
    
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
    )
    
    return response['message']['content']