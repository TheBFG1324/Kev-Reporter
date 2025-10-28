from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

# Data object for base vulnerability data
class Vulnerability(BaseModel):
    cveID: str
    vendorProject: str
    product: str
    vulnerabilityName: str
    dateAdded: date
    shortDescription: str
    requiredAction: str
    dueDate: date
    knownRansomwareCampaignUse: str
    notes: Optional[str]
    cwes: List[str]

# Data object for CISA catalog of vulnerabilities
class CISACatalog(BaseModel):
    title: str
    catalogVersion: str
    dateReleased: datetime
    count: int
    vulnerabilities: List[Vulnerability]
