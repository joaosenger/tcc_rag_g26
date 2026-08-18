"""Testes unitários da autenticação do frontend (login)."""

from __future__ import annotations

from frontend.auth import check_credentials, extract_credentials

LOGIN = "G26"
PASSWORD = "G26Tcc2026@UFG"


class FakeAttrDict(dict):
    """Simula o AttrDict retornado pelo st.secrets do Streamlit."""

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError(key) from exc


def test_extract_credentials_secao_login():
    section = FakeAttrDict({"login": LOGIN, "password": PASSWORD})
    assert extract_credentials(section) == (LOGIN, PASSWORD)


def test_extract_credentials_none():
    assert extract_credentials(None) == ("", "")


def test_extract_credentials_string_simples():
    assert extract_credentials(LOGIN) == (LOGIN, "")


def test_extract_credentials_secao_sem_chaves():
    assert extract_credentials({}) == ("", "")


def test_credentials_corretas():
    assert check_credentials(LOGIN, PASSWORD, LOGIN, PASSWORD) is True


def test_senha_errada():
    assert check_credentials(LOGIN, "senha-errada", LOGIN, PASSWORD) is False


def test_usuario_errado():
    assert check_credentials("outro", PASSWORD, LOGIN, PASSWORD) is False


def test_campos_vazios():
    assert check_credentials("", "", LOGIN, PASSWORD) is False


def test_case_sensitive():
    assert check_credentials("g26", PASSWORD, LOGIN, PASSWORD) is False
    assert check_credentials(LOGIN, "g26tcc2026@ufg", LOGIN, PASSWORD) is False


def test_usuario_correto_senha_errada_nao_autentica():
    assert check_credentials(LOGIN, "x", LOGIN, PASSWORD) is False