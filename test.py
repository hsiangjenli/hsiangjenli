import requests

GITHUB_API = "https://api.github.com/"

def get_github_user_repo(user):
    url = GITHUB_API + "users/{}/repos".format(user)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_tutorial_repos(user):
    repos = get_github_user_repo(user)
    tutorial_repos = [repo['name'] for repo in repos if repo['name'].startswith('tutorial')]
    return tutorial_repos
    
# if __name__ == '__main__':
#     repos = get_github_user_repo('hsiangjenli')
#     tutorial_repos = [repo for repo in repos if repo['name'].startswith('tutorial')]