import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from datetime import datetime

from style import load_style, metric_card

API_URL = "http://127.0.0.1:8000"

# carregando estilização da página
st.set_page_config(
    page_title="Civitas",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def categories():
    response = requests.get(f"{API_URL}/categories")
    return response.json()

def votes():
    response = requests.get(f"{API_URL}/result")
    return response.json()

def blockchain():
    response = requests.get(f"{API_URL}/chain")
    return response.json()

def last_update():
    chain = blockchain()
    if not chain:
        return "Sem atualizações"

    timestamp = chain[-1]["_Block__timestamp"]
    date = datetime.fromtimestamp(timestamp)

    return date.strftime("%d/%m/%Y %H:%M:%S")

def plot_results_chart(sorted_votes):
    df = pd.DataFrame(sorted_votes, columns=["Candidato", "Votos"])
    colors = ["#E04C4C", "#FA9D3A", "#ECE629", "#6AFF5C", "#48A440",
              "#4CC9E5", "#4881D7", "#AE76ED", "#F660DF", "#786D50"]

    # plot
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar( df["Candidato"], df["Votos"], color=colors[:len(df)])
    ax.set_ylabel("Votos")
    ax.yaxis.grid(True, linestyle="-", linewidth=0.6, alpha=0.5)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)


# implementação do front
def frontend():
    load_style()

    st.markdown('<div class="main-title">🗳️ Civitas </div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Sistema de votação baseado em Blockchain</div>', unsafe_allow_html=True)

    st.sidebar.image("assets/logo.png", width='stretch')
    st.sidebar.markdown('<div class="sidebar-title">NAVEGAÇÃO</div>', unsafe_allow_html=True)
    menu = st.sidebar.radio(
        ".",
        [
            "Adicionar candidato",
            "Votar",
            "Resultados",
            "Blockchain"
        ]
    )

    # MENU PARA ADICIONAR CANDIDATO
    if menu == "Adicionar candidato":
        st.subheader("Cadastrar candidato")

        category = st.text_input("Nome do candidato", placeholder="Digite o nome do candidato")

        if st.button("Adicionar candidato"):
            response = requests.post(f"{API_URL}/candidate", params={"new_category": category})

            if response.status_code == 200:
                result = response.json()

                if result[0]:
                    st.success(result[1])
                else:
                    st.warning(result[1])
            else:
                st.error("Erro ao cadastrar candidato.")
    

    # MENU PARA VOTAR
    elif menu == "Votar":
        current_categories = categories()
        if not current_categories:
            st.warning("Ainda não existem candidatos cadastrados.")

        else:
            st.subheader("Registrar voto")

            choice = st.selectbox("Escolha um candidato", current_categories)
            voter_cpf = st.text_input("CPF do eleitor", placeholder="Digite seu CPF")

            if st.button("Confirmar voto"):
                response = requests.post(
                    f"{API_URL}/vote",
                    json={
                        "choice": choice,
                        "voter_cpf": voter_cpf
                    }
                )

                result = response.json()

                if response.status_code == 200 and result["success"]:
                    st.success(result["message"])
                else:
                    st.warning(result["message"])


    # MENU PARA VISUALIZAR OS RESULTADOS
    elif menu == "Resultados":
        sorted_votes = votes()
        st.subheader("Resultados da eleição")
        st.caption(f"Última atualização: {last_update()}")

        if sorted_votes:
            total_votes = sum(count for _, count in sorted_votes)
            current_categories = categories()

            col1, col2, col3 = st.columns(3)
            with col1:
                metric_card(
                    "Candidatos",
                    len(current_categories)
                )

            with col2:
                metric_card(
                    "Votos registrados",
                    total_votes
                )

            with col3:
                metric_card(
                    "Blocos na Blockchain",
                    len(blockchain())
                )

            st.markdown("### Votos por candidato")
            for candidate, count in sorted_votes:
                st.write(
                    f"**{candidate}** — "
                    f"{count} voto"
                    + ("s" if count != 1 else "")
                )

            sorted_votes = votes()
            st.subheader("Gráfico da eleição")
            st.caption(f"Última atualização: {last_update()}")

            plot_results_chart(sorted_votes)

        else:
            st.info("Ainda não existem votos registrados.")


    # MENU PARA VISUALIZAR A BLOCKCHAIN
    elif menu == "Blockchain":
        st.subheader("Histórico da Blockchain")

        validation_response = requests.get(f"{API_URL}/chain/valid")
        blockchain_valid = validation_response.json()["valid"]
        if not blockchain_valid:
            st.error(
                "⚠️ Blockchain comprometida! "
                "Foram detectadas inconsistências na integridade da cadeia."
            )

        chain = blockchain()
        col1, col2 = st.columns(2)
        with col1:
            metric_card(
                "Blocos registrados",
                len(chain)
            )

        with col2:
            metric_card(
                "Votos registrados",
                max(len(chain) - 1, 0)
            )

        st.markdown("### Download")

        response = requests.get(f"{API_URL}/download")
        blockchain_json = response.json()

        st.download_button(
            label="Download Blockchain (.json)",
            data=blockchain_json,
            file_name="blockchain.json",
            mime="application/json"
        )
