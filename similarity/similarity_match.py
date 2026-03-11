
from data.githubsource import load_github_docs
from data.jirasource import load_jira_docs
from embeddings.embedder import github_embedding , jira_embedding

from sklearn.metrics.pairwise import cosine_similarity

from llm.gemini_llms import explain_similarity
from llm.ollama_llm import explain_similarity_ollama

import os


repo_name ="nihalshetty3/Hpe-mini-project"

github_docs = load_github_docs(os.getenv("GITHUB_TOKEN") , repo_name)

jira_docs = load_jira_docs(
    "https://nihalhshetty30.atlassian.net",
    "nihalhshetty30@gmail.com",
    os.getenv("JIRA_TOKEN")
)

similarity_matrix = cosine_similarity(github_embedding , jira_embedding)

print("\nSimilarity Matrix:\n")
print(similarity_matrix)



matched_pairs=[]
unrelated_pairs=[]


for i, g_doc in enumerate(github_docs):

    best_match_index = similarity_matrix[i].argmax()
    score = similarity_matrix[i][best_match_index]
    
    pair=(g_doc , jira_docs[best_match_index], score)
   
    if score>=0.6:
        matched_pairs.append(pair)
    else:
        unrelated_pairs.append(pair)

print("\n================ MATCHED PAIRS (HIGH SIMILARITY) ================\n")

for g_doc, j_doc, score  in matched_pairs:

    print("Github:", g_doc)
    print("Jira:", j_doc)
    print("Similarity Score:", score)

    try:
        gemini_explanation = explain_similarity(g_doc, j_doc)
        print("\nGemini explanation:\n") 
        print(gemini_explanation)

    except Exception as e:
        print("Gemini explanation (skipped):", str(e))

    try:
        ollama_explanation = explain_similarity_ollama(g_doc, j_doc)
        print("\nOllama explanation:\n") 
        print(ollama_explanation)

    except Exception as e:
        print("Ollama explanation (skipped):", str(e))

    print("-" * 60)

print("\n================ UNRELATED / LOW SIMILARITY PAIRS ================\n")

for g_doc , j_doc , score in unrelated_pairs:
    
    print("Github:" , g_doc)
    print("Jira:" , j_doc)
    print("Similarity Score:" , score)
    
    try:
        gemini_explanation = explain_similarity(g_doc , j_doc)
        print("\nGemini Explaination:\n")
        print(gemini_explanation)
    
    except Exception as e:
        print("Gemini explaination (skipped):" , str(e))
        
    try:
        ollama_explanation = explain_similarity_ollama(g_doc , j_doc)
        print("\nOllama Explaination:\n")
        print(ollama_explanation)
        
    except Exception as e:
        print("Ollama Explaination (skipped):" , str(e))
        
    print("-" * 60)