import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

recycling_info = {
    "papel": {
        "texto": "el papel se recicla en el contenedor azul. asegúrate de que esté limpio y sin restos de comida.",
        "curiosidad": "saber: reciclar una tonelada de papel ahorra aproximadamente 17 árboles y 26,500 litros de agua."
    },
    "carton": {
        "texto": "el cartón también va al contenedor azul. plácalo bien para ahorrar espacio.",
        "curiosidad": "saber: el cartón puede reciclarse hasta 5 veces antes de que las fibras se debiliten demasiado."
    },
    "plastico": {
        "texto": "los plásticos van al contenedor amarillo. enjuaga bien los envases antes de tirarlos.",
        "curiosidad": "saber: una botella de plástico tarda entre 450 y 1,000 años en degradarse en la naturaleza."
    },
    "vidrio": {
        "texto": "el vidrio se recicla en el contenedor verde. no incluye cristales rotos ni bombillas.",
        "curiosidad": "saber: el vidrio es 100% reciclable y puede reciclarse infinitas veces sin perder calidad."
    },
    "metal": {
        "texto": "los metales (latas, tapas) van al contenedor amarillo.",
        "curiosidad": "saber: una lata de aluminio reciclada puede estar de nuevo en una estantería en solo 60 días."
    },
    "baterias": {
        "texto": "las baterías y pilas deben llevarse a puntos limpios o contenedores específicos.",
        "curiosidad": "saber: una sola pila puede contaminar hasta 3,000 litros de agua o 600,000 litros de aire."
    },
    "electronicos": {
        "texto": "los aparatos electrónicos no se tiran a la basura. llévalos a un punto limpio.",
        "curiosidad": "saber: los teléfonos móviles contienen metales preciosos como oro y plata que se pueden recuperar."
    },
    "organico": {
        "texto": "los restos orgánicos pueden compostarse o ir al contenedor marrón si tu municipio lo tiene.",
        "curiosidad": "saber: el compostaje reduce las emisiones de metano de los vertederos en un 30%."
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
        
        embed.add_field(name="💡 curiosidad", value=info["curiosidad"], inline=False)
        embed.set_footer(text=f"bot de reciclaje - material: {material.capitalize()}")
        
        await ctx.send(embed=embed)
        
    else:
        await ctx.send(f"no tengo información sobre {material}. prueba con: papel, carton, plastico, vidrio, metal, baterias, electronicos, organico.")

bot.run('TU_TOKEN_AQUI')
