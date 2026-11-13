import streamlit as st
from google import genai

# Configuração da API e da Interface
st.set_page_config(page_title="CitizenTech", page_icon="🚍")
st.title("🤖 Assistente CitizenTech")
st.caption("Sistema Integrado de Mobilidade Urbana")

# Inicializa o cliente do Gemini (Substitua pela sua chave válida)
CHAVE_API = st.secrets["GEMINI_API_KEY"]
cliente = genai.Client(api_key=CHAVE_API)

#Estruturas de Dados (Banco Local e Memória do Chat)
status_transporte = {
    "L3": {"nome": "Linha 3 - Vermelha", "status": "Velocidade Reduzida"},
    "L9": {"nome": "Linha 9 - Esmeralda", "status": "Operação Normal"},
    "801": {"nome": "Ônibus 801", "status": "Atraso de 15 minutos"}
}

# Inicializa a memória da conversa no frontend (Variáveis de Sessão)
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [{"role": "assistant", "content": "Olá! Sou o Assistente CitizenTech. Como posso ajudar seu trajeto hoje?"}]

# Funções de Lógica e Automação (Mantendo as exigências do professor)
def verificar_status_local(mensagem):
    """Usa laço de repetição (for) e condicional (if) para busca local"""
    for chave, dados in status_transporte.items():
        if chave.lower() in mensagem.lower():
            return f"🚨 **[Sistema Local]** {dados['nome']}: {dados['status']}"
    return None

def interpretar_e_responder(texto_usuario):
    """Cérebro do bot: Roteamento usando condicionais"""
    texto_limpo = texto_usuario.strip().lower()
    
    # 1º Filtro: Busca local
    resposta_local = verificar_status_local(texto_usuario)
    if resposta_local:
        return resposta_local
        
    # 2º Filtro: Conecta com a IA
    try:
        chat = cliente.chats.create(model='gemini-3.5-flash')
        prompt = f"Você é o Assistente CitizenTech de mobilidade. Seja claro e direto. Cidadão: {texto_usuario}"
        resposta = chat.send_message(prompt)
        return resposta.text
    except Exception as e:
        return f"❌ Erro de conexão com a IA: {e}"

# Renderização do Chat na Tela
# Laço de repetição (for) para desenhar o histórico de mensagens
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada do Usuário (O "input" moderno)
if pergunta := st.chat_input("Digite sua dúvida sobre mobilidade..."):
    
    # Mostra a pergunta do cidadão na tela e salva na memória
    with st.chat_message("user"):
        st.markdown(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    
    # Processa a resposta passando pelas condicionais
    resposta_bot = interpretar_e_responder(pergunta)
    
    # Mostra a resposta do robô na tela e salva na memória
    with st.chat_message("assistant"):
        st.markdown(resposta_bot)
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_bot})