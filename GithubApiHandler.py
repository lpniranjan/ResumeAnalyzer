import github
from urllib.parse import urlparse
import inflect

def GetGithubRepoDetails(github_url):
    # Use a GitHub API token securely
    github_token = "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"
    g = github.Github(github_token)

    username = ''
    gitResult = ''

    if github_url:
        parsed_url = urlparse(github_url)
        path_parts = parsed_url.path.split("/")
        username = path_parts[1]

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

