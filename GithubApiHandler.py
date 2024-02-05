import os
from urllib.parse import urlparse
import asyncio
from github import Github
import inflect

async def GetGithubRepoDetails(github_url):
    # Use a GitHub API token securely
    github_token = os.getenv('GITHUB_TOKEN')

    if not github_token:
        return "GitHub token not provided."

    try:
        g = Github(github_token)

        parsed_url = urlparse(github_url)
        path_parts = parsed_url.path.split("/")
        username = path_parts[1]  # GitHub username is the second element in the path

        user = g.get_user(username)
        user_repos = user.get_repos()

        if user_repos.totalCount > 0:
            repo_count = inflect.engine().number_to_words(user_repos.totalCount)
            unique_languages = set(repo.language for repo in user_repos if repo.language)
            repo_lang = ', '.join(unique_languages)
            git_result = f'Candidate has {repo_count} repositories in GitHub and skills based on {repo_lang}'
        else:
            git_result = 'Candidate has no repositories on GitHub'
    except Exception as e:
        print(f"Error: {e}")
        git_result = ''

    return git_result

def NumberToWords(number):
    p = inflect.engine()
    return p.number_to_words(number)