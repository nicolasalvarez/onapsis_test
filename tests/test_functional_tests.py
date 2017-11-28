import pytest
import requests

@pytest.mark.parametrize("policy_name, policy_type, policy_status",
                         [
                             ("SAP1", "SAP", 200),
                             ("EBS1", "EBS", 200),
                             ("SAP2", "ZAP", 400),  # should return 400, instead is returning 200
                             (" ", "SAP", 400),  # should return 400, instead is returning 200,
                             # considering that policy with empty name is not allowed.
                             (" ", "EBS", 400),  # should return 400, instead is returning 200,
                             # considering that policy with empty name is not allowed.
                             (" ", " ", 400)  # should return 400, instead is returning 200,
                             # considering that policy with empty name is not allowed.
                         ])
def test_post_policy(policy_name, policy_type, policy_status):
    """
    :tests the creation of a policy with different values.
    """
    payload = {"name": policy_name, "type": policy_type}
    r = requests.post('http://localhost:6543/policy', json=payload)
    assert r.status_code == policy_status, "The response code was not the expected"


@pytest.mark.parametrize("module_name, module_type, policy_id, module_description, module_status",
                         [
                             ("mod1_SAP1", "SAP", 1, "mod1_SAP1 Desc", 200),
                             ("mod2_EBS1", "EBS", 2, "mod2_EBS1 Desc", 200),
                             ("mod2_EBS1", "EBS", 100000, "mod2_EBS1 Desc", 400),
                             # Duplicated module association,
                             ("mod1_SAP1", "SAP", 1, "mod1_SAP1 Desc", 400),
                             # should return 400 instead is returning a 200
                         ])
def test_post_module(module_name, module_type, policy_id, module_description, module_status):
    """
    :tests the creation of a module with different values.
    """
    payload = {"name": module_name, "type": module_type,
               "policy_id": policy_id, "description": module_description}

    # Creating the module
    r = requests.post('http://localhost:6543/module', json=payload)
    assert r.status_code == module_status

    # Fetching the created module.
    r = requests.get('http://localhost:6543/module/1')

    # verify that content of the GET response matches the expected.
    assert r.status_code == 200, "The response code was not the expected, the expected code was" + module_status
    assert r.text.find(module_name), "The module name was not found on the created module"
    assert r.text.find(module_type), "The module type was not found on the created module"
    assert r.text.find(str(policy_id)), "The policy id was not found on the created module"
    assert r.text.find(
        module_description), "The module description was not found on the created module"



def test_return_policy_sap():
    test_post_policy("SAP1","SAP",200)
    r = requests.get('http://localhost:6543/policy/1')
    assert r.status_code == 200, "The response code was not the expected"
    assert r.text.find("SAP1"), "The policy name was not found on the response"
    assert r.text.find("SAP"), "The policy type was not found on the response"
    assert r.text.find("1"), "The policy id was not found on the response"

def test_return_policy_ebs():
    test_post_policy("EBS1","EBS",200)
    r = requests.get('http://localhost:6543/policy/2')
    assert r.status_code == 200, "The response code was not the expected"
    assert r.text.find("EBS1"), "The policy name was not found on the response"
    assert r.text.find("EBS"), "The policy type was not found on the response"
    assert r.text.find("EBS"), "The policy id was not found on the response"


def test_return_module_sap():
    test_post_policy("SAP1","SAP",200)
    test_post_module("mod_SAP","SAP",1,"Desc 1",200)
    r = requests.get('http://localhost:6543/module/1')
    assert r.status_code == 200, "The response code was not the expected"
    assert r.text.find("mod_SAP"), "The module description was not found on the created module"
    assert r.text.find("1"), "The associated policy id name was not found on the created module"
    assert r.text.find("SAP"), "The module name was not found on the created module"

def test_return_module_ebs():
    test_post_policy("EBS1","EBS",200)
    test_post_module("mod_EBS","EBS",2,"Desc 2",200)
    r = requests.get('http://localhost:6543/module/2')
    assert r.status_code == 200, "The response code was not the expected"
    assert r.text.find("mod_EBS"), "The module description was not found on the created module"
    assert r.text.find("EBS"), "The module type was not found on the created module"
    assert r.text.find("2"), "The associated policy id name was not found on the created module"