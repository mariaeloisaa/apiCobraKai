from fastapi import FastAPI, HTTPException, status, Depends
from model import Personagem
from typing import Optional, Any

app = FastAPI(title="CobraKai | API", description="Conheça os personagens de Cobra Kai!")

personagens ={

    1: {
        "Nome": "Johnny Lawrence",
        "Estilo de Luta": "Cobra Kai",
        "Personalidade": "Arrogante, mas com boa evolução de caráter",
        "Histórico": "Campeão de torneio de karatê nos anos 80, mas depois teve dificuldades na vida adulta.",
        "Foto": "https://static.wikia.nocookie.net/thekaratekid/images/7/75/JohnnyS6FinalSceneProfile.png/revision/latest?cb=20250214060307"
    },
    2: {
        "Nome": "Daniel LaRusso",
        "Estilo de Luta": "Miyagi-Do",
        "Personalidade": "Confiante, sensato, mas por vezes impulsivo",
        "Histórico": "Campeão do torneio de karatê em 1984, aluno de Mr. Miyagi.",
        "Foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fthekaratekid.fandom.com%2Fwiki%2FDaniel_LaRusso&psig=AOvVaw2z3h9zWgiJxgXhl8BrXj_Z&ust=1741871579659000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCj9rjPhIwDFQAAAAAdAAAAABAE"
    },
    3: {
        "Nome": "Miguel Diaz",
        "Estilo de Luta": "Cobra Kai",
        "Personalidade": "Gentil, mas inicialmente inseguro",
        "Histórico": "Começa com dificuldades e evolui como aluno de Johnny Lawrence.",
        "Foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fvillains.fandom.com%2Fwiki%2FMiguel_Diaz&psig=AOvVaw3F7D3pBRCPCkhAmttSpLfn&ust=1741871602142000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPi8zMTPhIwDFQAAAAAdAAAAABAE"
    },
    4: {
        "Nome": "Robby Keene",
        "Estilo de Luta": "Miyagi-Do / Cobra Kai (mistura)",
        "Personalidade": "Rebeldemente bom, determinado",
        "Histórico": "Filho de Johnny Lawrence, começa treinando com Daniel LaRusso.",
        "Foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fvillains.fandom.com%2Fwiki%2FRobby_Keene&psig=AOvVaw2kHHSVCdjn7qylOOjOkGEO&ust=1741871632038000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNCamdHPhIwDFQAAAAAdAAAAABAE"
    },
    5: {
        "Nome": "Tory Nichols",
        "Estilo de Luta": "Cobra Kai",
        "Personalidade": "Impulsiva, determinada, mas com um lado vulnerável",
        "Histórico": "Aluna do Cobra Kai, tem uma rivalidade com Samantha LaRusso.",
        "Foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fvillains.fandom.com%2Fwiki%2FTory_Nichols&psig=AOvVaw297hkyYpQQqONkW8DLYTcI&ust=1741871659063000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIDAit7PhIwDFQAAAAAdAAAAABAE"
    },
    6: {
        "Nome": "Samantha LaRusso",
        "Estilo de Luta": "Miyagi-Do",
        "Personalidade": "Determinada, inteligente, e ética",
        "Histórico": "Filha de Daniel LaRusso, aprende os ensinamentos de seu pai.",
        "Foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F2392346934408437%2Fposts%2F3451910671785386%2F&psig=AOvVaw3CoMcnq5n_SBW62xEtR_nr&ust=1741871676818000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNj27-bPhIwDFQAAAAAdAAAAABAQ"
    },
    7: {
        "Nome": "Falcão (Eli Moskowitz)",
        "Estilo de Luta": "Cobra Kai",
        "Personalidade": "Inseguro no início, mas torna-se mais confiante e agressivo",
        "Histórico": "Começa como um estudante tímido e se transforma em um dos melhores lutadores.",
        "Foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fvillains.fandom.com%2Fwiki%2FEli_%2522Hawk%2522_Moskowitz&psig=AOvVaw3PSFfyfQdKCdJLuoImqBjw&ust=1741871708239000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPDIk_vPhIwDFQAAAAAdAAAAABAE"
    },
    8: {
        "Nome": "Demetri Alexopoulos",
        "Estilo de Luta": "Miyagi-Do (inicialmente)",
        "Personalidade": "Nerd, engraçado, leal",
        "Histórico": "Iniciou no mundo do karatê por pressão, mas ao longo do tempo desenvolve habilidades e confiança.",
        "Foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fcobrakai%2Fcomments%2F15j5z4l%2Fdo_you_consider_demetri_to_be_a_main_character%2F%3Ftl%3Dpt-br&psig=AOvVaw3RMs94RST6BGbsG1YsaaxP&ust=1741871738974000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMC72IPQhIwDFQAAAAAdAAAAABAE"
    },
    9: {
        "Nome": "John Kreese",
        "Estilo de Luta": "Cobra Kai (princípios de combate agressivo e sem piedade)",
        "Personalidade": "Cruel, manipulador, controlador",
        "Histórico": "Fundador do dojo Cobra Kai, um dos maiores antagonistas da série.",
        "Foto": "https://static.wikia.nocookie.net/antagonists/images/0/0e/John_Kreese.png/revision/latest?cb=20230205233056"
    },
    10: {
        "Nome": "Chosen Toguchi",
        "Estilo de Luta": "Miyagi-Do (com variações de Okinawan Karate)",
        "Personalidade": "Inicialmente hostil, mas depois se torna aliado",
        "Histórico": "Antagonista no filme original Karate Kid II, mas mais tarde se torna um aliado de Daniel LaRusso.",
        "Foto": "https://static.wikia.nocookie.net/thekaratekid/images/7/79/ChozenS6FinalSceneProfile.png/revision/latest?cb=20250214055855"
    }
}


# Pegar todos os personagens
@app.get("/personagens", description="Retorna todos os personagens ou retorna nada",  summary="Retorna todos os personagens")
async def get_personagens():
    return personagens 

# Pegar um personagem pelo ID
@app.get("/personagens/{personagem_id}", summary="Retorna um personagem",)
async def get_personagens(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")

#Adicionar novo personagem
@app.post("/personagens",summary="Adiciona novo personagem",status_code=status.HTTP_201_CREATED)
async def post_personagem(personagem: Optional[Personagem]=None):
    next_id = len(personagens)+1
    personagens[next_id]=personagem
    del personagem.id
    return personagem

# Alterar um personagem
@app.put("/personagens/{personagem_id}", summary="Altera um personagem", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: Personagem):
    if personagem_id in personagens:
        personagens[personagem_id]=personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem 
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não existe o personagem com o ID {personagem_id}")
    
# Deletar um personagem
@app.delete("/personagens/{personagem_id}", summary="Deleta um personagem", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não existe o personagem com o ID {personagem_id}")

# Alterar parcialmente um personagem
@app.patch("/personagens/{personagem_id}", summary="Altera parcialmente um personagem", status_code=status.HTTP_202_ACCEPTED)
async def patch_personagem(personagem_id: int, nome: Optional[str] = None, estilo_de_luta: Optional[str] = None, 
                           personalidade: Optional[str] = None, historico: Optional[str] = None, foto: Optional[str] = None):
    if personagem_id in personagens:
        personagem = personagens[personagem_id]
        
        if nome:
            personagem["Nome"] = nome
        if estilo_de_luta:
            personagem["Estilo de Luta"] = estilo_de_luta
        if personalidade:
            personagem["Personalidade"] = personalidade
        if historico:
            personagem["Histórico"] = historico
        if foto:
            personagem["Foto"] = foto
        
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe o personagem com o ID {personagem_id}")


if __name__ =="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="info", reload=True)


