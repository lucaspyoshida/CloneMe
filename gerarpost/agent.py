import asyncio
import os


from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from dotenv import load_dotenv
import uuid

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

APP_NAME = "GerarPost"
USER_ID = "user123"
def generate_session_id():
    """Gera um session_id aleatório usando UUID4."""
    return str(uuid.uuid4())
SESSION_ID  = generate_session_id()
model = "gemini-2.0-flash-lite-001"

session_service = InMemorySessionService()

session = asyncio.run(session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
))

parametros = """
- Número médio de palavras: 100 a 150
- Tom de escrita: informal, envolvente e direto ao ponto
- Uso de emojis: sim, para destacar pontos importantes e tornar o texto mais atrativo
- Estrutura: frases curtas e parágrafos pequenos para facilitar a leitura
- Chamada para ação: incluir sempre uma sugestão de interação (curtir, comentar, compartilhar, salvar)
- Uso de hashtags: de 3 a 5 hashtags relevantes ao tema
- Público-alvo: linguagem adaptada para jovens adultos e adultos conectados às redes sociais
"""
redator = LlmAgent(
    name="Redator",
    description="Pesquisa o assunto e escreve um texto claro, conciso e informativo.",
    model=model,
    instruction="""
    Receba um argumento `assunto` (string).
    - Use o search_tool para buscar informações.
    - Compile os principais insights em um parágrafo de introdução, desenvolvimento e conclusão.
    """,
    tools=[google_search]
)

# 3) Revisor: ajusta estilo para social media
revisor = LlmAgent(
    name="Revisor",
    description="Refina o texto para redes sociais conforme parâmetros de estilo.",
    model=model,
    instruction=f"""
    Receba o texto bruto gerado pelo Redator e os parâmetros de estilo:
    {parametros}

    - Aplique ton de voz, limite de caracteres, emoticons, hashtags, etc.
    - Entregue o texto pronto para publicação.
    """
)

# 4) Workflow linear: Redator → Revisor
pipeline = SequentialAgent(
    name="PipelineSocial",
    description="Encadeia pesquisa, escrita e revisão para conteúdo de social media.",
    sub_agents=[redator, revisor]
)

# 5) Runner

runner = Runner(
    agent=pipeline,
    app_name=APP_NAME,
    session_service=session_service
)



if __name__ == "__main__":
    content = types.Content(
        role="user",
        parts=[types.Part(text="Escreva sobre copo Camelbak.")]
    )

    events = runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content
    )

    try:
        final = next(
            e for e in events
            if e.author == "Revisor" and e.is_final_response()
        )
        print(final.content.parts[0].text)
    except StopIteration:
        print("❌ Não encontrei a resposta final do Revisor.")
