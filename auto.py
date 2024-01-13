import os
import datetime
from core import tutils

# == personal information ============================================================================================
Q = "The way lead to success is your own resolution."

NAME = "Hsiang-Jen Li"
NICKNAME = "RN"
GITHUB = "https://github.com/hsiangjenli"
MAIL = "hsiangjenli@gmail.com"

EDU = tutils.load_toml("config/_education.toml")
SKILL = tutils.load_toml("config/_skill.toml")
RI = tutils.load_toml("config/_research.toml")
SIDE_PROJECT = tutils.load_toml("config/_project.toml")

# == webpage ==========================================================================================================
WEBPAGE = "hsiangjenli.github.io"
WEBPAGE_TEMPLATE = tutils.set_environemnt(folder='static/template/html/read_only', template='index.html')

os.makedirs(f"{WEBPAGE}/static", exist_ok=True)
os.system(f"cp -r static/* {WEBPAGE}/static/")

# == main ============================================================================================================
if __name__ == "__main__":

    LAST_UPDATE = datetime.datetime.now().strftime("%Y-%m-%d")
    YEAR = f"2024 ~ {datetime.datetime.now().year}" if datetime.datetime.now().year > 2024 else 2024
    COPYRIGHT = f"© {YEAR} Hsiang-Jen Li. All rights reserved."

    PERSONAL_INFO = {
        "Q": Q,
        "NAME": NAME,
        "NICKNAME": NICKNAME,
        "GITHUB": GITHUB,
        "MAIL": MAIL,
    }

    O_WEBPAGE = WEBPAGE_TEMPLATE.render(**PERSONAL_INFO, EDU=EDU, SKILL=SKILL, RI=RI, SIDE_PROJECT=SIDE_PROJECT, COPYRIGHT=COPYRIGHT, LAST_UPDATE=LAST_UPDATE)

    tutils.write(O_WEBPAGE, f"{WEBPAGE}/index.html")