import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import colorsys
import random
import os
 
client = Bot(description="I am wand.", command_prefix="spell ", pm_help = True)
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='Looking for spell book'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Currently in development.'))
        await asyncio.sleep(10)
        
async def status_taskk():
    while True:
      server = client.get_server(id="474572009263857684")
       r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
       role_name = discord.utils.get(server.roles, name='Utkarsh Kumar')
        await client.edit_role(message.server, role, name=role_name, colour=discord.Color((r << 16) + (g << 8) + b))



@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------------------------------------')
    print('Successfully Learned Spells/Curses!')
    print('Long Live Wizards!')
    client.loop.create_task(status_task())
    client.loop.create_task(status_taskk())
    
@client.event
async def on_member_join(member):
   
   if member.server.id == "476628581536235533":
    

    print("In our server" + member.name + " just joined")
    
    embed = discord.Embed(color = 0x000000)
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='**Hope you will be active here. Check Our server rules and never try to break any rules. Also join our official server- https://discord.gg/**',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await client.send_message(member,embed=embed)
   
    print("Sent message to " + member.name)

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
async def book(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = 0x000000)
    embed.set_author(name='Book of Spells and Curses.')
    embed.add_field(name = 'book',value ='Explains all the commands',inline = False)
    embed.add_field(name = 'sectumsempra(<@&474620468947582996> or above.)',value ='Use it like ``spell expelliarmus @user`` to kick any user',inline = False)
    embed.add_field(name = 'clear(<@&474620468947582996> or above.)',value ='Use it like ``spell clear <number>`` to clear any message',inline = False)
    embed.add_field(name = 'crucio(<@&474620468947582996> or above.)',value ='Use it like ``spell mute @user <time>`` to mute any user',inline = False)
    embed.add_field(name = 'uncrucio(<@&474620468947582996> or above.) ',value ='Use it like ``spell unmute @user`` to unmute anyone',inline = False)
    embed.add_field(name = 'avadakedavra(<@&474619905275199513> or above.) ',value ='Use it like ``spell avadakedarva @user`` to ban any user',inline = False)
    embed.add_field(name = 'warn(mods)(Mute_members permission.)',value ='Use it like ``spell warndm @user <violation type in one word>`` to warn any user in dm',inline = False)
    embed.add_field(name = 'imperio (everyone.)',value ='Use it like ``spell imperio <message here>`` to make bot say message.',inline = False)
    embed.add_field(name = 'bans (Only those who are powerful enough)',value ='use it like ``spell bans``',inline = False)
    await client.send_message(author,embed=embed)
      
@client.command(pass_context = True)
@commands.has_permissions(send_messages=True)
async def imperio(ctx, *, msg = None):
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
async def avadakedavra(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members:
        await client.ban(member)
        embed=discord.Embed(title="**{1}** used Avada Kedavra on **{0}**!", description="The ancient ones have banned **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0x000000)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x000000)
        await client.say(embed=embed)   	 		 		  
     
@client.command(pass_context = True)
async def sectumsempra(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members:
        await client.kick(member)
        embed=discord.Embed(title="User booted!", description="The ancient ones have Kicked **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0x000000)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x000000)
        await client.say(embed=embed)
        
@client.command(pass_context = True)
async def invite(ctx):
     if ctx.message.author.id == "471988330335174667":
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
    join.add_field(name = '__Text/Voice Channels__', value = str(channels));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);
 
       
@client.command(pass_context = True)
async def crucio(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="The ancient ones have Muted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
          
@client.command(pass_context = True)
async def uncrucio(ctx, member: discord.Member):
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
async def setuup(ctx):
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
@commands.has_permissions(administrator=True)
async def setup(ctx):
        if ctx.message.author.id == "471988330335174667":
           author = ctx.message.author
           server = ctx.message.server
           mod_perms = discord.Permissions(manage_messages=True, kick_members=True, manage_nicknames =True,mute_members=True)
           admin_perms = discord.Permissions(ADMINISTRATOR=True)

           await client.create_role(author.server, name="Owner", permissions=admin_perms)
           await client.create_role(author.server, name="Admin", permissions=admin_perms)
           await client.create_role(author.server, name="Senior Moderator", permissions=mod_perms)
           await client.create_role(author.server, name="Good mod")
           await client.create_role(author.server, name="Moderator", permissions=mod_perms)
           await client.create_role(author.server, name="Muted")
    
           await client.create_role(author.server, name="Friend of Owner")
           await client.create_role(author.server, name="Verified")
           everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
           everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
           user_perms = discord.PermissionOverwrite(read_messages=True)
           user = discord.ChannelPermissions(target=server.default_role, overwrite=user_perms)
           private_perms = discord.PermissionOverwrite(read_messages=False)
           private = discord.ChannelPermissions(target=server.default_role, overwrite=private_perms)    
           await client.create_channel(server, '🎉welcome🎉',everyone)
           await client.create_channel(server, '🎯rules🎯',everyone)
           await client.create_channel(server, '🎥featured-content🎥',everyone)
           await client.create_channel(server, '📢announcements📢',everyone)
           await client.create_channel(server, '📢vote_polls📢',everyone)
           await client.create_channel(server, 'private_chat',private)
           await client.create_channel(server, '🎮general_chat🎮',user)
           await client.create_channel(server, '🎮general_media🎮',user)
           await client.create_channel(server, '👍bots_zone👍',user)
           await client.create_channel(server, '🎥youtube_links🎥',user)
           await client.create_channel(server, '🎥giveaway_links🎥',user)
           await client.create_channel(server, '🎥other_links🎥',user)
           await client.create_channel(server, '🔥Music Zone🔥', type=discord.ChannelType.voice)
           await client.create_channel(server, '🔥music_command🔥s',user)
           await client.create_channel(server, '🔥Chill Zone🔥', type=discord.ChannelType.voice)
        else:
           await client.say("Sorry, only Voldemort can wield this command!")
 
                                                                                                    
client.run(os.getenv('Token'))
