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


client = OpenAI(
    api_key = openaikey
)

prompt = """

Analise critericamente as imagens fornecidas e identifique o estilo visual predominante.
Ao final, você irá retornar um JSON estruturado com as seguintes chaves e valores:

| Campo                                | O que observar                                                                                  |
|--------------------------------------|------------------------------------------------------------------------------------------------|
| `realism_level`                      | Nível de realismo das imagens (fotorealista, ilustrativo, flat_design).                        |
| `scene_types`                        | Tipos de cena frequentes (paisagem, objetos, urbano, retratos).                                 |
| `color_palette.dominant_colors`      | Paleta principal usada.                                                                        |
| `color_palette.accent_colors`        | Cores de destaque secundárias.                                                                 |
| `lighting.type`                      | Tipo de iluminação (natural, artificial, misto).                                                |
| `lighting.direction`                 | Direção da luz (frontal, lateral, contra-luz).                                                  |
| `lighting.intensity`                 | Intensidade da luz (alta, média, baixa).                                                       |
| `exposure.contrast`                  | Nível de contraste predominante.                                                               |
| `exposure.saturation`                | Nível de saturação aplicado.                                                                   |
| `exposure.brightness`                | Brilho típico das imagens.                                                                     |
| `filter_usage.style`                 | Estilo de filtro aplicado (sutil, dramático).                                                  |
| `filter_usage.strength`              | Intensidade do filtro (baixo, médio, alto).                                                    |
| `composition.rule`                   | Regra de composição (regra_dos_terços, simetria).                                              |
| `composition.style`                  | Estilo de composição (minimalista, visualmente carregado, estético).                           |
| `composition.balance`                | Equilíbrio visual (simétrico, assimétrico).                                                    |
| `framing.perspective`                | Perspectiva do enquadramento (ângulo_padrao, de cima).                                         |
| `framing.distance`                   | Distância do enquadramento (plano_médio, close_up).                                            |
| `framing.depth_of_field`             | Profundidade de campo (rasa, profunda).                                                        |
| `geometry.aspect_ratio`              | Relação de aspecto da imagem (1:1, 16:9).                                                      |
| `geometry.orientation`               | Orientação da imagem (quadrado, retrato, paisagem).                                            |
| `overlay_graphics.has_text`          | Se há texto sobreposto nas imagens.                                                            |
| `overlay_graphics.font_style`        | Estilo de fonte do texto sobreposto.                                                           |
| `overlay_graphics.text_position`     | Posição onde o texto aparece (canto_inferior_direito, centro etc.).                            |
| `overlay_graphics.border_style`      | Estilo de bordas ou molduras (nenhum, fino, grosso).                                           |
| `format`                             | Formato de postagem mais comum (carrossel, reels, single).                                     |
| `post_processing.sharpening`         | Nível de nitidez aplicado no pós-processamento.                                                |
| `post_processing.noise_reduction`    | Nível de redução de ruído aplicada no pós-processamento.                                       |
| `mood_and_tone`                      | Clima ou sensação predominante (clean, profissional, artístico, divertido).                    |


Abaixo está um exemplo de saída esperada:

{
 "visual_style": {
    "realism_level": "fotorealista",
    "scene_types": [
      "paisagem",
      "objetos",
      "urbano",
      "retratos"
    ],
    "common_subjects": [
      "notebooks",
      "dashboards",
      "softwares",
      "reuniões"
    ],
    "color_palette": {
      "dominant_colors": ["#1E1E1E", "#FFFFFF", "#FF5722"],
      "accent_colors": ["#03A9F4"],
      "style": "analógico",           
      "dynamic_range": "alto"
    },
    "lighting": {
      "type": "natural",
      "direction": "lateral",
      "intensity": "média"
    },
    "exposure": {
      "contrast": "alto",
      "saturation": "leve",
      "brightness": "normal"
    },
    "filter_usage": {
      "style": "sutil",
      "strength": "baixo"
    },
    "composition": {
      "rule": "regra_dos_terços",
      "style": "minimalista",
      "balance": "simétrico"
    },
    "framing": {
      "perspective": "ângulo_padrao",
      "distance": ["plano_médio", "close_up"],
      "depth_of_field": "rasa"
    },
    "geometry": {
      "aspect_ratio": "1:1",
      "orientation": "quadrado"
    },
    "overlay_graphics": {
      "has_text": true,
      "font_style": "sans_serif_moderno",
      "text_position": "canto_inferior_direito",
      "border_style": "nenhum"
    },
    "mood_and_tone": "tecnológico_e_profissional",
    "format": "carrossel",
    "post_processing": {
      "sharpening": "moderado",
      "noise_reduction": "baixo"
    }
  }
}


Retorne apenas o JSON estruturado, sem explicações adicionais ou formatação de texto.
"""


script_dir = os.path.dirname(os.path.abspath(__file__))
imgs_dir = os.path.abspath(os.path.join(script_dir, "../imgs"))

# Cria lista de imagens codificadas
image_contents = []
for filename in os.listdir(imgs_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        img_path = os.path.join(imgs_dir, filename)
        with open(img_path, "rb") as img_file:
            b64_image = base64.b64encode(img_file.read()).decode("utf-8")
            image_contents.append({
                "type": "input_image",
                "image_url": f"data:image/png;base64,{b64_image}"
            })

content = [{"type": "input_text", "text": prompt}]
content.extend(image_contents)

# Faz requisição
response = client.responses.create(
    model=constants.MODEL_OPENAI,
    input=[
        {
            "role": "user",
            "content": content
        }
    ]
)
print(response.output_text)
