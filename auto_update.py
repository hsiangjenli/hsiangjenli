# %% Load necessary lib
import toml
from jinja2 import Environment, FileSystemLoader
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
    return tutorial_repos, len(tutorial_repos)


def get_repos_keywords(repos, n=5):
    keywords = []
    for repo in repos:
        keywords.extend(repo.split('-'))

    # remove tutorial in keywords
    keywords = [keyword for keyword in keywords if keyword != 'tutorial']

    # calculate keywords frequency
    keywords_freq = {}
    for keyword in keywords:
        if keyword in keywords_freq:
            keywords_freq[keyword] += 1
        else:
            keywords_freq[keyword] = 1
    
    # return top n keywords
    keywords_freq = sorted(keywords_freq.items(), key=lambda x: x[1], reverse=True)
    return [keyword[0] for keyword in keywords_freq[:n]]


def load_config(fname: str) -> dict:
    return toml.load(fname)


def set_environemnt(folder: str, template: str):
    env = Environment(loader=FileSystemLoader(folder))
    template = env.get_template(template)
    return template


# %% Load meta data and templates
config = load_config(fname='config/_readme.toml')

template_md = set_environemnt(folder='static/templates', template='README.md')
template_html = set_environemnt(folder=['static/templates', 'static'], template='index.html')

tutorial_repos, tutorial_repos_count = get_tutorial_repos(user='hsiangjenli')
tutorial_repos_keywords = get_repos_keywords(repos=tutorial_repos, n=3)

# Update config['Experience']['Sharing_Programming_Knowledge']
# Store the number of repos in which I've shared programming knowledge
config['Experience']['Sharing_Programming_Knowledge']['Description'] = \
config['Experience']['Sharing_Programming_Knowledge']['Description'].format(
    tutorial_repos_count=tutorial_repos_count,
    tutorial_repos_keywords=', '.join(tutorial_repos_keywords)
)

meta_data = {
    'static': r'C:\Users\ASUS\Documents\Github\hsiangjenli\static',
    # 'static': 'https://hsiangjenli.github.io/hsiangjenli/static',
    'author':config['Author'],
    'experiences':config['Experience'],
    'educations':config['Education'],
    'awards':config['Award'],
    'skills':config['Skills'],
    'projects':config['Personal_Project'],
    'social_links':config['Social_Media'],
    'tutorial_repos_keywords':tutorial_repos_keywords,
    'tutorial_repos_count':tutorial_repos_count,
    'attributes': config['Attributes']
}

# %% Output
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(
        template_md.render(
            **meta_data
        )
    )

with open('hsiangjenli.github.io/index.html', 'w', encoding='utf-8') as f:
    f.write(
        template_html.render(
            **meta_data
        )

    )