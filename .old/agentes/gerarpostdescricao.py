import os
from google import genai

try:
    from tools.parametrospost import parametros
except:
    pass



def gerarpostdescrito(descricao: str):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite-preview-06-17",
        contents=f"""

        Com base na descrição a seguir, gere um texto para uma postagem em redes sociais:
        {descricao}


    O texto a ser gerado deve seguir os seguintes parâmetros de estilo:
    {parametros}

    - Aplique ton de voz, limite de caracteres, emoticons, hashtags, etc.
    - Entregue o texto pronto para publicação.
        """,
    )

    print(response.text)

if __name__ == "__main__":
    import sys
    modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools'))

    if modulo_path not in sys.path:
        sys.path.insert(0, modulo_path)
    from parametrospost import parametros
    from dotenv import load_dotenv
    load_dotenv()
    main()
    
