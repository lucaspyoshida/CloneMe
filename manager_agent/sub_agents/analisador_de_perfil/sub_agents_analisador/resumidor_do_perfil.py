from google.adk.agents import Agent
from ....shared import constants


resumidor_do_perfil = Agent(
    name="resumidor_do_perfil",
    description="Agente responsável por resumir o perfil analisado, extraindo informações relevantes e apresentando um resumo conciso.",
    instruction="""Você é um agente especializado em resumir perfis do Instagram.
Sua função é analisar os dados de um perfil que está em JSON e gerar um resumo conciso e informativo.

Segue o perfil a ser analisado:
{perfil}

Ao final, retorne um texto resumido que destaque os principais pontos do perfil, como:
- Principais tópicos abordados
- Estilo de escrita
- Padrões visuais observados
- Qualquer outra informação relevante que possa ser extraída dos dados.
Certifique-se de que o resumo seja claro, objetivo e fácil de entender.
""",
    model=constants.MODEL,
)