from unittest.mock import Mock
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