---
date: "2024-06-05"
category: today-i-learned
tags: JetBrains, PyCharm, Python
author: René
---

# Pycharm won't start the debugger with a clean interpreter

You get something like

```bash
Traceback (most recent call last):
  File "$HOME/.local/share/JetBrains/Toolbox/apps/pycharm-professional/plugins/python/helpers/pydev/_pydevd_bundle/pydevd_cython_wrapper.py", line 8, in <module>
    from _pydevd_bundle_ext import pydevd_cython as mod
ModuleNotFoundError: No module named '_pydevd_bundle_ext'
```

which means the debugger can't find the Cython extension.
Normally you get asked for that, but apparently sometimes you don't.
In that case, you can manually install it with

```bash
pip install setuptools cython # just in case your env doesn't have  them
python ~/.local/share/JetBrains/Toolbox/apps/pycharm-professional/plugins/python/helpers/pydev/setup_cython.py build_ext -i
```
