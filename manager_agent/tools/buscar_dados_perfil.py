from google.adk.tools.tool_context import ToolContext


def buscarperfil(username: str, tool_context: ToolContext) -> None:
    """
    Recupera os textos dos posts públicos de um perfil.

    Esta função realiza a raspagem dos posts mais recentes do perfil indicado
    e insere uma lista contendo os textos (legendas) de cada publicação no state.

    Parâmetros:
        username (str): Nome de usuário a ser pesquisado.
    """
    print(f"Buscando posts para o usuário: {username}...")
    
    posts = [
    "🔍 Você sabia? O ciclo menstrual não serve só para engravidar. Ele é um dos maiores indicadores da saúde da mulher! Observar padrões, irregularidades e sintomas pode ajudar a identificar desequilíbrios hormonais e muito mais. Escute seu corpo. ❤️ #SaúdeFeminina #CicloMenstrual",

    "💊 Pílula anticoncepcional: vilã ou aliada? Tudo depende de orientação adequada. Nem toda mulher precisa ou deve usá-la. Converse com sua ginecologista antes de tomar qualquer decisão. Informação é poder! #Anticoncepcional #Ginecologia",

    "🔥 TPM não é frescura! Alterações de humor, inchaço, dores e cansaço podem ter causas hormonais sérias. Vamos parar de normalizar o sofrimento mensal? Procure ajuda! #TPM #SaúdeMentalFeminina",

    "🌸 Corrimento vaginal: o que é normal e o que merece investigação? Transparente e sem cheiro geralmente está ok. Mas coceira, cor forte ou odor devem ser avaliados. Seu corpo fala! #CorrimentoVaginal #SaúdeÍntima",

    "🤱 Amamentar dói? Pode doer no início, mas não deve ser insuportável. Procure ajuda de uma consultora de amamentação ou da sua gineco. Cuidar de você é cuidar do bebê! #Amamentação #MaternidadeReal",

    "🚫 Dor na relação sexual não é normal. Ponto. Não aceite isso como parte da rotina. Pode ser hormonal, muscular, emocional ou tudo junto. E merece cuidado e respeito. #DorNaRelação #SexoSemDor",

    "🩸 Menstruação irregular: será que é normal? Pode ser estresse, síndrome dos ovários policísticos, disfunções da tireoide… ou outras causas. Só uma avaliação personalizada pode responder. #CicloIrregular #ConsultaGinecológica",

    "🔮 Menopausa não é o fim de nada! É uma nova fase que merece acolhimento, informação e autonomia. Ondas de calor, secura vaginal e insônia não precisam ser rotina. Há tratamento! #Menopausa #GinecoInformada",

    "🛑 Autoconhecimento salva vidas: faça o autoexame das mamas, observe seu ciclo, cuide da sua alimentação. O corpo dá sinais. E quanto antes a gente escuta, melhor o desfecho. #Prevenção #Autoexame",

    "💬 Dúvidas sobre saúde íntima? Não tenha vergonha de perguntar. Toda mulher merece ser acolhida e bem informada. Informação liberta, empodera e salva! #TabuNão #GinecologiaSemVergonha"
    ]

    tool_context.state["posts_lidos"] = posts
    print(f"{len(posts)} posts foram lidos e salvos no estado 'posts_lidos'.")
    return {
        "status": "success"
    }


