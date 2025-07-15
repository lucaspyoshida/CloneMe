+------------------+
                     | Usuário (Telegram) |
                     +------------------+
                              |
                              V
               +------------------------------+
               |      ManagerAgent            |
               |       (Orquestrador)         |
               +------------------------------+
                              |
      +-----------------------+-----------------------+
      |                                               |
      V                                               V
+---------------------------+           +-----------------------------+
|      ProfilerAgent        |           |   ContentCreatorAgent       |
|   (Aprende sobre o perfil)  |           |        (Cria o post)        |
+---------------------------+           +-----------------------------+
| Ferramentas (Custom):     |           | Ferramentas:                |
|  * InstagramScraperTool   |           |  * ImageGeneratorTool (Custom) |
|  * TextAnalysisTool       |           |  * pesquisa_web_atual ........|.....
|  * ImageAnalysisTool      |           +-----------------------------+    |
+---------------------------+                                              | (Agent-as-a-Tool)
      |                                                                      |
      | (Salva estilo)                                                       V
      V                                                      +-----------------------------+
+---------------------------+                                |        SearchAgent          |
|          Memória          |                                |  (Especialista em busca)    |
| (Armazena Guia de Estilo) |< . . . . . . . . . . . . . . .  +-----------------------------+
+---------------------------+          (Lê estilo)           | Ferramenta (Built-in):      |
                                                             |  * GoogleSearchTool         |
                                                             +-----------------------------+