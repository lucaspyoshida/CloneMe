from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
from manager_agent.agent import root_agent
from google.genai.types import Content, Part


async def conversar(msg: str, id: str):
    db_url = "sqlite:///./my_agent_data.db"
    memoria = DatabaseSessionService(db_url=db_url)    
    print(f"Msg recebida: {msg}")
    session_act = await memoria.get_session(
        app_name="CloneMe",
        user_id=id,
        session_id=id
    )
    if session_act is None:
        print("Criando sessão...")
        session_act = await memoria.create_session(
            app_name="CloneMe",
            user_id=id,
            session_id=id,
            state={
                "perfil": {},
                "posts_lidos":  []
            }
        )
    runner = Runner(
        agent=root_agent,
        app_name="CloneMe",
        session_service=memoria
    )
    mensagem = Content(
        role='user',
        parts=[
            Part(text=msg)
        ]
    )
    events = runner.run_async(
        user_id=id,
        session_id=session_act.id,
        new_message=mensagem
    )
    respfinal = []
    async for event in events:
        if event.is_final_response():
            respfinal.append(event.content.parts[0].text)
            # print(event.content.parts[0].text)
    print(f"Resposta enviada: {respfinal[-1]}")
    return respfinal[-1] if respfinal else "Nenhuma resposta recebida."
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(conversar("Analise o perfil @sandeco?", "12345"))