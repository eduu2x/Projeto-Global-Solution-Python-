# 🏙️ Assistente CitizenTech - Mobilidade Urbana

## 📋 Sobre o Projeto
Este projeto foi desenvolvido como avaliação da para a Global solution na disciplina de **Pensamento Computacional e Automação em Python**. Trata-se de uma aplicação web interativa focada em **Mobilidade Urbana**, alinhada ao conceito de **CitizenTech** (Tecnologia Cidadã). 

O sistema funciona como um assistente virtual inteligente capaz de tirar dúvidas, informar status de transportes e receber relatos do cidadão, utilizando uma interface amigável e processamento de linguagem natural.

---

## 🚀 Tecnologias Utilizadas
O projeto foi construído **100% em Python**, sem a necessidade de frameworks front-end externos (como HTML/JS), respeitando o escopo da disciplina.
* **Linguagem:** Python 3
* **Interface Gráfica (Frontend):** Streamlit
* **Inteligência Artificial:** Google Gemini API (`google-genai`)
* **Versionamento:** Git e GitHub
* **Deploy/Hospedagem:** Streamlit Community Cloud

---

## 🧠 Requisitos Acadêmicos Atendidos (Pensamento Computacional)
O código fonte demonstra o domínio das seguintes estruturas e lógicas de programação:

1. **Modularização e Funções (`def`):** A lógica central não é sequencial, mas sim dividida em funções reutilizáveis (como o processamento das mensagens e a chamada da API).
2. **Condicionais (`if/elif/else`):** Utilizadas para o roteamento inteligente, decidindo quando a resposta deve vir do banco de dados local ou quando a IA deve ser acionada.
3. **Estruturas de Dados (`dict` e `list`):** Uso de dicionários para simular uma base de dados local ultra-rápida (status de transporte) e listas para armazenar o histórico de conversa.
4. **Laços de Repetição (`for`):** Aplicados na varredura da base local e na renderização do histórico de mensagens na tela do usuário.
5. **Tratamento de Exceções (`try/except`):** Implementação de resiliência contra quedas do servidor do Google (ex: Erro 503), garantindo que a aplicação não quebre e exiba uma mensagem amigável ao cidadão.

---

## ⚙️ Como executar o projeto localmente

### Pré-requisitos
* Python 3 instalado
* Chave de API do Google Gemini

### Passo a passo
1. Clone este repositório:
```bash
git clone https://github.com/eduu2x/Projeto-Global-Solution-Python-.git
```

2. Acesse a pasta do projeto:
```bash
cd Projeto-Global-Solution-Python-
```

3. Instale as dependências:
```bash
python -m pip install -r requirements.txt
```

4. Configure a sua chave de API:
Crie uma pasta chamada `.streamlit` na raiz do projeto, e dentro dela um arquivo chamado `secrets.toml`. Adicione sua chave da seguinte forma:
```toml
GEMINI_API_KEY = "SUA_CHAVE_AQUI"
```

5. Execute a aplicação:
```bash
python -m streamlit run app.py
```

---

## 🌐 Deploy
O projeto está hospedado e disponível para uso através do Streamlit Community Cloud. As variáveis de ambiente (Secrets) foram devidamente configuradas na plataforma para proteger as credenciais de acesso à API.

Site do projeto: https://it7eikwrztva7dwm7jymyt.streamlit.app/