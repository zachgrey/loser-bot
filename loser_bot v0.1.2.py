import discord 
from discord.ext import commands, tasks
import random

client = commands.Bot(command_prefix='--')
TOKEN = ''

#help commands

@client.command(name='admin_help')
async def admin_help(context):
    AHelp_embed = discord.Embed(Title='Help') 
    AHelp_embed.add_field(name='ban', value='bans users (admin only)', inline=False)
    AHelp_embed.add_field(name='kick', value='kicks users (admin only)', inline=False)
    AHelp_embed.add_field(name='mute', value='mutes users on the server (admin only)', inline=False)
    AHelp_embed.add_field(name='role', value='gives a already exisiting role to a user (admin only)', inline=False)

    await context.message.channel.send(embed=AHelp_embed)

@client.command(name='command_help')
async def command_help(context):
    command_embed = discord.Embed(Title='Help')
    command_embed.add_field(name='joke', value='tells a random joke', inline=False)
    command_embed.add_field(name='date', value='tells you the currents date', inline=False)
    command_embed.add_field(name='GET_ONLINE', value='@ a user 10 times', inline=False)

    await context.message.channel.send(embed=command_embed)
#admin commands

@client.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member, *, reason=None):
    await member.kick()
    await context.message.channel.send('A user has been kicked from the server')
    

@client.command(name='ban')
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member, *, reason=None):
    guild = context.guild
    await member.ban()
    await context.message.channel.send('A user has been banned from the server')
    

@client.command(name='mute')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


#general commands

Jokes = ['What do you call a mac n cheese that gets all up in your face? Too close for comfort food!', 'What rock group has four men that don’t sing? Mount Rushmore.', 'A cheese factory exploded in France. Da brie is everywhere!', 'Want to hear a joke about construction? Im still working on it!']
@client.command(name='joke')
async def joke(context):
    joke_embed = discord.Embed(title='joke', description=random.choice(Jokes))
    await context.message.channel.send(embed=joke_embed)

#bot info
@client.command(name='bot_info')
async def bot_info(context):
    info_embed = discord.Embed(title='Loser Bot')
    info_embed.add_field(name='vertion', value='Loser Bot: v0.1.0', inline=False)
    info_embed.add_field(name='author', value='bot made by zach grey', inline=False)
    info_embed.add_field(name='github', value='sorce code at https://github.com/zachgrey/loser-bot', inline=False)

    await context.message.channel.send(embed=info_embed)

client.run(TOKEN)