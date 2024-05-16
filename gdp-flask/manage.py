#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   manage.py
# Time    :   2024/05/16 16:07:52
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from application import app


app.run("0.0.0.0", port=5000, debug=True)
