from data.githubsource import load_github_docs
from data.jirasource import load_jira_docs
from sentence_transformers import SentenceTransformer
import os

from dotenv import load_dotenv

from main import GITHUB_TOKEN, JIRA_TOKEN

load_dotenv()

repo_name = "nihalshetty3/Hpe-mini-project"
github_docs = load_github_docs(os.getenv(GITHUB_TOKEN) , repo_name)
jira_docs = load_jira_docs(
    "https://nihalhshetty30.atlassian.net",
    "nihalhshetty30@gmail.com",
    os.getenv("JIRA_TOKEN")
)

model = SentenceTransformer("all-MiniLM-L6-v2")

github_embedding = model.encode(github_docs)

jira_embedding = model.encode(jira_docs)

print("Github embedding shape:" , github_embedding.shape)
print("Jira embedding shape:" , jira_embedding.shape)