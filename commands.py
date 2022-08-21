import discord
from settings import DISCORD_TOKEN, DISCORD_GUILD, __version__
from discord.ext import commands
from connections import get_people
from discord import ActionRow, Button
import random 

"""
Comandos e eventos do bot
"""

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == DISCORD_GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{DISCORD_GUILD}'    )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name='rt', help='Use !rt para invocar frases aleatórias do bot')
async def quote(ctx):

    

    quotes = [
        
            'Acho que estou com defeito',            
            'Não me chame de filósofo maluco, pote de graxa barrigudo',
            'Meu obtuso amigo, se precisassem da nossa ajuda, teriam pedido. Tem muito a aprender sobre o comportamento humano',
            'Eu sugiro uma nova estratégia: deixe o Wookie ganhar',
            'Oh, meu Deus! Desligue-me! Máquinas fazendo máquinas. Que maldade!',
            'Olá. Eu não acredito que fomos apresentados. Prazer em conhecê-lo. Sou C-3PO, Relações Humano-Ciborgue.'
            
    ]

    response = random.choice(quotes)
    await ctx.send(response)

@bot.command(name=f'people', help="Mostra dados de personagem de Star Wars")
async def all_companies(ctx, *args):

    message = ' '.join(word for word in args)

    embed = discord.Embed(color=0x1E1E1E, type='rich')   
    
    informed_page = message # colhe o numero da pagina pra pedir pra API   

    people, returned_page = get_people(informed_page)    #retorna os dados da API   
    

    name = people['name']   
    birth_year = people['birth_year']
    homeworld = people['homeworld']
    starships = people['starships']    
  
    embed.add_field(name="page", value=returned_page, inline=False)
    embed.add_field(name="name", value=name, inline=False) 
    embed.add_field(name="birth year", value=birth_year, inline=False)
    embed.add_field(name="home world", value=homeworld, inline=False)
    embed.add_field(name="starships", value=starships, inline=False)

    button1 = Button(label="<", custom_id="button1")
    button2 = Button(label=">", custom_id="button2")

    components = ActionRow(button1, button2)

    await ctx.send(embed=embed, components=components)
    




try:
    bot.run(DISCORD_TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")