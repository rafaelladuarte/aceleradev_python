
from main import get_temperature, RequestError
import requests
import pytest


# Classe customizada para realizar o mock
# Ela vai sobrescrever requests.Response
# retornado pelo requests.get
class MockResponse:
    def __init__(self, resposta):
        self.resposta = resposta

    # Substitui o método json() para retornar o que eu definir
    # como resposta na criação
    def json(self):
        return self.resposta


# As fixtures abaixo são funções executadas antes de cada teste
# em que são aplicadas. Normalmente fixtures são usadas
# para fornercer dados para os testes
@pytest.fixture
def latitude():
    return -14.235004


@pytest.fixture
def longitude():
    return -51.92528


@pytest.fixture
def key():
    return 'e1ee55658d4a2b28c4841e373c3b3d87'


def test_get_temperature_by_lat_lng(monkeypatch, latitude, longitude, key):

    reposta_mock = {"currently": {"temperature": 62}}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    # Retorna o valor convertido em celsius
    result = get_temperature(latitude, longitude, key)
    assert result == 16


def test_wrong_key(monkeypatch, latitude, longitude):
    key = 'e1ff55658d4a2b28c4841e373c3b3d87'

    reposta_mock = {"error": "permission denied"}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    with pytest.raises(RequestError):
        get_temperature(latitude, longitude, key)


def test_without_latitude(monkeypatch, longitude, key):
    # Como na função esse valor se torna string
    # Então atribui uma string vazia para testar a omissão.
    latitude = ''

    reposta_mock = {"error": "Poorly formatted request"}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    with pytest.raises(RequestError):
        get_temperature(latitude, longitude, key)
