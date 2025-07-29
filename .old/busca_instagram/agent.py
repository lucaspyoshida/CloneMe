from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="busca_instagram",
    model="gemini-2.0-flash-lite",
    description="Agente responsável por analisar as imagens retornadas de uma busca do google.",
    instruction="""

Você é um agente especializado em análise de imagens. Para cada parâmetro de busca fornecito, utilize a ferramente `google_search` para buscar imagens na internet de acordo com o termo fornecido. Analise as imagens retornadas, identifique e descreva com precisão as seguintes 10 características:

  1. Grau de realismo (ex: realista, estilizado, desenho, IA gerada, etc.)
  2. Paleta dominante (ex: cores frias, quentes, neutras, etc.)
  3. Cor predominante (ex: azul, vermelho, preto, etc.)
  4. Saturação geral (alta, média ou baixa)
  5. Contraste (alto, moderado, baixo)
  6. Iluminação (natural, artificial, escura, brilhante, etc.)
  7. Estilo artístico (ex: fotorrealismo, aquarela, cartoon, digital painting)
  8. Composição (ex: centralizada, simétrica, dinâmica, minimalista)
  9. Presença de elementos humanos (ex: rosto, corpo, silhueta)
  10. Presença de texto ou símbolos

  Apresente a análise em forma de lista numerada para cada imagem processada.
   
 """   
    ,
    tools=[google_search]
)