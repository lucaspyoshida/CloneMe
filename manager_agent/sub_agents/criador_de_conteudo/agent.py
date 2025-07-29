from google.adk.agents import SequentialAgent
from .sub_agents_criador.criador_post import criador_post
from .sub_agents_criador.buscador_internet import buscador_internet
from .sub_agents_criador.revisor_post import revisor_post

sequencia_criador = SequentialAgent(
    name="sequencia_criador",
    description="Coordena a criação de posts textuais acionando buscador_internet para pesquisa e criador_post para redação e revisor_post para revisão, sendo usado apenas quando o pedido não envolve imagens, descrição de imagens nem análise de perfil.",
    sub_agents=[buscador_internet, criador_post,revisor_post]
)