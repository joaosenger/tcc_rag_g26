"""Frontend Streamlit: chat RAG sobre materiais do curso.

O corpus é ingerido automaticamente na inicialização da API — o aluno só
precisa fazer perguntas.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests
import streamlit as st

from frontend.auth import check_credentials
from frontend.utils import (
    build_pdf_url,
    format_sources_display,
    is_insufficient_evidence,
    list_corpus_pdfs,
)

API_URL = os.getenv("API_URL", "http://localhost:8000")

APP_TITLE = "TCC G26 - Pós em Processamento de Linguagem Natural UFG"
PLAYLIST_URL = (
    "https://www.youtube.com/watch?v=ImhYlISeWPQ&list=PLOQgLBuj2-3KT9ZWvPmaGFQ0KjIez0403"
)
COURSE_DOC_URL = "https://fastapidozero.dunossauro.com/estavel/"


def render_header() -> None:
    st.markdown(
        f"<h3 style='text-align:center; margin-bottom:0.2rem;'>{APP_TITLE}</h3>"
        "<hr style='margin-top:0.2rem; margin-bottom:1.5rem;'>",
        unsafe_allow_html=True,
    )


def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False


def render_login() -> None:
    st.markdown(
        "<p style='text-align:center; margin-top:2rem;'>"
        "<strong>Acesso restrito</strong></p>",
        unsafe_allow_html=True,
    )
    _, center, _ = st.columns([1, 2, 1])
    with center:
        with st.form("login_form"):
            username = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            submitted = st.form_submit_button("Entrar", use_container_width=True)

    if submitted:
        expected_username = st.secrets.get("login", "")
        expected_password = st.secrets.get("password", "")
        if check_credentials(username, password, expected_username, expected_password):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")


def render_logout() -> None:
    with st.sidebar:
        st.markdown("**Conteúdo do curso**")
        st.markdown(
            f'<a href="{PLAYLIST_URL}" target="_blank">▶ Playlist das aulas</a>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<a href="{COURSE_DOC_URL}" target="_blank">📖 Documentação do curso</a>',
            unsafe_allow_html=True,
        )

        pdfs = list_corpus_pdfs(Path(__file__).resolve().parent.parent / "content" / "documents")
        if pdfs:
            st.markdown("**Documentos PDF**")
            for pdf in pdfs:
                st.markdown(
                    f'<a href="{build_pdf_url(API_URL, pdf)}" target="_blank">📄 {pdf}</a>',
                    unsafe_allow_html=True,
                )

        st.markdown("---")
        if st.button("Sair"):
            st.session_state.authenticated = False
            st.session_state.messages = []
            st.rerun()


def check_api() -> bool:
    """Verifica se a API está online."""
    try:
        resp = requests.get(f"{API_URL}/health", timeout=5)
        return resp.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def render_chat() -> None:
    st.subheader("Pergunte sobre o material do curso")
    init_session_state()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources_display"):
                with st.expander("Fontes"):
                    st.markdown(msg["sources_display"])

    if question := st.chat_input("Digite sua pergunta..."):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Consultando o material..."):
                try:
                    resp = requests.post(
                        f"{API_URL}/api/chat",
                        json={"question": question},
                        timeout=60,
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        answer = data["answer"]
                        sources = data.get("sources", [])
                    else:
                        answer = f"Erro {resp.status_code}: {resp.json().get('detail', resp.text)}"
                        sources = []
                except requests.exceptions.ConnectionError:
                    answer = f"Não foi possível conectar à API em {API_URL}."
                    sources = []
                except Exception as exc:
                    answer = f"Falha na consulta: {exc}"
                    sources = []

            st.markdown(answer)

            sources_display = format_sources_display(sources)
            if sources_display:
                with st.expander("Fontes"):
                    st.markdown(sources_display)

            if is_insufficient_evidence(answer):
                st.warning(
                    "⚠️ Evidência insuficiente: a resposta não está "
                    "totalmente sustentada pelo material."
                )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources,
                "sources_display": sources_display,
            }
        )


def main() -> None:
    st.set_page_config(page_title="TCC G26 - RAG", page_icon="📚", layout="centered")
    init_session_state()
    render_header()

    if not st.session_state.authenticated:
        render_login()
        return

    render_logout()

    if not check_api():
        st.error(f"Não foi possível conectar à API em {API_URL}. Verifique se ela está rodando.")
        st.info("Inicie a API com:\n\n```\nuvicorn app.main:app --reload\n```")
        return

    render_chat()


if __name__ == "__main__":
    main()
