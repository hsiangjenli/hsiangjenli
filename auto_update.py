# %% Load necessary lib
import toml
from jinja2 import Environment, FileSystemLoader
import requests
from core import GitHubRepos, CrawlerMyBlogPosts, CalculateKeywords

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
config = load_config(fname='config/_readme.toml')

template_md = set_environemnt(folder='static/templates', template='README.md')
template_html = set_environemnt(folder=['static/templates', 'static'], template='index.html')

tutorial_keywords, tutorial_counts = tutorial_info()

# Update config['Experience']['Sharing_Programming_Knowledge']
# Store the number of repos in which I've shared programming knowledge
config['Experience']['Sharing_Programming_Knowledge']['Description'] = \
config['Experience']['Sharing_Programming_Knowledge']['Description'].format(
    tutorial_repos_count=tutorial_counts,
    tutorial_repos_keywords=', '.join(tutorial_keywords)
)

meta_data = {
    # 'static': r'C:\Users\ASUS\Documents\Github\hsiangjenli\static',
    'static': 'https://hsiangjenli.github.io/hsiangjenli/static',
    'author':config['Author'],
    'experiences':config['Experience'],
    'educations':config['Education'],
    'awards':config['Award'],
    'skills':config['Skills'],
    'projects':config['Personal_Project'],
    'social_links':config['Social_Media'],
    'tutorial_repos_keywords':tutorial_keywords,
    'tutorial_repos_count':tutorial_counts,
    'attributes': config['Attributes']
}

# %% Output
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(
        template_md.render(
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
            **meta_data
        )

    )