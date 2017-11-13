from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    #config.include('pyramid_jinja2')
    #config.add_static_view('static', 'static', cache_max_age=3600)
    #config.add_route('home', '/')

    config.add_route('get_policy', '/policy/{id}')
    config.add_route('post_policy', '/policy')
    config.add_route('get_policies_by_type', '/policies/{type}')
    config.add_route('get_policy_modules', '/policy/{id}/modules')
    config.add_route('post_module', '/module')
    config.add_route('get_module', '/module/{id}')
    config.scan()
    return config.make_wsgi_app()
