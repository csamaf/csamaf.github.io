# -- Project information -----------------------------------------------------
import sys

sys.path.append("scripts")
sys.path.append(".")

project = "CONF_PY_PROJECT"
copyright = "CONF_PY_COPYRIGHT"
author = "CONF_PY_AUTHOR"

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_examples",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

templates_path = ["templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    "README.md",
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
            "url": "CONF_PY_GITHUB_URL",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Blog RSS feed",
            "url": "CONF_PY_SITE_URL/blog/atom.xml",
            "icon": "fa-solid fa-rss",
        },
    ],
}

html_favicon = "CONF_PY_HTML_FAVICON"
html_title = "CONF_PY_HTML_TITLE"
html_static_path = ["static"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "blog": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}

# OpenGraph config
ogp_site_url = "CONF_PY_OPENGRAPH_SITE_URL"
ogp_social_cards = {
    "line_color": "#4078c0",
    "image": "CONF_PY_OPENGRAPH_IMAGE",
}


rediraffe_redirects = {}
# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "blog",
}
from pathlib import Path

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

blog_baseurl = "CONF_PY_ABLOG_URL"
blog_title = "CONF_PY_ABLOG_TITLE"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = "CONF_PY_ABLOG_FEED_SUBTITLE"
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
# Don't execute anything by default because many old posts don't execute anymore
# and this slows down build times.
# Instead if I want something to execute, manually set it in the post's metadata.
nb_execution_mode = "off"


def setup(app):
    app.add_css_file("custom.css")
