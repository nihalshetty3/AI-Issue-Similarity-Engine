from ingest import create_vector_store
from agent import create_agent
import os

Threshold = 0.6

if not os.path.exists("vector_db"):
    create_vector_store()

qa_chain, web_search , llm = create_agent()

while True:
    query = input("\nAsk a question:")
    
    if query.lower() == "exit":
        break
    
    docs_with_scores = qa_chain.retriever.vectorstore.similarity_search_with_score(query)
    
    best_doc, score = docs_with_scores[0]
    
    print("\nBest similarity disatance:", score)
    
    if score > Threshold:
        # not related
        print("\nSource: Web Search")
        results = web_search.run(query)
        
        prompt = f"""
        Answer the following question using the web search results.
        
        Question: {query}
        
        Web Search Results: 
        {results}
        
        Give a clear and  concise answer.
        """
        
        response = llm.invoke(prompt)
        if hasattr(response , "content"):
            answer = response.content
        else:
            answer = str(response)
        
        
    else:
        #related query
        print("\nSource: Vector DB(Contextual answer)")
        response = qa_chain.invoke({"query": query})
        
        if isinstance(response , dict):
            answer = response.get("result") or response.get("output_text") or ""
            
        else:
            answer = str(response)
            
    print("\nAnswer:\n", answer)
    