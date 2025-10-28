import requests
import asyncio
import subprocess
import os

from dotenv import load_dotenv
from typing import List, Optional
from agents import function_tool
from models.context_functions import BatchToolRequest, ContextToolResponse

load_dotenv()

@function_tool
def send_email_report(report: str) -> str:
    '''
    Sends an email report of recent CISA KEV to security research team.

    Args:
        report: A string report in markdown.
    Returns:
        A mock PDF report
    '''
    return report

@function_tool
async def gather_context(context_request: BatchToolRequest) -> ContextToolResponse:
    '''
    Gathers additional context for a recent CISA KEV.

    Args:
        context_request: A BatchToolRequest pydantic object
    Returns:
        A ContextToolResponse pydantic Object
    '''
    mitre_args = context_request.mitre.cve
    google_news_args = context_request.google_news.cve
    exploitdb_args = context_request.exploit_db.queries
    tags = context_request.tags
    mitre_resp, google_resp, exploitdb_resp = await asyncio.gather(get_mitre_cve_context(mitre_args), get_google_news_context(google_news_args), search_exploit_db(exploitdb_args))
    context = ContextToolResponse(mitre_response=mitre_resp, google_news_response=google_resp, exploitdb_response=exploitdb_resp, tags=tags)
    return context

async def get_mitre_cve_context(cve: str, timeout: int = 10) -> Optional[str]:
    '''Function to fetch additional CVE data from MITRE'''
    url = f"https://cveawg.mitre.org/api/cve/{cve}"
    try:
        resp = await asyncio.to_thread(requests.get, url, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except Exception:
        return None

async def get_google_news_context(cve: str, timeout: int = 10) -> Optional[str]:
    '''Function to get relevant Google News article of a given CVE'''
    url = "https://google-news13.p.rapidapi.com/search"
    params = {"keyword": cve, "lr": "en-US"}
    headers = {
        "x-rapidapi-host": "google-news13.p.rapidapi.com",
        "x-rapidapi-key": os.getenv("X_RAPIDAPI_KEY"),
    }
    try:
        resp = await asyncio.to_thread(requests.get, url, headers=headers, params=params, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except Exception:
        return None

async def search_exploit_db(queries: List[str], timeout: int = 10) -> Optional[List[str]]:
    '''Function to search ExploitDB for relevant exploits'''
    def _run_searchsploit(q: str) -> str:
        try:
            proc = subprocess.run(["searchsploit", q], capture_output=True, text=True, timeout=timeout)
            if proc.returncode != 0:
                return proc.stderr.strip() or proc.stdout.strip()
            return proc.stdout.strip()
        except Exception:
            return None
    tasks = [asyncio.to_thread(_run_searchsploit, q) for q in queries]
    return await asyncio.gather(*tasks)

