policies = {}
modules = {}
policy_index = 0
module_index = 0


class Policy(object):
    """
    Policy
    """
    def __init__(self, name, type):
        global policy_index
        policy_index += 1
        self.id = policy_index
        self.name = name
        self.type = type
        self.modules = []

    def add_module(self, module_id):
        self.modules.append(module_id)

    def __dict__(self):
        """
        Return policy as a dict
        :return: policy dict
        """
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'modules': self.modules}


class Module(object):
    """
    Module
    """
    def __init__(self, name, type, description, policy_id):
        global module_index
        global policies

        module_index += 1
        self.id = module_index
        self.name = name
        self.type = type
        self.description = description
        self.policy_id = policy_id
        policies[policy_id].add_module(self.id)

    def __dict__(self):
        """
        Return module as a dict
        :return: module dict
        """
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'policy_id': self.policy_id}
