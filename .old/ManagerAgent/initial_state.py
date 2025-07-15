# initial_state.py

"""
Este arquivo contém o dicionário que serve como template para o estado inicial
de cada nova sessão do bot. Ele representa um "perfil genérico" de um criador
de conteúdo sobre tecnologia.
"""

initial_state_template = {
    "app_status": {
        "current_mode": "idle",
        "last_action_timestamp": None,
        "last_error": None,
    },
    "profile_data": {
        # << A SER ATUALIZADO APÓS A ANÁLISE >>
        "active_profile_username": None,
        "is_analyzed": False,

        "style_guide": {
            # --- Estilo Textual ---
            "textual_style": {
                # << A SER ATUALIZADO PELO PROFILER AGENT >>
                "main_topics": ["Tecnologia", "Produtividade", "Inteligência Artificial"],
                "secondary_topics": ["Startups", "Carreira"],
                "writing_tone": "informativo_e_acessível",
                "formality_level": "casual_profissional",
                "narrative_voice": "primeira_pessoa_profissional",
                "common_vocabulary": ["workflow", "otimizar", "inovação", "ecossistema"],
                "sentence_complexity": "mista",
                "avg_post_length_words": 120,
                "capitalization_style": "padrão",
                "punctuation_style": "padrão",
                "cta_pattern": "faz_perguntas",
                "mention_frequency": "médio",
                "emoji_usage_pattern": "discreto_no_final",
                "hashtag_strategy": {
                    "avg_count": 5,
                    "placement": "final_do_post",
                    "common_hashtags": ["#tecnologia", "#ia", "#produtividade", "#inovacao"]
                },
                "link_sharing_habit": "raro",
            },
            # --- Estilo Visual ---
            "visual_style": {
                # << A SER ATUALIZADO PELO PROFILER AGENT >>
                "dominant_colors": ["#0D1B2A", "#E0E1DD", "#415A77"], # Paleta de Azul Escuro e Cinza
                "secondary_colors": ["#F07167"], # Cor de destaque (ex: Coral)
                "photography_details": {
                    "contrast": "médio",
                    "saturation": "natural",
                    "brightness": "normal",
                },
                "filter_usage": "sutil",
                "image_type": "fotografia_de_produto",
                "primary_format": "carrossel",
                "common_subjects": ["laptops", "desks organizados", "smartphones", "telas com código"],
                "composition_style": "minimalista",
                "framing_style": "close-up",
                "text_overlay": {
                    "has_text": True,
                    "font_style": "sans_serif_moderno",
                    "text_position": "canto_inferior_esquerdo"
                },
                "border_style": "nenhum",
                "overall_mood": "profissional_e_clean",
            }
        }
    },
    "session_log": {
        "user_id": None, # << A SER ATUALIZADO NO INÍCIO DA SESSÃO >>
        "session_start_time": None, # << A SER ATUALIZADO NO INÍCIO DA SESSÃO >>
        "interaction_history": [],
    }
}