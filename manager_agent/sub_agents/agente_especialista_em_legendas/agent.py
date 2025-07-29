from google.adk.agents import SequentialAgent
from .sub_agentes_legenda.criador_de_legenda import criador_de_legenda
from .sub_agentes_legenda.revisor_de_legenda import revisor_de_legenda


agente_especialista_em_legendas = SequentialAgent(
    name="agente_especialista_em_legendas",
    description="Agente responsável por coordenar a criação de legendas para imagens, garantindo que estejam alinhadas com o perfil do usuário.",
    sub_agents=[criador_de_legenda, revisor_de_legenda]
)