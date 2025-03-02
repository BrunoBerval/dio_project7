# dio_project7
Virtual Assistant

# Voice Assistant with Groq API

Este projeto é um assistente de voz baseado em Python que utiliza a API da Groq para processar comandos e responder interativamente. Ele permite capturar áudio via microfone, reconhecer a fala, interpretar comandos personalizados e obter respostas através da IA da Groq.

## Recursos
- Conversão de fala para texto utilizando a biblioteca `speech_recognition`.
- Conversão de texto para fala com `pyttsx3`.
- Comunicação com a API da Groq para processar e responder perguntas.
- Execução de comandos personalizados por meio do módulo `command_list`.
- Interação contínua até que o usuário encerre o programa.

## Configuração

### 1. Clonar o repositório
```sh
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2. Instalar dependências
Certifique-se de ter o Python instalado e execute:
```sh
pip install -r requirements.txt
```

### 3. Configurar a variável de ambiente da API Key
Para utilizar a API da Groq, é necessário definir a chave de autenticação. Para isso:

**No Windows (cmd):**
```sh
set GROQ_API_KEY=SUA_CHAVE_AQUI
```

**No Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="SUA_CHAVE_AQUI"
```

**No Linux/macOS:**
```sh
export GROQ_API_KEY=SUA_CHAVE_AQUI
```

### 4. Acessar a API da Groq
Para obter uma chave de API, acesse o site da [Groq](https://groq.com/) e crie uma conta. Após o login, gere sua API Key na área de configurações.

### 5. Executar o assistente
Após configurar a chave, basta rodar o script:
```sh
python virtual_assitant.py
```
Agora, o assistente de voz estará pronto para interagir com você!

---
Caso tenha dúvidas ou precise de melhorias, contribuições são bem-vindas!

