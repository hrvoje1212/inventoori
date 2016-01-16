WTF_CSRF_ENABLED = True
SECRET_KEY = 'N*X( 8g$E>zKx-+R}m*vAlDX0gD2c-37gb}:iT0p$9j!;tMG&}WF:--9-;l@KrTF'

# DB
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'inventoori.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WHOOSH_BASE = os.path.join(basedir, 'search.db')