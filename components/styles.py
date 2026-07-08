import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#F5F7FB;
    }

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        max-width:1300px;
    }

    h1,h2,h3{
        color:#1E3A8A;
        font-weight:700;
    }

    div[data-testid="metric-container"]{
        background:white;
        border-radius:18px;
        padding:18px;
        box-shadow:0px 8px 20px rgba(0,0,0,.08);
        transition:0.25s;
        border:1px solid #EEF2FF;
    }

    div[data-testid="metric-container"]:hover{
        transform:translateY(-5px);
        box-shadow:0px 15px 30px rgba(0,0,0,.12);
    }

    .card{

        background:white;

        padding:20px;

        border-radius:20px;

        box-shadow:0px 10px 25px rgba(0,0,0,.08);

        margin-bottom:20px;

    }

    .header{

        background:linear-gradient(90deg,#2563EB,#60A5FA);

        padding:30px;

        border-radius:25px;

        color:white;

        margin-bottom:25px;

    }

    .header h1{

        color:white;

        margin-bottom:5px;

    }

    .header p{

        color:white;

        font-size:18px;

    }

    .ai-box{

        background:#EEF6FF;

        border-left:8px solid #2563EB;

        padding:20px;

        border-radius:18px;

        margin-top:15px;

    }

    </style>
    """, unsafe_allow_html=True)