import github
from urllib.parse import urlparse
import inflect
import os
async def GetGithubRepoDetails(github_url):
    # Use a GitHub API token securely
    github_token = os.getenv('GITHUB_TOKEN')
    # g = github.Github(github_token)
    g = await github.GHClient()

    username = ''
    gitResult = ''

    if github_url:
        parsed_url = urlparse(github_url)
        path_parts = parsed_url.path.split("/")
        print(path_parts)
        username = path_parts[0]

    try:
        user = g.get_user(username)
        print(user.name)
        user_repos = user.get_repos()

        if user_repos.totalCount > 0:
            repoCount = NumberToWords(user_repos.totalCount)
            # Use a set to store unique languages
            unique_languages = set(repo.language for repo in user_repos if repo.language)
            
            repoLang = ', '.join(unique_languages)
            gitResult = f'Candidate has {repoCount} repositories in GitHub and skills based on {repoLang}'
        else:
            gitResult = 'Candidate has no repositories on GitHub'
    except Exception as e:
        print(e)
        gitResult = ''

    return gitResult

def NumberToWords(number):
    p = inflect.engine()
    return p.number_to_words(number)

