#!/usr/bin/env python
# find . -name "*.pyc" -exec rm -rf {} \;
# -*- coding: utf-8 -*-

from project import create_app
from project.config import DevelopmentConfig

application = create_app(DevelopmentConfig)

if __name__ == '__main__':
    application.run()