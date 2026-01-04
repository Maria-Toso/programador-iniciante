import streamlit as st

# --- CONFIGURAÇÃO E ESTILO ---
st.set_page_config(page_title="Jogo da Velha", page_icon="🎮")
st.title("🎮 Jogo da Velha")

# Estética dos botões para parecerem quadrados e grandes
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 100px;
        font-size: 40px !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAÇÃO DO ESTADO ---
if 'tabuleiro' not in st.session_state:
    st.session_state.tabuleiro = [""] * 9
    st.session_state.jogador_atual = "X"
    st.session_state.vencedor = None

def reset_jogo():
    st.session_state.tabuleiro = [""] * 9
    st.session_state.jogador_atual = "X"
    st.session_state.vencedor = None

def verificar_vitoria():
    vitorias = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colunas
        (0, 4, 8), (2, 4, 6)             # Diagonais
    ]
    for a, b, c in vitorias:
        if (st.session_state.tabuleiro[a] == st.session_state.tabuleiro[b] == 
            st.session_state.tabuleiro[c] != ""):
            return st.session_state.tabuleiro[a]
    if "" not in st.session_state.tabuleiro:
        return "Empate"
    return None

def clique_botao(indice):
    # Só age se a casa estiver vazia e não houver vencedor
    if st.session_state.tabuleiro[indice] == "" and st.session_state.vencedor is None:
        st.session_state.tabuleiro[indice] = st.session_state.jogador_atual
        
        resultado = verificar_vitoria()
        if resultado:
            st.session_state.vencedor = resultado
        else:
            # Alterna jogador
            st.session_state.jogador_atual = "O" if st.session_state.jogador_atual == "X" else "X"

# --- INTERFACE DO UTILIZADOR ---

# Criar a grelha 3x3 usando colunas do Streamlit
cols = st.columns(3)
for i in range(9):
    conteudo = st.session_state.tabuleiro[i]
    label = conteudo if conteudo != "" else " "
    
    with cols[i % 3]:
        # Cada botão tem uma chave (key) única
        st.button(label, key=f"btn_{i}", on_click=clique_botao, args=(i,))

st.divider()

# Mensagens de Status
if st.session_state.vencedor:
    if st.session_state.vencedor == "Empate":
        st.warning("🤝 Empate! Deu velha.")
    else:
        st.success(f"🏆 Vitória! O jogador **{st.session_state.vencedor}** venceu!")
else:
    st.info(f"Vez do jogador: **{st.session_state.jogador_atual}**")

# Botão de Reiniciar
st.button("Reiniciar Partida", on_click=reset_jogo)
