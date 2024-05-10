---
date: "2024-05-08"
category: today-i-learned
tags: Github, Giscus, meta
author: Felix
---

# Enabling opt-out for Giscus comments

I'd like to restrict discussions to blog entries, and want to disable them in the index and other sites.

- we [previously added](https://github.com/csamaf/csamaf.github.io/pull/7) a custom
[templates/layout.html](https://github.com/csamaf/csamaf.github.io/blob/main/templates/layout.html) that is
unconditionally added to every page
- I want to be able to specify `comments: false` in the metadata section of a site to opt-out of discussions
- thus guard loading of the script with `{% if 'comments' in meta and meta.comments != 'False' %}`
- note that the check in Jinja is case-sensitive (I specify `false` in the metadata and need to check for `False`)
- add `comments: false` to all non-blog pages
