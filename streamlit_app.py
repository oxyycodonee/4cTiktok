import streamlit as st
 import requests
 import itertools
 import string
 import time
 
 st.title("Checker de usuarios de 4 letras en TikTok")
 
 # Iniciar checkeo
 if st.button("Buscar 1000 disponibles"):
     caracteres = string.ascii_lowercase + string.digits
     combinaciones = itertools.product(caracteres, repeat=4)
     resultados = []
     encontrados = 0
 
     with st.spinner("Buscando usuarios..."):
         for combo in combinaciones:
             if encontrados >= 1000:
                 break
             username = ''.join(combo)
             url = f"https://www.tiktok.com/@{username}"
             headers = {"User-Agent": "Mozilla/5.0"}
 
             try:
                 response = requests.get(url, headers=headers)
                 if response.status_code == 404:
                     resultados.append(username)
                     st.success(f"{username} está DISPONIBLE")
                 else:
                     st.warning(f"{username} no disponible")
                 encontrados += 1
                 time.sleep(0.3)
 
             except Exception as e:
                 st.error(f"Error al checar {username}: {e}")
                 time.sleep(2)
 
     st.subheader("Usuarios disponibles encontrados:")
     st.code("\n".join(resultados))
