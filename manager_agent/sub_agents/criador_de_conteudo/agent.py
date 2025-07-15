from google.adk.agents import SequentialAgent
from .sub_agents_criador.criador_post import criador_post
from .sub_agents_criador.buscador_internet import buscador_internet
from .sub_agents_criador.revisor_post import revisor_post

sequencia_criador = SequentialAgent(
    name="sequencia_criador",
    description="Agente responsável por coordenar a criação de conteúdo, acionando o agente `buscador_internet` para coletar informações relevantes e, em seguida, o `criador_post` para gerar o post final.",
    sub_agents=[buscador_internet, criador_post,revisor_post]
)