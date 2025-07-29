from pydantic import BaseModel, Field
from typing import List, Literal





class Topics(BaseModel):
    main: List[str] = Field(..., description="Tópicos principais dos posts.")
    secondary: List[str] = Field(..., description="Tópicos recorrentes, mas menos frequentes.")

class Tone(BaseModel):
    overall: str = Field(..., description="Tom geral (ex: informativo_e_motivacional, inspirador, técnico).")
    formality: str = Field(..., description="Nível de formalidade (ex: casual_profissional, informal, técnico).")
    narrative_voice: str = Field(..., description="Voz narrativa (ex: primeira_pessoa_profissional, impessoal).")

class Vocabulary(BaseModel):
    common_terms: List[str] = Field(..., description="Palavras e expressões usadas com frequência.")
    filler_words: List[str] = Field(..., description="Expressões de preenchimento (ex: basicamente, tipo, na real).")
    colloquialisms: List[str] = Field(..., description="Gírias e coloquialismos.")
    preferred_acronyms: List[str] = Field(..., description="Acrônimos preferidos (ex: AI, ML, API).")

class Structure(BaseModel):
    avg_post_length_words: int = Field(..., description="Média de palavras por legenda.")
    avg_sentences_per_paragraph: int = Field(..., description="Média de frases por parágrafo.")
    avg_paragraphs: int = Field(..., description="Média de parágrafos por post.")
    line_break_style: Literal["quebra_entre_parágrafos", "sem_quebra", "quebra_completa"] = Field(...)
    sentence_complexity: str = Field(..., description="Complexidade das frases.")
    paragraph_opener_patterns: List[str] = Field(..., description="Padrões para iniciar parágrafos.")
    paragraph_closer_patterns: List[str] = Field(..., description="Padrões para fechar parágrafos.")

class Idiosyncrasies(BaseModel):
    ellipses: Literal["raro", "ocasional", "frequente"] = Field(...)
    exclamations: Literal["raro", "ocasional", "frequente"] = Field(...)
    questions: Literal["raro", "ocasional", "frequente"] = Field(...)
    commas_before_conjunctions: Literal["raro", "ocasional", "frequente"] = Field(...)

class Punctuation(BaseModel):
    style: Literal["padrão", "com_emojis", "com_interjeições", "padrão_com_emojis"] = Field(...)
    idiosyncrasies: Idiosyncrasies = Field(...)

class RhetoricalDevices(BaseModel):
    use_of_analogies: Literal["raro", "ocasional", "frequente"] = Field(...)
    use_of_metaphors: Literal["raro", "ocasional", "frequente"] = Field(...)
    rhetorical_questions: Literal["raro", "ocasional", "frequente_no_final_parágrafo"] = Field(...)
    lists: Literal["raro", "ocasional", "bullet_points", "enumerações", "bullet_points_ocasional"] = Field(...)

class Humor(BaseModel):
    frequency: Literal["raro", "ocasional", "frequente"] = Field(...)
    themes: List[str] = Field(...)
    placement: Literal["início", "meio", "final", "normalmente_no_meio_do_texto"] = Field(...)
    joke_formats: List[str] = Field(...)

class Interjections(BaseModel):
    frequency: Literal["raro", "ocasional", "frequente"] = Field(...)
    examples: List[str] = Field(...)

class Technicality(BaseModel):
    use_of_technical_terms: Literal["baixo", "moderado", "alto"] = Field(...)
    use_of_jargon: Literal["baixo", "moderado", "alto"] = Field(...)
    explanations: Literal["nunca", "às_vezes", "sempre_que_técnico"] = Field(...)

class CTA(BaseModel):
    pattern: str = Field(..., description="Padrão de chamadas para ação.")
    examples: List[str] = Field(...)

class Mentions(BaseModel):
    frequency: Literal["baixo", "médio", "alto"] = Field(...)
    pattern: str = Field(...)

class EmojiProfile(BaseModel):
    choices: List[str] = Field(...)
    usage_pattern: str = Field(...)
    avg_count: int = Field(...)
    placement: List[str] = Field(...)

class HashtagStrategy(BaseModel):
    avg_count: int = Field(...)
    placement: Literal["final_do_post", "início_do_post", "misturado"] = Field(...)
    common_hashtags: List[str] = Field(...)
    separator: Literal["espaço", "quebra_de_linha"] = Field(...)

class LinkSharing(BaseModel):
    frequency: Literal["raro", "ocasional", "frequente"] = Field(...)
    format: Literal["URL_encurtada", "URL_cheia"] = Field(...)

class Signature(BaseModel):
    salutation: str = Field(...)
    name_pattern: str = Field(...)
    footer_notes: str = Field(...)

class TextualStyle(BaseModel):
    perfil_base: str = Field(..., description="Nome do perfil base de onde o estilo foi extraído.")
    language: str = Field(..., description="Idioma predominante dos posts.")
    topics: Topics
    tone: Tone
    vocabulary: Vocabulary
    structure: Structure
    punctuation: Punctuation
    rhetorical_devices: RhetoricalDevices
    humor: Humor
    interjections: Interjections
    technicality: Technicality
    cta: CTA
    mentions: Mentions
    emoji_profile: EmojiProfile
    hashtag_profile: HashtagStrategy
    link_sharing: LinkSharing
    signature: Signature






class ColorPalette(BaseModel):
    dominant_colors: List[str] = Field(..., description="Cores predominantes nas imagens do perfil.")
    accent_colors: List[str] = Field(..., description="Cores de destaque secundárias.")
    style: str = Field(..., description="Estilo de aplicação de cores (ex: analógico, vibrante).")
    dynamic_range: str = Field(..., description="Amplitude dinâmica de cores (ex: alto, médio, baixo).")

class Lighting(BaseModel):
    type: Literal["natural", "artificial", "misto"] = Field(..., description="Tipo de iluminação utilizada nas fotos.")
    direction: str = Field(..., description="Direção da luz (ex: frontal, lateral, contra-luz).")
    intensity: str = Field(..., description="Intensidade da luz (ex: alta, média, baixa).")

class Exposure(BaseModel):
    contrast: str = Field(..., description="Nível de contraste predominante nas imagens.")
    saturation: str = Field(..., description="Nível de saturação aplicado nas imagens.")
    brightness: str = Field(..., description="Brilho típico das imagens postadas.")

class FilterUsage(BaseModel):
    style: str = Field(..., description="Estilo de filtro aplicado (ex: sutil, dramático).")
    strength: str = Field(..., description="Intensidade do filtro (ex: baixo, médio, alto).")

class Composition(BaseModel):
    rule: str = Field(..., description="Regra de composição predominante (ex: regra_dos_terços).")
    style: str = Field(..., description="Estilo de composição visual (ex: minimalista, simétrico).")
    balance: str = Field(..., description="Equilíbrio visual (ex: simétrico, assimétrico).")

class Framing(BaseModel):
    perspective: str = Field(..., description="Perspectiva de enquadramento (ex: ângulo_padrao, de cima).")
    distance: List[str] = Field(..., description="Distância do enquadramento (ex: plano_médio, close_up).")
    depth_of_field: str = Field(..., description="Profundidade de campo (ex: rasa, profunda).")

class Geometry(BaseModel):
    aspect_ratio: str = Field(..., description="Relação de aspecto da imagem (ex: 1:1, 16:9).")
    orientation: Literal["quadrado", "retrato", "paisagem"] = Field(..., description="Orientação da imagem.")

class OverlayGraphics(BaseModel):
    has_text: bool = Field(..., description="Indica se as imagens geralmente têm texto sobreposto.")
    font_style: str = Field(..., description="Estilo de fonte utilizado no texto das imagens.")
    text_position: str = Field(..., description="Posição onde o texto sobreposto costuma aparecer.")
    border_style: str = Field(..., description="Estilo de bordas das imagens.")

class PostProcessing(BaseModel):
    sharpening: str = Field(..., description="Nível de nitidez aplicado no pós-processamento.")
    noise_reduction: str = Field(..., description="Nível de redução de ruído aplicada.")

class VisualStyle(BaseModel):
    realism_level: Literal["fotorealista", "ilustrativo", "flat_design"] = Field(..., description="Nível de realismo das imagens.")
    scene_types: List[str] = Field(..., description="Tipos de cena frequentes (ex: paisagem, objetos, urbano, retratos).")
    common_subjects: List[str] = Field(..., description="Temas visuais frequentemente representados.")
    color_palette: ColorPalette = Field(..., description="Paleta de cores predominante nas imagens.")
    lighting: Lighting = Field(..., description="Detalhes de iluminação das fotos.")
    exposure: Exposure = Field(..., description="Configurações de exposição das imagens.")
    filter_usage: FilterUsage = Field(..., description="Uso de filtros nas imagens.")
    composition: Composition = Field(..., description="Estilo de composição visual.")
    framing: Framing = Field(..., description="Parâmetros de enquadramento das imagens.")
    geometry: Geometry = Field(..., description="Aspectos geométricos das imagens.")
    overlay_graphics: OverlayGraphics = Field(..., description="Informações sobre texto e bordas sobrepostas.")
    mood_and_tone: str = Field(..., description="Clima ou sensação geral transmitida pelas fotos.")
    format: Literal["carrossel", "reels", "single"] = Field(..., description="Formato de postagem mais comum.")
    post_processing: PostProcessing = Field(..., description="Ajustes de pós-processamento aplicados.")




class StyleGuide(BaseModel):
    textual_style: TextualStyle = Field(..., description="Guia de estilo textual extraído do perfil.")
    visual_style: VisualStyle = Field(..., description="Guia de estilo visual extraído do perfil.")
