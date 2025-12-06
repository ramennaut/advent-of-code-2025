import os
import urllib.request
from dotenv import load_dotenv

load_dotenv()

def get_input(year: int, day: int) -> list[str]:
    """
    Fetch input for Advent of Code puzzle given year and day and return it as raw text.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_cookie = os.getenv("AOC_SESSION")
    email = os.getenv("AOC_USER_AGENT_EMAIL", "example@example.com")
    
    if not session_cookie:
        raise ValueError("AOC_SESSION is missing.")
    
    req = urllib.request.Request(
        url,
        headers = {
            "Cookie": f"session={session_cookie}",
            "User-Agent": f"github.com/ramennaut/advent-of-code-2025 by {email}",
        },
    )
    
    with urllib.request.urlopen(req) as response:
        file = response.read().decode("utf-8")
        
    return file.strip()