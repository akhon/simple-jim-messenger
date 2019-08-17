import pytest
from datetime import datetime


@pytest.fixture
def initial_port():
    return 7777

@pytest.fixture
def initial_host():
    return ''

@pytest.fixture
def initial_action():
    return 'presence'

@pytest.fixture
def initial_request(initial_action, initial_data):
    return {
        'action': initial_action,
        'time': datetime.now().timestamp(),
        'data': initial_data
    }


def test_action_make_response(initial_request, initial_code, initial_data, initial_action):
    actual_response = make_response(initial_request, initial_code, initial_data)
    assert actual_response.get('action') == initial_action

def test_code_make_response(initial_request, initial_code, initial_data):
    actual_response = make_response(initial_request, initial_code, initial_data)
    assert actual_response.get('code') == initial_code

def test_data_make_response(initial_request, initial_code, initial_data):
    actual_response = make_response(initial_request, initial_code, initial_data)
    assert actual_response.get('data') == initial_data

def test_client():
