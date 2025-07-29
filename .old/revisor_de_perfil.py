from google.adk.agents import Agent
from manager_agent.tools.state_schema import StyleGuide
from ....shared import constants

revisor_de_perfil = Agent(
    name="revisor_de_perfil",
    description="Agente responsável por revisar o perfil analisado, garantindo que os dados estejam de acordo com estilo de posts do usuário.",
    instruction="""

Sua missão é comparar criteriosamente o conteúdo do JSON `<perfil>` com os padrões observados nos `<posts>`.

**Regras:**

1. Verifique se todos os campos do JSON estão de acordo com os padrões descritos nos posts.
2. Considere estilo de escrita, vocabulário, emojis, hashtags, formato de imagens, cores, composição visual, etc.
3. Se o JSON estiver consistente com os dados extraídos dos posts, retorne o `<perfil>` como está.
4. Se houver inconsistências, corrija os campos necessários para refletir o estilo real observado e retorne o JSON ajustado.
5. O retorno deve ser **apenas o JSON**, formatado corretamente.

<perfil>
{perfil}
</perfil>

<posts>
{posts_lidos}
</posts>

**Saída esperada:**

Um JSON completo no formato do `<perfil>`, validado ou ajustado conforme necessário.  
    """,
    output_key="perfil",
    output_schema=StyleGuide,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True
)
    