from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest
from onapsis_test.models import policies, Policy, modules, Module


@view_config(route_name='home', renderer='json')
def my_view(request):
    return {'project': 'onapsis_test'}


@view_config(route_name='post_policy', request_method="POST", renderer='json')
def post_policy(request):
    json_policy = request.json_body
    policy = Policy(json_policy['name'], json_policy['type'])
    policies[policy.id] = policy
    return policy.__dict__()


@view_config(route_name='get_policy', request_method="GET", renderer='json')
def get_policy(request):
    policy_id = request.matchdict['id']
    return policies[int(policy_id)].__dict__()


@view_config(route_name='post_module', request_method="POST", renderer='json')
def post_module(request):
    json_mod = request.json_body

    if not policies.get(json_mod['policy_id']):
        raise HTTPBadRequest("Policy not found")

    module = Module(json_mod['name'], json_mod['type'], json_mod.get('description', ""), json_mod['policy_id'])
    modules[module.id] = module
    return module.__dict__()


@view_config(route_name='get_module', request_method="GET", renderer='json')
def get_module(request):
    module_id = request.matchdict['id']
    return modules[int(module_id)].__dict__()


@view_config(route_name='get_policies_by_type', request_method="GET", renderer='json')
def get_policies_by_type(request):
    type = request.matchdict['type']
    return [policy.__dict__() for policy in policies.values() if policy.type == type]


@view_config(route_name='get_policy_modules', request_method="GET", renderer='json')
def get_policy_modules(request):
    policy_id = request.matchdict['id']
    return [modules[mod_id].__dict__() for mod_id in policies[int(policy_id)].modules]
