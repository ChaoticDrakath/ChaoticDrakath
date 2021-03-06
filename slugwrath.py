import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import platform
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = Bot(description="I am The local Guard in Mystics", command_prefix="m!", pm_help = True)
client.remove_command('help')

players = {}


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name="with Ninjas", type=1))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name="with "+str(len(set(client.get_all_members())))+" Ninjas!", type=1))
        await asyncio.sleep(5)
	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Created By Mushronin')
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    await client.process_commands(message)

def is_owner(ctx):
    return ctx.message.author.id == "471988330335174667"

def is_immortal(ctx):
    return ctx.message.author.id == "471988330335174667"

@client.command(pass_context = True)
@commands.check(is_owner)
async def restart():
    await client.logout()



@client.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    embed = discord.Embed(color = 0x5c0587)
    embed.set_author(name='Welcome message')
    embed.add_field(name = 'Welcome to Our Server!',value ='**Please be active and read rules. ',inline = False)
    embed.set_image(url = 'https://goo.gl/images/1T8Ce8')
    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='ets', name='general')
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules.', color = 0x5c0587)
    embed.add_field(name='Thanks for joining!', value='**Please be active here.**', inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://goo.gl/images/1T8Ce8')
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)
	
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Mushronin')
    await client.add_roles(member, role)
	
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    """Returns a user's avatar url."""
    if user is None:
        await client.say(ctx.message.author.avatar_url)                   
    else:
        await client.say(user.avatar_url)
	
	
async def on_message(self, message):
    if message.content.startswith('@Dark Shroom#5272'):
        await self.send_message(message.channel, 'My prefix is !m')
	

@client.command(pass_context=True, aliases=['em', 'e'])
async def support(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='support')
    color = 0x5c0587
    if not msg:
        await client.say("Please specify a message to ask!")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def Ninjainfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = 0x5c0587)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
    pass

@client.command(pass_context=True)
async def SenseiInfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- ImmortalBOT", color=0x00ff00)
    embed.set_footer(text="Copyright")
    embed.set_author(name=" Bot Owner Name -Mushronin #6460 -ID:471988330335174667")
    await client.say(embed=embed)
    
    
@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def givenick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say("Poll can't have 1 option!")
            return
        if len(options) > 9:
            await client.say('You cany make poll longer than 9 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), color = 0x5c0587)
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
        
@client.command(pass_context = True)
async def ip02(ctx, *, msg = None):
    if not msg: await client.say("Please specify a string")
    else:
        await client.say('http://lmgtfy.com/?q=' + msg)
    return

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0x5c0587)
    embed.set_author(name='Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'Dark Shroom commanderhelp ',value ='Explains all the commands which are only usable by Those who has Commander role or above.',inline = False)
    embed.add_field(name = 'Dark Shroom generalhelp ',value ='Explains all the commands which are usable by everyone.',inline = False)
    embed.add_field(name = 'Dark Shroom legendhelp ',value ='Explains all the commands which are usable by Mushronins legend! (TBD)',inline = False)
    await client.send_message(author,embed=embed)
    await client.say('Check ur DMs!')
	
@client.command(pass_context = True)
@commands.has_role("Mushronin's Commander")
async def commanderhelp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0x5c0587)
    embed.set_author(name='Officer Commands Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'say(Admin permission required) ',value ='Use it like ``Mush say <text>``',inline = False)
    embed.add_field(name = 'embed(Admin permission required) ',value ='Use it like ``Mush embed <text>``',inline = False)
    embed.add_field(name = 'dm((Admin permission required) ',value ='Use it like ``Mush dm @user <text>`` to dm anyone',inline = False)
    embed.add_field(name = 'membercount(Kick members Permission Required) ',value ='Use it like ``Mush membercount`` to get membercount',inline = False)
    embed.add_field(name = 'role(Manage Roles Permission Required)',value ='Use it like ``Mush role @user <rolename>``.',inline = False)
    embed.add_field(name = 'givenick(Manage nicknames permission required)',value ='Use it like ``Mush givenick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
    embed.add_field(name = 'serverinfo(Kick members Permission Required) ',value ='Use it like ``Mush serverinfo`` to get server info',inline = False)
    embed.add_field(name = 'userinfo(Kick members Permission Required) ',value ='Use it like ``Mush userinfo @user`` to get some basic info of tagged user',inline = False)
    embed.add_field(name = 'kick(Kick members Permission Required)',value ='Use it like ``Mush kick @user`` to kick any user',inline = False)
    embed.add_field(name = 'roles(Manage roles Permission Required) ',value ='Use it to check roles present in server',inline = False)
    embed.add_field(name = 'clear(Manage Messages Permission Required)',value ='Use it like ``Mush clear <number>`` to clear any message',inline = False)
    embed.add_field(name = 'mute(Mute members Permission Required)',value ='Use it like ``Mush mute @user <time>`` to mute any user',inline = False)
    embed.add_field(name = 'unmute(Mute members Permission Required) ',value ='Use it like ``Mush unmute @user`` to unmute anyone',inline = False)
    embed.add_field(name = 'ban(Ban members Permission Required) ',value ='Use it like ``Mush ban @user`` to ban any user',inline = False)
    embed.add_field(name = 'rules(Kick members Permission Required)',value ='Use it like ``Mush rules @user <violation type>`` to warn user',inline = False)
    embed.add_field(name = 'warn(Kick members Permission Required)',value ='Use it like ``Mush warn @user <violation type>`` to warn any user',inline = False)    
    await client.send_message(author,embed=embed)
    await client.say('Check ur DMs!')

@client.command(pass_context = True)
async def generalhelp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0x5c0587)
    embed.add_field(name = 'poll ',value ='Use it like ``Mush poll "Question" "Option1" "Option2" ..... "Option9"``.',inline = False)
    embed.add_field(name = 'guess ',value ='To play guess game use ``Mush guess <number> and number should be between 1-10``',inline = False)
    embed.add_field(name = 'ownerinfo ',value ='To get basic information about owner.',inline = False)
    embed.add_field(name = 'avatar @user ',value ='Shows avatar',inline = False) 	
    await client.send_message(author,embed=embed)
    await client.say('Check ur DMs!')
	
	
@client.command(pass_context = True)
async def invite(ctx):
     if ctx.message.author.id == "471988330335174667":
        embed=discord.Embed(title="You can invite me using this link!", description="https://discordapp.com/api/oauth2/authorize?client_id=474575162424033280&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D474575162424033280%26permissions%3D8%26redirect_uri%3Dhttps%253A%252F%252Fdiscordapp.com%252Fapi%252Foauth2%252Fauthorize%253Fclient_id%253D&scope=bot", color=0x000000)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0x5c0587)
        await client.say(embed=embed
 
 
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)     
async def Promote(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("You haven't specified a role! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("{} role has been added to {}.".format(role, user))

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)      



    	 		


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def Expell(ctx,user:discord.Member):

    if ctx.message.author.id == "471988330335174667":
        await client.kick(user)
        await client.say(user.name+' was kicked. Good bye '+user.name+'!')
        await client.delete_message(ctx.message)
        return

    if user.server_permissions.kick_members:
        await client.say('**He is mod/admin and i am unable to kick him/her**')
        return

    try:
        await client.kick(user)
        await client.say(user.name+' was kicked. Good bye '+user.name+'!')
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        await client.say('Permission denied.')
        return



@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unExpell(ctx):
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
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="The ancient ones have Muted **{0}** #information, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
          
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="The ancient ones have Unmuted **{0}** #information, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)

  
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a user who breaked any of these rules.")
    else: await client.say(msg + ", Looks like you breaked a rule, please read read rules and dont break any of them again or you'll get punished by me or by the server moderators")
    return

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

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
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = 0x5c0587);
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def welcome(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a user to welcome")
    else: await client.say('Welcome' + msg +  ', Please check <#441312601255837744>.')
    return

   

@client.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await client.say("Invalid number")
    else:
        await client.say('The correct answer is ' + str(arg))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '' + role.name + '' + ": " + '' + role.id + '' + "\n "
	await client.say(result)
    
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(send_messages=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "" % (membs, membs_on, users, users_on, bots, bots_on, created)

    color = 0x5c0587
    await client.send_message(ctx.message.channel, embed=em(color = color, description=em.description))
    await client.delete_message(ctx.message)
	
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    """
    Sending embeded messages with color (and maby later title, footer and fields)
    """
    argstr = " ".join(args)
    text = argstr
    color = 0x5c0587
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    await client.delete_message(ctx.message)


client.run(os.getenv('Token'))
