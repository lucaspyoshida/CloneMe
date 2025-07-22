import os
from dotenv import load_dotenv
import instaloader

def login_com_sessionid():
    load_dotenv()
    sessionid = os.getenv("SESSIONID")
    username = os.getenv("LOGININSTAGRAM")

    L = instaloader.Instaloader()

    # Injeta o cookie da sessão diretamente
    L.context._session.cookies.set("sessionid", sessionid)
    L.context._session.cookies.set("ds_user_id", os.getenv("DS_USER_ID"))  # IMPORTANTE!

    # Verifica se está logado
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        print(f"Login bem-sucedido como {profile.username}")
    except Exception as e:
        print(f"Erro ao acessar perfil: {e}")

    return L

def baixar_posts_usuario(L: instaloader.Instaloader, nome_usuario: str, limite: int = 10):
    try:
        profile = instaloader.Profile.from_username(L.context, nome_usuario)
        id_usuario = profile.userid
        base_path = f"posts/{id_usuario}"
        img_path = os.path.join(base_path, "img")
        os.makedirs(img_path, exist_ok=True)

        posts_txt_path = os.path.join(base_path, "posts.txt")
        with open(posts_txt_path, "w", encoding="utf-8") as f_txt:
            print(f"Baixando últimos {limite} posts de {nome_usuario}...")
            for idx, post in enumerate(profile.get_posts()):
                if idx >= limite:
                    break
                # Baixa imagem
                post_img_filename = os.path.join(img_path, f"{post.shortcode}.jpg")
                L.download_pic(post_img_filename, post.url, post.date_utc)

                # Salva legenda no txt
                caption = post.caption or "(sem legenda)"
                f_txt.write(f"Post {idx + 1} - {post.shortcode}\n")
                f_txt.write(caption.strip() + "\n\n")

            print(f"Imagens salvas em: {img_path}")
            print(f"Legendas salvas em: {posts_txt_path}")

    except Exception as e:
        print(f"Erro ao baixar posts: {e}")

if __name__ == "__main__":
    L = login_com_sessionid()
    baixar_posts_usuario(L, nome_usuario="sandeco", limite=10)
