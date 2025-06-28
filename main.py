from tools.lerimg import lerimg
from agentes.gerarpostdescricao import gerarpostdescrito
from agentes.gerarpostassunto import gerarpostassunto
from dotenv import load_dotenv

load_dotenv()

# descricao = lerimg()
# print(f"Post: {gerarpostdescrito(descricao)}")


assunto = "Como a inteligência artificial está transformando o marketing digital"
print(f"Post: {gerarpostassunto(assunto)}")