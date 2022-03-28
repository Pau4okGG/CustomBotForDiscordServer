import discord
from discord.ext import commands
from discord import utils
import config

bot = commands.Bot(command_prefix='!', help_command=None)

@bot.event #On start
async def on_ready():
    print('Logged in as {0.user}!'.format(bot))

#!mute @username reason (optional)
@bot.command(description='Mute user.')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason = None):
    guild = ctx.guild

    mutedRole = utils.get(member.guild.roles, id = config.ROLES["Muted"])

    await member.add_roles(mutedRole, reason=reason)
    if reason != None:  
        await ctx.send(f'Muted {member.mention} for {reason}.')    
        await member.send(f"You were muted in the server {member.guild.name} for {reason}.")

    else:
        await member.send(f"You were muted in the server {member.guild.name}.")
        await ctx.send(f'Muted {member.mention}.') 
    try:
        logs = bot.get_channel(config.CHANNELS['logs']) #custom    
        await logs.send(f'Muted {member}.')
    except AttributeError:
        pass


#!unmute @username 
@bot.command(description='Unmute user.')
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = utils.get(member.guild.roles, id = 957616267735498782)

    await member.remove_roles(mutedRole)
    await ctx.send(f'Unmuted {member.mention}')
    await member.send(f"You were unmuted in the server {member.guild.name}!")
    try:
        logs = bot.get_channel(config.CHANNELS['logs']) #custom    
        await logs.send(f'Muted {member}.')
    except AttributeError:
        pass

#Clears chat (!clear amount)
@bot.command(description='Clear chat.')
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount):
    try:
        amount = int(amount)
    except ValueError:
        await ctx.send('```Indicate how much messages to delete (!clear 10)```')

    try:
        await ctx.channel.purge(limit=amount + 1)    
    except TypeError:
        pass

    try:
        logs = bot.get_channel(config.CHANNELS['logs']) #custom    
        await logs.send(f'Muted {member}.')
    except AttributeError:
        pass

#!ban @username reason (optional)
@bot.command(description='Ban user.')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):

    if reason != None:
        await member.ban(reason=reason)
        await ctx.send(f'{member} was banned for {reason}!')

    else:
        await ctx.send(f'{member} was banned!')
    try:
        logs = bot.get_channel(config.CHANNELS['logs']) #custom    
        await logs.send(f'Muted {member}.')
    except AttributeError:
        pass

#!kick @username reason (optional)
@bot.command(description='Kick user.')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):

    if reason != None:
        await member.kick(reason=reason)
        await ctx.send(f'{member} was kicked for {reason}!')

    else:
        await ctx.send(f'{member} was kicked!')
    try:
        logs = bot.get_channel(config.CHANNELS['logs']) #custom    
        await logs.send(f'Muted {member}.')
    except AttributeError:
        pass

#Help command
@bot.command()
async def help(ctx):
    await ctx.send(">>> ```diff\n-List of commands: \n !mute @username reason(optional) \n !unmute @username \n !ban @username reason(optional) \n !kick @username reason(optional) \n !clear amount \n !help (Shows commands)```")

bot.run(config.token)