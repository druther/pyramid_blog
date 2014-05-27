from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    User,
    Entry,
    )

@view_config(route_name='home', renderer='pyramid_blog:templates/index.mako')
def index_page(request):
    return {}

@view_config(route_name='blog', renderer='pyramid_blog:templates/view_blog.mako')
def blog_view(request):
    return {}


@view_config(route_name='blog_action', match_param='action=create',
             renderer='pyramid_blog:templates/edit_blog.mako')
def blog_create(request):
    return {}


@view_config(route_name='blog_action', match_param='action=edit',
             renderer='pyramid_blog:templates/edit_blog.mako')
def blog_update(request):
    return {}


@view_config(route_name='auth', match_param='action=in', renderer='string',
             request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string')
def sign_in_out(request):
    return {}

"""\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pyramid_blog_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

