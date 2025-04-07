import streamlit as st
import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor

def check_username(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        return username if response.status_code == 404 else None
    except:
        return None

def generar_usernames(cantidad):
    caracteres = string.ascii_letters + string.digits
    return list({''.join(random.choices(caracteres, k=4)) for _ in range(cantidad * 2)})[:cantidad]

st.title("Checker de 4c.")
st.caption("By @oxyycodonee.")
if st.button("Buscar"):
    st.write("Buscando, espera un momento...")
    usernames = generar_usernames(100000)
    disponibles = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        resultados = executor.map(check_username, usernames)

    for resultado in resultados:
        if resultado:
            disponibles.append(resultado)

    st.success(f"Disponibles: {len(disponibles)}")
    st.write(disponibles[:50])
    st.warning(f"No disponibles: {5000 - len(disponibles)}")
