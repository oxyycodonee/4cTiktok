import streamlit as st
import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_username(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        return username, (response.status_code == 404)
    except:
        return username, False

def generar_usernames(cantidad):
    caracteres = string.ascii_letters + string.digits
    return list({''.join(random.choices(caracteres, k=4)) for _ in range(cantidad * 2)})[:cantidad]

st.title("Checker de 4c")
st.caption("By @oxyycodonee")

if st.button("Buscar"):
    st.write("Buscando, espera un momento...")
    usernames = generar_usernames(10000)
    disponibles = []
    no_disponibles = []
    tabla = st.empty()
    resultados_mostrados = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(check_username, user) for user in usernames]
        for future in as_completed(futures):
            user, disponible = future.result()
            resultados_mostrados.append({"Usuario": user, "Estado": "Disponible" if disponible else "No disponible"})
            tabla.dataframe(resultados_mostrados)

            if disponible:
                disponibles.append(user)
            else:
                no_disponibles.append(user)

    st.success(f"Disponibles: {len(disponibles)}")
    st.warning(f"No disponibles: {len(no_disponibles)}")
    st.write("Primeros 50 disponibles:")
    st.write(disponibles[:50])
