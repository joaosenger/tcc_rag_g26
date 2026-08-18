"""Autenticação do frontend Streamlit (login com usuário e senha).

Funções puras e testáveis, sem dependência do Streamlit.
"""

from __future__ import annotations

import hmac


def check_credentials(
    username: str,
    password: str,
    expected_username: str,
    expected_password: str,
) -> bool:
    """Valida usuário e senha contra os valores esperados.

    Usa comparação em tempo constante (hmac.compare_digest) para evitar
    ataques de timing.

    Args:
        username: usuário informado.
        password: senha informada.
        expected_username: usuário válido.
        expected_password: senha válida.

    Returns:
        True se as credenciais conferem.
    """
    username_ok = hmac.compare_digest(username, expected_username)
    password_ok = hmac.compare_digest(password, expected_password)
    return username_ok and password_ok