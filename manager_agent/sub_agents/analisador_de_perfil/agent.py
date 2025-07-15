from google.adk.agents import SequentialAgent
from .sub_agents_analisador.analisador_em_si import analisador_de_perfil
from .sub_agents_analisador.leitor_de_dados import leitor_de_dados
from .sub_agents_analisador.resumidor_do_perfil import resumidor_do_perfil
from .sub_agents_analisador.revisor_de_perfil import revisor_de_perfil


sequencia_analisador = SequentialAgent(
    name="sequencia_analisador",
    description="Agente responsável por coordenar a análise de perfis do Instagram, executando o agente `leitor_de_dados` para coletar os posts e, em seguida, acionando o `analisador_de_perfil` para processar esses dados e atualizar o estado global do sistema.",
    sub_agents=[leitor_de_dados, analisador_de_perfil,revisor_de_perfil,resumidor_do_perfil]
)