import requests

from bs4 import BeautifulSoup


def fetch_problem_body(problem_id: int) -> str:
    """Fetch the problem body from Baekjoon with provided `problem_id`

    Parameters:
        problem_id: The ID identifying problem

    Returns:
        The problem body

    """
    url = f"https://acmicpc.net/problem/{problem_id}"
    response = requests.get(url)

    # Raise error if status error ocurred
    response.raise_for_status()

    soup = BeautifulSoup(response.text)
    problem_body = soup.find(id="problem-body")

    return str(problem_body)
