from unittest.mock import Mock

import pytest
from SingleSignOn.my_service import MyService, Request
from SingleSignOn.single_sign_on import SSOToken, SingleSignOnRegistry


def test_hello_name():
    service = MyService(Mock(SingleSignOnRegistry))
    response = service.handle(Request("Alice"), SSOToken())
    assert response.text == "Hello Alice!"

def test_single_sign_on():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(spy_sso_registry)
    token = SSOToken
    service.handle(Request("Alice"), token)
    spy_sso_registry.is_valid.assert_called_with(token)

def confirm_token(token):
    def is_valid(actual_token):
        if actual_token != token:
            raise ValueError("wrong token received")
    
    return is_valid

def test_single_sign_on_receives_correct_token():
    mock_sso_resgistry = Mock(SingleSignOnRegistry)
    correct_token = SSOToken
    mock_sso_resgistry.is_valid = Mock(side_effect=confirm_token(correct_token))
    service = MyService(mock_sso_resgistry)
    wrong_token = SSOToken
    service.handle(Request("Alice"), wrong_token) # this will still pass because, all its checking is if the object has been passed. its not checking the value of the object
    mock_sso_resgistry.is_valid.assert_called_with(correct_token)