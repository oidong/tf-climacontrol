# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Paths for Datafiles
datadir = os.path.join(basedir, "daten")
database = os.path.join(datadir, "clima.db")

# Additional stylesheets and scripts
stylesheets = [] 
scripts = []

# Datenbank
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + database
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Pagination
POSTS_PER_PAGE = 10
