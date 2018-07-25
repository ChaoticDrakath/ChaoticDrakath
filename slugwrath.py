import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import os
 
client = Bot(description="I corrupt the servers with Chaos", command_prefix="Chaos ", pm_help = True)
client.remove_command('help')
newUserMessage = """Welcome to Crownsreach. Hope you will be active here. Check <#452740981666742282>, <#453569407558483968> and <#453189578040541205>."""


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------------------------------------')
    print('Successfully Summoned Chaos!')
    print('Long Live Chaos!')
    return await client.change_presence(game=discord.Game(name='Youtube with Drakath#3722'))
     
@client.event
async def on_member_join(member):
    print("In our server" + member.name + " joined just joined")
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)
 
@client.event
async def on_member_leave(member):
    server = member.server
    fmt = '{0.mention} just left {1.name}!'
    await client.send_message(server, fmt.format(member, server))
    
    async def on_member_leave(member):
     server = member.server
     fmt = '{0.mention} just left {1.name}!'
     await client.send_message(server, fmt.format(member, server))
     
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.Purple())
    embed.set_author(name='Help')
    embed.add_field(name = 'help',value ='Explains all the commands',inline = False)
    embed.add_field(name = 'kick(Officers or above.)',value ='Use it like ``Chaos kick @user`` to kick any user',inline = False)
    embed.add_field(name = 'clear(Guards or above.)',value ='Use it like ``Chaos clear <number>`` to clear any message',inline = False)
    embed.add_field(name = 'mute(Officers or above.)',value ='Use it like ``Chaos mute @user <time>`` to mute any user',inline = False)
    embed.add_field(name = 'unmute(Officers or above.) ',value ='Use it like ``Chaos unmute @user`` to unmute anyone',inline = False)
    embed.add_field(name = 'friend(Champion or above.) ',value ='Use it like ``Chaos friend @user`` to give anyone friend role',inline = False)
    embed.add_field(name = 'ban(Officers or above.) ',value ='Use it like ``Chas ban @user`` to ban any user',inline = False)
    embed.add_field(name = 'warndm(Guards or above.)',value ='Use it like ``Chaos warndm @user <violation type in one word>`` to warn any user in dm',inline = False)
    embed.add_field(name = 'say (everyone.)',value ='Use it like ``Chaos warndm @user <violation type in one word>`` to warn any user in dm',inline = False)
    await client.send_message(author,embed=embed)
      
@client.command(pass_context = True)
@commands.has_permissions(send_messages=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)
 
    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return

@client.command(pass_context = True)
@commands.has_permissions(mute_members=True)
async def warndm(ctx, member: discord.Member):
    await client.delete_message(ctx.message)
    await client.send_message(member, 'Please Read <#Rules> and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return
 
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def dm(ctx, member: discord.Member , msg = None):
    await client.delete_message(ctx.message)
    await client.send_message(member, msg)
    return
 
@client.command(pass_context = True)
async def ban(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members:
        await client.ban(member)
        embed=discord.Embed(title="User Banned!", description="The ancient ones have banned **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0xff00f6)
        await client.say(embed=embed)
 
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
 
 
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)
 
    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))
 
    # Unban last banned user
    if not ban_list:
     	
        await client.say('Ban list is empty.')
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('unban failed.')
        return		      	 		 		  
     
@client.command(pass_context = True)
async def kick(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members:
        await client.kick(member)
        embed=discord.Embed(title="User Kicked!", description="The ancient ones have Kicked **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0xff00f6)
        await client.say(embed=embed)
         
  
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)
    await client.delete_messages(mgs)      
 
       
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="The ancient ones have Muted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0xff00f6)
        await bot.say(embed=embed)
          
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="The ancient ones have Unmuted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0xff00f6)
        await bot.say(embed=embed)
      
                                                                                                
 
 
client.run(os.getenv('Token'))
