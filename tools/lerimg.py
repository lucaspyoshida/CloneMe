import os
import base64
from openai import OpenAI


IMAGE_PATH = "imgs/imagem.jpg"

def encode_image_to_base64(path: str) -> str:
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def lerimg():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Erro: defina a variável de ambiente OPENAI_API_KEY.")
        return

    client = OpenAI(api_key=api_key)

    if not os.path.exists(IMAGE_PATH):
        print(f"Erro: não foi possível encontrar a imagem '{IMAGE_PATH}'.")
        return

    img_b64 = encode_image_to_base64(IMAGE_PATH)

    messages = [
        {"role": "system", "content": "Você é um assistente especializado em descrever imagens de forma detalhada e clara."},
        {"role": "user", "content": (
            "Por favor, forneça uma descrição detalhada da imagem a seguir. "
            f"Ela está codificada em base64 abaixo:\n\n{img_b64}"
        )}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano-2025-04-14",
            messages=messages,
            temperature=0.7
        )
        descricao = response.choices[0].message.content
        return descricao
    
    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API do OpenAI: {e}")


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    lerimg()
