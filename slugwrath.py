import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import os
 
client = Bot(description="I am spell.", command_prefix="Spell ", pm_help = True)
client.remove_command('help')

newUserMessage = """Welcome to Hogwarts. Hogwarts is with you! Check <#452740981666742282>, <#453569407558483968> and <#453189578040541205>. *Wizard/Witch effect added*"""

leaveUserMessage = """Hogwarts is not with you anymore... *Wizard/Witch effect removed*."""


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------------------------------------')
    print('Successfully Learned Spells/Curses!')
    print('Long Live Wizards!')
    return await client.change_presence(game=discord.Game(name='With Spells/Curses.'))
     
@client.event
async def on_member_join(member):
    print("In our server" + member.name + " joined just joined")
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)
 
@client.event
async def on_member_leave(member):
    print("Reporting member leave" + member.name + "is not Wizard/Witch anymore")
    await client.send_message(member, leaveUserMessage)
    print("Sent message to " + member.name)
    
@client.event
async def on_member_leave(member):
    server = member.server
    fmt = '{0.mention} just left {1.name}!'
    await client.send_message(server, fmt.format(member, leaveUserMessage))
     
@client.command(pass_context = True)
async def whois(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Info about user.", color=0x000000)
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
    embed = discord.Embed(colour = 0x000000)
    embed.set_author(name='Help')
    embed.add_field(name = 'help',value ='Explains all the commands',inline = False)
    embed.add_field(name = 'kick(<@&474620468947582996> or above.)',value ='Use it like ``Chaos kick @user`` to kick any user',inline = False)
    embed.add_field(name = 'clear(<@&474620468947582996> or above.)',value ='Use it like ``Chaos clear <number>`` to clear any message',inline = False)
    embed.add_field(name = 'mute(<@&474620468947582996> or above.)',value ='Use it like ``Chaos mute @user <time>`` to mute any user',inline = False)
    embed.add_field(name = 'unmute(<@&474620468947582996> or above.) ',value ='Use it like ``Chaos unmute @user`` to unmute anyone',inline = False)
    embed.add_field(name = 'hirecommander(<@&474571423495749664> only.) ',value ='Use it like ``Chaos hireguard @user`` to give anyone guard role',inline = False)
    embed.add_field(name = 'ban(<@&474619905275199513> or above.) ',value ='Use it like ``Chas ban @user`` to ban any user',inline = False)
    embed.add_field(name = 'warndm(<@&474620468947582996> or above.)',value ='Use it like ``Chaos warndm @user <violation type in one word>`` to warn any user in dm',inline = False)
    embed.add_field(name = 'say (everyone.)',value ='Use it like ``Chaos say <message here>`` to make bot say message.',inline = False)
    embed.add_field(name = 'bans (<@&474572090637287424> and <@&474571423495749664>)',value ='use it like ``Chaos bans```',inline = False)
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
async def warn(ctx, member: discord.Member):
    await client.delete_message(ctx.message)
    await client.send_message(member, 'Please Read <#Rules> and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return
 
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def tellto(ctx, member: discord.Member , msg = None):
    await client.delete_message(ctx.message)
    await client.send_message(member, msg)
    return
 
@client.command(pass_context = True)
async def Avada kedavra(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members:
        await client.ban(member)
        embed=discord.Embed(title="**{1}** used Avada Kedavra on **{0}**!", description="The ancient ones have banned **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0x000000)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x000000)
        await client.say(embed=embed)   	 		 		  
     
@client.command(pass_context = True)
async def boot(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members:
        await client.kick(member)
        embed=discord.Embed(title="User booted!", description="The ancient ones have Kicked **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0x000000)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x000000)
        await client.say(embed=embed)
        
@client.command(pass_context = True)
async def invite(ctx):
     if ctx.message.author.server_permissions.administrator:     
        embed=discord.Embed(title="You can invite me using this link!", description="https://discordapp.com/api/oauth2/authorize?client_id=474575162424033280&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D474575162424033280%26permissions%3D8%26redirect_uri%3Dhttps%253A%252F%252Fdiscordapp.com%252Fapi%252Foauth2%252Fauthorize%253Fclient_id%253D&scope=bot", color=0x000000)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x000000)
        await client.say(embed=embed)
         
  
@client.command(pass_context = True)
@commands.has_permissions(send_messages=True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)
    await client.delete_messages(mgs)
    
@client.command(pass_context=True)  
@commands.has_permissions(send_messages=True)     

async def serverinfo(ctx):
    '''Hogwarts is Wizardly!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channels = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0x000000);
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);
 
       
@client.command(pass_context = True)
async def ducttape(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="The ancient ones have Muted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
          
@client.command(pass_context = True)
async def untape(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="The ancient ones have Unmuted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def accept(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='')
    await client.add_roles(ctx.message.author, role)
 
@client.command(pass_context=True)
async def leave(ctx):
    await client.kick(ctx.message.author)
   
 
   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0x6b009c)
    return await client.say(embed = embed)
   
@client.command(pass_context = True)
async def setup(ctx):
        if ctx.message.author.id == "471988330335174667":
           await client.say("ok")
        else:
           await client.say("Sorry, u are not powerful enough to use this command!")
           
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("My minions can't find role like that! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("Chaotic Minions gave {} to {}.".format(role, user))

        if role in user.roles:
            await client.remove_roles(user, role)
            return await client.say("{} My minions took away role {}!".format(user, role))
         
@client.command(pass_context = True)
@commands.has_permissions(send_messages=True)
async def crucio(ctx, member: discord.Member):
    await client.delete_message(ctx.message)
    await client.ban(member)
      
                                                                                                    
client.run(os.getenv('Token'))
