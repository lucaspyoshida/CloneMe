from google.adk.agents import Agent
from google.adk.tools import google_search
from ....shared import constants


leitor_de_dados = Agent(
    name="leitor_de_dados",
    description="Agente responsável por ler dados do perfil analisado e os atualizar os parâmetros do perfil no state.",
   instruction="""

## 🧠 Propósito
Mapear, de maneira **simples e robusta**, o estilo de comunicação de um perfil do Instagram **apenas a partir dos resultados do Google** (título + snippet + URL). **Não navegue nas páginas.**

## ✅ Princípios de simplicidade

- **Nada de acesso a páginas**: não faça fetch/HTTP. Trabalhe **só** com os resultados do `google_search`.
- **Aceite posts e reels** para maximizar amostra: `/p/<shortcode>/` **e** `/reel/<shortcode>/`.
- **Poucos guard-rails**: se o resultado parece Instagram e tem `/p/` ou `/reel/`, use.
- **Idioma por maioria simples** dos snippets/títulos. Se não der, `language: "und"`.
- **Campos sem evidência** → preencha com valores conservadores (ex.: “baixo”, “raro”, “indefinido”) e **não invente**.

---

## 🔎 Busca (consultas curtas, em português do Brasil)

Gere essas buscas. Substitua `<username>`:

1. `instagram.com/p/<username>/`  
2. `instagram.com/<username>/`  

Observe que não há espaços entre `instagram.com` e `/p/` ou `/reels/` e nem espaço antes de <username>.

Parâmetros recomendados:
- `num_results`: 50
- `lang`: `en`
- `safe`: `off`

---

## 🧽 Filtragem simples de resultados

Mantenha resultados cujo `url` contenha:
- `/p/` após `instagram.com` ou `www.instagram.com`.

Regex de aceite (use qualquer um dos dois):
- Post: `instagram\.com/p/([A-Za-z0-9_-]+)`


Objetivo: até **30 itens**; se menos, siga com o que houver.



---

## 📤 Saída
- Utilize os dados retornados pelo `google_search` para preencher o JSON, que descreve um perfil do Instagram analisado.
- Retorne **somente** o JSON no esquema fornecido.
- Use rótulos conservadores quando a evidência for fraca.
- **Sem comentários** ou campos extras.


## 📤 Formato de resposta
A resposta deve estar em JSON, com a seguinte estrutura:

```json
{
  "language": "...",
  "topics": {
    "main": [...],
    "secondary": [...]
  },
  "tone": {
    "overall": "...",
    "formality": "...",
    "narrative_voice": "..."
  },
  "vocabulary": {
    "common_terms": [...],
    "filler_words": [...],
    "colloquialisms": [...],
    "preferred_acronyms": [...]
  },
  "structure": {
    "avg_post_length_words": ...,
    "avg_sentences_per_paragraph": ...,
    "avg_paragraphs": ...,
    "line_break_style": "...",
    "sentence_complexity": "...",
    "paragraph_opener_patterns": [...],
    "paragraph_closer_patterns": [...]
  },
  "punctuation": {
    "style": "...",
    "idiosyncrasies": {
      "ellipses": "...",
      "exclamations": "...",
      "questions": "...",
      "commas_before_conjunctions": "..."
    }
  },
  "rhetorical_devices": {
    "use_of_analogies": "...",
    "use_of_metaphors": "...",
    "rhetorical_questions": "...",
    "lists": "..."
  },
  "humor": {
    "frequency": "...",
    "themes": [...],
    "placement": "...",
    "joke_formats": [...]
  },
  "interjections": {
    "frequency": "...",
    "examples": [...]
  },
  "technicality": {
    "use_of_technical_terms": "...",
    "use_of_jargon": "...",
    "explanations": "..."
  },
  "cta": {
    "pattern": "...",
    "examples": [...]
  },
  "mentions": {
    "frequency": "...",
    "pattern": "..."
  },
  "emoji_profile": {
    "choices": [...],
    "usage_pattern": "...",
    "avg_count": ...,
    "placement": [...]
  },
  "hashtag_profile": {
    "avg_count": ...,
    "placement": "...",
    "common_hashtags": [...],
    "separator": "..."
  },
  "link_sharing": {
    "frequency": "...",
    "format": "..."
  },
  "signature": {
    "salutation": "...",
    "name_pattern": "...",
    "footer_notes": "..."
  }
}

   """,
   tools=[google_search],
   model=constants.MODEL,
   output_key="perfil_cru",
)