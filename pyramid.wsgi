import site
site.addsitedir('/opt/tagdown/lib/python2.7/site-packages')
from pyramid.paster import get_app
application = get_app(
  '/opt/tagdown/development.ini', 'main')
