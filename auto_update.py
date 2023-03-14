# %% Load necessary lib
import toml
from jinja2 import Environment, FileSystemLoader


# %% 
def LoadConfig(fname: str) -> dict:
    return toml.load(fname)

def SetEnvironemnt(folder: str, template: str):
    env = Environment(loader=FileSystemLoader(folder))
    template = env.get_template(template)
    return template


# %% Load meta data and templates
config = LoadConfig(fname='config/_readme.toml')

template_md = SetEnvironemnt(folder='static/templates', template='README.md')
template_html = SetEnvironemnt(folder=['static/templates', 'static'], template='index.html')

meta_data = {
    'static': 'https://hsiangjenli.github.io/hsiangjenli/static',
    'author':config['Author'],
    'experiences':config['Experience'],
    'educations':config['Education'],
    'awards':config['Award'],
    'skills':config['Skills'],
    'projects':config['Personal_Project'],
    'social_links':config['Social_Media']    
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