from pydantic import BaseModel
from typing import List, Optional

# Required parameter for Mitre tool
class MitreArgs(BaseModel):
    cve: str

# Required parameter for Google News tool
class GoogleNewsArgs(BaseModel):
    cve: str

# Required parameters for ExploitDB tool
class ExploitDBArgs(BaseModel):
    queries: List[str]

# Data object to call all tools to gather KEV context
class BatchToolRequest(BaseModel):
    mitre: MitreArgs
    google_news: GoogleNewsArgs
    exploit_db: ExploitDBArgs
    tags: List[str]

# Data object to hold gather_context function responses and tags
class ContextToolResponse(BaseModel):
    mitre_response: Optional[str]
    google_news_response: Optional[str]
    exploitdb_response: Optional[List[str]]
    tags: Optional[List[str]]