import os
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
repo_info = next(w.repos.list(path_prefix=os.getcwd()))
print(repo_info.head_commit_id)
