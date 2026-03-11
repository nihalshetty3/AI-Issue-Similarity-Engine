from data.githubsource import load_github_docs
from data.jirasource import load_jira_docs
from dotenv import load_dotenv
import os

load_dotenv(".env")


# Read GitHub token from environment variable (set GITHUB_TOKEN in your shell)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")

repo_name = "nihalshetty3/Hpe-mini-project"


github_docs = load_github_docs(GITHUB_TOKEN, repo_name)
print("Github docs loaded", len(github_docs))


JIRA_SERVER = "https://nihalhshetty30.atlassian.net"
JIRA_EMAIL = "nihalhshetty30@gmail.com"


jira_docs = load_jira_docs(JIRA_SERVER, JIRA_EMAIL, JIRA_TOKEN)
print("Jira docs loaded", len(jira_docs))