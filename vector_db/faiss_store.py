from embeddings.embedder import github_embedding, jira_embedding
import faiss 
import numpy as np

dimension = github_embedding.shape[1]

github_index = faiss.indexFlatL2(dimension)
jira_index = faiss.indexFlatL2(dimension)

github_index.add(np.array(github_embedding))
jira_index.add(np.array(jira_embedding))

