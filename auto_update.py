# %% Load necessary lib
import toml
from jinja2 import Environment, FileSystemLoader
import requests
from core import GitHubRepos, CrawlerMyBlogPosts, CalculateKeywords
from core.static_url import is_abs_url

def load_config(fname: str) -> dict:
    return toml.load(fname)

def set_environemnt(folder: str, template: str):
    env = Environment(loader=FileSystemLoader(folder))
    template = env.get_template(template)
    return template

def tutorial_info():
    # Crawl my blog posts
    crawler = CrawlerMyBlogPosts("https://github.com/hsiangjenli/blog/tree/main/source/_posts/tutorial")
    posts, count_blogs = crawler.get_blog_posts_name()
    
    # Crawl my github repos
    github = GitHubRepos("hsiangjenli")
    repos, count_repos = github.get_tutorial_repos()

    # Calculate keywords
    cal = CalculateKeywords(posts, repos)
    keywords = cal.get_keywords(n=4)

    count = count_repos + count_blogs

    return keywords, count

# %% Load meta data and templates
author = load_config(fname='config/_author.toml')
edcations = load_config(fname='config/_education.toml')
experiences = load_config(fname='config/_experience.toml')
competitions = load_config(fname='config/_award.toml')
skills = load_config(fname='config/_skill.toml')
projects = load_config(fname='config/_project.toml')

template_md = set_environemnt(folder='static/templates', template='README.md')
template_html = set_environemnt(folder=['static/templates', 'static'], template='index.html')

tutorial_keywords, tutorial_counts = tutorial_info()

# Update config['Experience']['Sharing_Programming_Knowledge']
# Store the number of repos in which I've shared programming knowledge
experiences['sharing_programming_knowledge']['english']['description'] = \
experiences['sharing_programming_knowledge']['english']['description'].format(
    tutorial_repos_count=tutorial_counts,
    tutorial_repos_keywords=', '.join(tutorial_keywords)
)

meta_data = {
    'static': r'C:\Users\ASUS\Documents\Github\hsiangjenli\static',
    # 'static': 'https://hsiangjenli.github.io/hsiangjenli/static',
    'language': 'english',
    'author':author,
    "social_links": author['social_media'],
    'educations': edcations,
    'experiences': experiences,
    'awards': competitions,
    'skills': skills,
    'projects': projects,
}

# %% Output
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(
        template_md.render(
            is_abs_url=is_abs_url,
            **meta_data
        )
    )

if meta_data['static'].startswith("https://"):
    output_path = 'hsiangjenli.github.io/index.html'
else:
    output_path = 'test.html'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(
        template_html.render(
            is_abs_url=is_abs_url,
            **meta_data
        )

    )