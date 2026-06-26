import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

recycling_info = {
    "papel": {
        "texto": "el papel se recicla en el contenedor azul. asegúrate de que esté limpio y sin restos de comida.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Blue_recycling_bin.jpg/640px-Blue_recycling_bin.jpg"
    },
    "carton": {
        "texto": "el cartón también va al contenedor azul. plácalo bien para ahorrar espacio.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Cardboard_boxes_recycling.jpg/640px-Cardboard_boxes_recycling.jpg"
    },
    "plastico": {
        "texto": "los plásticos van al contenedor amarillo. enjuaga bien los envases antes de tirarlos.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Yellow_recycling_bin.jpg/640px-Yellow_recycling_bin.jpg"
    },
    "vidrio": {
        "texto": "el vidrio se recicla en el contenedor verde. no incluye cristales rotos ni bombillas.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Green_recycling_bin.jpg/640px-Green_recycling_bin.jpg"
    },
    "metal": {
        "texto": "los metales (latas, tapas) van al contenedor amarillo.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Yellow_recycling_bin.jpg/640px-Yellow_recycling_bin.jpg"
    },
    "baterias": {
        "texto": "las baterías y pilas deben llevarse a puntos limpios o contenedores específicos.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Battery_recycling_bin.jpg/640px-Battery_recycling_bin.jpg"
    },
    "electronicos": {
        "texto": "los aparatos electrónicos no se tiran a la basura. llévalos a un punto limpio.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/E-waste_recycling.jpg/640px-E-waste_recycling.jpg"
    },
    "organico": {
        "texto": "los restos orgánicos pueden compostarse o ir al contenedor marrón si tu municipio lo tiene.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Brown_recycling_bin.jpg/640px-Brown_recycling_bin.jpg"
    }
}

@bot.event
async def on_ready():
    print(f'bot conectado como {bot.user}')

@bot.command(name='reciclar')
async def reciclar(ctx, *, material: str):
    material = material.lower()
    
    if material in recycling_info:
        info = recycling_info[material]
        
        embed = discord.Embed(
            title=f"¿cómo reciclar {material}?",
            description=info["texto"],
            color=discord.Color.green()
        )
        await ctx.send(url=info["imagen"])

        embed.set_footer(text=f"bot de reciclaje - material: {material.capitalize()}")
        
        await ctx.send(embed=embed)
        
    else:
        await ctx.send(f"no tengo información sobre {material}. prueba con: papel, carton, plastico, vidrio, metal, baterias, electronicos, organico.")

bot.run("token")
