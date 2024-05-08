---
date: "2024-05-08"
category: TodayILearned
tags: Github, Giscus
author: Felix
---

# Enabling discussions for this blog via Giscus

Basically, follow the instructions on [giscus.app](https://giscus.app/):

- enable [github.com/apps/giscus](https://github.com/apps/giscus) for the repo hosting our site
- enable discussions for the repo hosting our site
- create a new discussion category
  - `Category name`: `Blog comments`
  - `Discussion Format`: `Open-ended discussion`
- select newly created category on https://giscus.app/
- create `templates/layout.html` with the following data (adapt to your needs)
  ```
  {%- extends "pydata_sphinx_theme/layout.html" %}

  {% block docs_body %}
  {{ super() }}
  <!-- Add a comment box underneath the page's content -->
  <script src="https://giscus.app/client.js"
          data-repo="csamaf/csamaf.github.io"
          data-repo-id="R_kgDOLvzyjQ"
          data-category="Blog comments"
          data-category-id="DIC_kwDOLvzyjc4CfN7O"
          data-mapping="pathname"
          data-reactions-enabled="1"
          data-emit-metadata="0"
          data-theme="light"
          data-lang="en"
          crossorigin="anonymous"
          async>
  </script>
  {% endblock %}
  ```
- ensure to have `templates_path = ["templates"]` in your `conf.py`
