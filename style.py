import streamlit as st


BLUE = "#269196"
WHITE = "#ffffff"


def load_style():
    st.markdown(
        f"""
        <style>

        /* FUNDO PRINCIPAL */

        .stApp {{
            background-color: {WHITE};
        }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }}


        /* TÍTULOS E TEXTOS */

        .main-title {{
            font-size: 2.5rem;
            font-weight: 800;
            color: {BLUE};
            margin-bottom: 0.2rem;
        }}

        .subtitle {{
            font-size: 1.05rem;
            color: {BLUE};
            margin-bottom: 2rem;
        }}

        h1, h2, h3 {{
            color: {BLUE} !important;
        }}

        p, label {{
            color: {BLUE};
        }}


        /* CARDS */

        .card {{
            background-color: {WHITE};
            padding: 1.5rem;
            border-radius: 16px;
            border: 1px solid {BLUE};
            box-shadow: 0 2px 8px rgba(38, 150, 92, 0.08);
            margin-bottom: 1rem;
        }}

        .metric-card {{
            background-color: {WHITE};
            padding: 1.3rem;
            border-radius: 14px;
            border: 2px solid {BLUE};
            text-align: center;
            box-shadow: 0 2px 8px rgba(38, 150, 92, 0.08);
        }}

        .metric-title {{
            font-size: 0.9rem;
            color: {BLUE};
            margin-bottom: 0.4rem;
        }}

        .metric-value {{
            font-size: 1.8rem;
            font-weight: 700;
            color: {BLUE};
        }}


        /* SIDEBAR */

        .sidebar-title {{
            color: #ffffff;
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            margin-bottom: 0.8rem;
        }}

        section[data-testid="stSidebar"] {{
            background-color: {BLUE};
        }}

        section[data-testid="stSidebar"] * {{
            color: {WHITE} !important;
        }}


        /* BOTÕES */

        .stButton > button {{
            background-color: {BLUE} !important;
            border: 1px solid {BLUE} !important;
            border-radius: 10px;
            font-weight: 600;
            padding: 0.55rem 1rem;
        }}

        .stButton > button p {{
            color: #ffffff !important;
        }}

        .stButton > button span {{
            color: #ffffff !important;
        }}

        .stButton > button:hover {{
            background-color: {BLUE} !important;
            border: 1px solid {BLUE} !important;
        }}

        .stButton > button:hover p {{
            color: #ffffff !important;
        }}

        .stButton > button:hover span {{
            color: #ffffff !important;
        }}


        /* CAMPOS DE TEXTO */

        .stTextInput input {{
            background-color: {WHITE};
            color: {BLUE};
            border: 1px solid {BLUE};
            border-radius: 10px;
        }}

        .stTextInput input:focus {{
            border: 2px solid {BLUE};
            box-shadow: 0 0 0 1px {BLUE};
        }}


        /* SELECTBOX */

        .stSelectbox div[data-baseweb="select"] {{
            border-radius: 10px;
        }}

        .stSelectbox div[data-baseweb="select"] > div {{
            background-color: {WHITE};
            color: {BLUE};
            border-color: {BLUE};
        }}


        /* DOWNLOAD BUTTON */

        .stDownloadButton > button {{
            background-color: {BLUE} !important;
            border: 1px solid {BLUE} !important;
            border-radius: 10px;
            font-weight: 600;
        }}

        .stDownloadButton > button p {{
            color: #ffffff !important;
        }}

        .stDownloadButton > button span {{
            color: #ffffff !important;
        }}

        .stDownloadButton > button:hover {{
            background-color: {BLUE} !important;
            border: 1px solid {BLUE} !important;
        }}

        .stDownloadButton > button:hover p {{
            color: #ffffff !important;
        }}

        .stDownloadButton > button:hover span {{
            color: #ffffff !important;
        }}


        /* EXPANDERS */

        div[data-testid="stExpander"] {{
            border: 1px solid {BLUE};
            border-radius: 10px;
            background-color: {WHITE};
        }}

        div[data-testid="stExpander"] summary {{
            color: {BLUE};
        }}


        </style>
        """,
        unsafe_allow_html=True
    )


def metric_card(title, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )