import os

if __name__ == "__main__":
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    from manager_agent.shared import constants
else:
    from ..shared import constants

from dotenv import load_dotenv
from openai import OpenAI
import base64


load_dotenv()

openaikey = os.getenv('OPEN_AI_KEY')

def descreverimagem(b64_image:str) -> str:
    client = OpenAI(
        api_key = openaikey
    )

    prompt = """
    Me dê uma ideia do contexto do ambiente da imagem e do que está ocorrendo na imagem.
    Quais são as expressões faciais predominantes (feliz, triste, neutro, etc.)?                                
    Qual é a expressão emocional delas? 
    Além disso, descreva qualquer objeto ou elemento marcante na cena.
    Tente identificar se é dia ou noite, ambiente aberto ou fechado,
    de festa ou calmo. O que as pessoas estão fazendo?

    Sempre inicie sua respota como "Essa é uma imagem com a seguinte descrição: "
    Termine sempre com a frase: "Crie uma legenda para essa imagem utilizando o criador_de_legendas_para_imagens."
    """

    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # img_path = os.path.join(script_dir, "../imgs/img.png")

    # with open(img_path, "rb") as image_file:
    #     b64_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = client.responses.create(
        model=constants.MODEL_OPENAI,
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
                ],
            }
        ],
    )

    return response.output_text
