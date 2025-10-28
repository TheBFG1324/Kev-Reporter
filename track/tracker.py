import requests

from models.kevs import Vulnerability, CISACatalog
from typing import List, Optional

# Class to routinely check CISA site for new KEVs 
class KevTracker:
    def __init__(self, url: str = 'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json', start_count: int = 0):
        self._url = url
        self._start_count = start_count

    def new_items(self) -> Optional[List[Vulnerability]]:
        '''
        This method checks the CISA site for new vulnerabilities. Returns a list of vulnerabilities if found, otherwise returns None
        '''
        data = requests.get(self._url).json()
        catalog = CISACatalog(**data)
        if catalog.count <= self._start_count:
            return None
        return self._filter_kevs(catalog)

    def _filter_kevs(self, catalog: CISACatalog) -> List[Vulnerability]:
        '''
        Helper method to filter new KEVS based on a start count
        '''
        if self._start_count == 0:
            return catalog.vulnerabilities
        return catalog.vulnerabilities[:catalog.count - self._start_count]