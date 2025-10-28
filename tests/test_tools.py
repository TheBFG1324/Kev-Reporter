import pytest
from tools.functions import get_mitre_cve_context, get_google_news_context, search_exploit_db, gather_context


# Test mitre function
@pytest.mark.asyncio
async def test_get_mitre_cve_context_function():
    r = await get_mitre_cve_context(cve="CVE-2025-54236")
    print(r)
    assert r is not None

# Test google news function
@pytest.mark.asyncio
async def test_get_google_news_context_function():
    r = await get_google_news_context(cve="CVE-2025-54236")
    print(r)
    assert r is not None

# Test exploitDB function
@pytest.mark.asyncio
async def test_search_exploit_db_function():
    q = ["Windows 11 Reverse TCP Shellcode", "ChiefsAreTheBestTeam"]
    r = await search_exploit_db(queries=q)
    print(r)
    for item in r:
        assert item is not None

