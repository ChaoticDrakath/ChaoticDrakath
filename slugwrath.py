import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import os
 
client = Bot(description="I corrupt the servers with Chaos", command_prefix="Chaos ", pm_help = True)
client.remove_command('help')
newUserMessage = """Welcome to Crownsreach. Chaos is with you! Check <#452740981666742282>, <#453569407558483968> and <#453189578040541205>. *Chaotic effect added*"""
leaveUserMessage = """Chaos is not with you anymore... *Chaotic effect removed*."""


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
    print("Reporting member leave" + member.name + "is not Chaotic anymore")
    await client.send_message(member, leaveUserMessage)
    print("Sent message to " + member.name)
    
    async def on_member_leave(member):
     server = member.server
     fmt = '{0.mention} just left {1.name}!'
     await client.send_message(server, fmt.format(member, server))
     
@client.command(pass_context = True)
async def whois(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Info about user.", color=0x6b009c)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
     
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = 0x6b009c)
    embed.set_author(name='Help')
    embed.add_field(name = 'help',value ='Explains all the commands',inline = False)
    embed.add_field(name = 'kick(Officers or above.)',value ='Use it like ``Chaos kick @user`` to kick any user',inline = False)
    embed.add_field(name = 'clear(Guards or above.)',value ='Use it like ``Chaos clear <number>`` to clear any message',inline = False)
    embed.add_field(name = 'mute(Officers or above.)',value ='Use it like ``Chaos mute @user <time>`` to mute any user',inline = False)
    embed.add_field(name = 'unmute(Officers or above.) ',value ='Use it like ``Chaos unmute @user`` to unmute anyone',inline = False)
    embed.add_field(name = 'hireguard(Champion only.) ',value ='Use it like ``Chaos hireguard @user`` to give anyone guard role',inline = False)
    embed.add_field(name = 'ban(Officers or above.) ',value ='Use it like ``Chas ban @user`` to ban any user',inline = False)
    embed.add_field(name = 'warndm(Guards or above.)',value ='Use it like ``Chaos warndm @user <violation type in one word>`` to warn any user in dm',inline = False)
    embed.add_field(name = 'say (everyone.)',value ='Use it like ``Chaos say <message here>`` to make bot say message.',inline = False)
    embed.add_field(name = 'bans (Lords and Champion)',value ='use it like ``Chaos bans```',inline = False)
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
        embed=discord.Embed(title="User Banned!", description="The ancient ones have banned **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x6b009c)
        await client.say(embed=embed)   	 		 		  
     
@client.command(pass_context = True)
async def kick(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members:
        await client.kick(member)
        embed=discord.Embed(title="User Kicked!", description="The ancient ones have Kicked **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x6b009c)
        await client.say(embed=embed)
         
  
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)
    await client.delete_messages(mgs)
    
@client.command(pass_context=True)  
@commands.has_permissions(send_messages=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0x6b009c);
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);
 
       
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="The ancient ones have Muted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
          
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="The ancient ones have Unmuted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
   
@client.command(pass_context = True)
async def hireguard(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name='Chaorrupted Guard')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Chaorrupted", description="The ancient ones have chaorrupted **{0}**".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def accept(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='Chaos Hero')
    await client.add_roles(ctx.message.author, role)
   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0x6b009c)
    return await client.say(embed = embed)
                                                                                                    
client.run(os.getenv('Token'))
