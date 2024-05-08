import sys
from pathlib import Path

# -- Project information -----------------------------------------------------

sys.path.append("scripts")
sys.path.append(".")

# BASE_URL = "https://csamaf.github.io"
BASE_URL = "http://127.0.0.1:8000"
PROJECT = "CS-AM-AF"
PROJECT_LONG = "Computational Scientists, Applied Mathematicians, and Friends"

project = f"{PROJECT}"
copyright = f"{PROJECT} Authors"
author = f"{PROJECT}"

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_examples",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    ".venv",
    "venv",
    "README.md",
    "LICENSE.md",
    "**/.ipynb_checkpoints/*",
]

# -- HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "search_bar_text": "Search this site ...",
    "analytics": {"google_analytics_id": "CONF_PY_GOOGLE_ANALYTICS_ID"},
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/csamaf/csamaf.github.io",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Blog RSS feed",
            "url": f"{BASE_URL}/blog/atom.xml",
            "icon": "fa-solid fa-rss",
        },
    ],
}

html_favicon = "static/favicon-32x32.png"
html_title = f"{PROJECT}"
html_static_path = ["static"]
html_sidebars = {
    "**": [
        "ablog/authors.html",
        "ablog/languages.html",
        "ablog/locations.html",
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
    ]
}

rediraffe_redirects = {}
# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "blog",
}

for old, new in redirect_folders.items():
    for newpath in Path(new).rglob("**/*"):
        if newpath.suffix in [".ipynb", ".md"] and "ipynb_checkpoints" not in str(
            newpath
        ):
            oldpath = str(newpath).replace("blog/", "posts/", 1)
            # Skip pandoc because for some reason it's broken
            if "pandoc" not in str(newpath):
                rediraffe_redirects[oldpath] = str(newpath)

# -- ABlog ---------------------------------------------------

blog_baseurl = f"{BASE_URL}"
blog_title = f"{PROJECT} Blog"
blog_authors = {
    "Felix": ("Felix Schindler", f"{blog_baseurl}/about/felix/"),
}
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = f"{PROJECT_LONG}"
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# -- MyST and MyST-NB ---------------------------------------------------

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# MyST-NB
# Don't execute anything by default as this slows down build times.
# Instead if I want something to execute, manually set it in the post's metadata.
nb_execution_mode = "off"


def setup(app):
    app.add_css_file("custom.css")
