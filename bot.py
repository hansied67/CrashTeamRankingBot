import discord
import os
from tracks import Track, TRACKS, ENGINES
from discord.ext import commands
from discord.ext.commands import bot_has_permissions, CommandNotFound, UserInputError, CommandInvokeError

import re

client = commands.Bot(command_prefix='.')

@client.command()
async def rename(ctx, name):
    await client.user.edit(username=name)

def get_track_name(track):
    args = track.split()
    print(args)
    track_name = args[0]
    if track_name not in [x for v in TRACKS.values() for x in v]:
        track_name = args[0] + args[1]
        if track_name not in [x for v in TRACKS.values() for x in v]:
            track_name = args[0] + args[1] + args[2]
            if track_name not in [x for v in TRACKS.values() for x in v]:
                raise CommandInvokeError(track)
    return track_name

def get_engine_type(kart_style):
    if kart_style in ENGINES["Speed"]: return 1
    elif kart_style in ENGINES["Accel"]: return 2
    elif kart_style in ENGINES["Turn"]: return 3
    elif kart_style in ENGINES["Drift"]: return 4
    elif kart_style in ENGINES["Balanced"]: return 5
    else: return 0


@client.event
async def on_ready():
    print('Bot is Ready')

client.remove_command('help')
@client.command(aliases=['help', 'HELP', 'Help'])
async def _help(ctx):
    await ctx.send("Commands:\n\n.wr [track] [class]\n.top10 [track] [class]")#\n.ourtimes [track]\n.addtime [track] [time] [link] (link optional)")


@client.command(aliases=['wr', 'worldrecord', 'WR', 'Wr', 'WorldRecord', 'Worldrecord', 'WORLDRECORD'])
async def _wr(ctx, *, track):
    track_name = get_track_name(track.lower())
    kart_style = track.split()[-1].lower()
    this_track = Track(track_name)

    await ctx.send(embed=this_track.wr(get_engine_type(kart_style)))

@client.command(aliases=['top10', 'Top10', 'TOP10', 't10', 'T10', 'top', '10'])
async def _top10(ctx, *, track):
    track_name = get_track_name(track.lower())
    kart_style = track.split()[-1].lower()
    this_track = Track(track_name)

    await ctx.send(embed=this_track.top10(get_engine_type(kart_style)))

@client.command(aliases=['ethan', 'Ethan', 'ETHAN'])
async def _ethan(ctx):
    await ctx.send(file=discord.File('ethan.png'))

'''@client.command(aliases=['ourtimes', 'Ourtimes', 'OurTimes', 'ourTimes', 'OURTIMES'])
async def _ourtimes(ctx, *, track):
    try:
        this_track = Track(track)
    except:
        raise CommandInvokeError(track)
    await ctx.send(embed = this_track.ourtimes(ctx))

@client.command(aliases=['addtime', 'Addtime', 'AddTime', 'addTime', 'ADDTIME'])
async def _addtime(ctx, *, track):
    if ctx.guild is None:
        await ctx.send('Cannot perform this action in DMs, only in servers.')
        return
    track_name = get_track_name(track)
    this_track = Track(track_name)

    args = track[re.search(track_name, track).end()+1:] + ' ' + ctx.message.author.name
    try:
        os.mkdir('./' + ctx.guild.name)
    except OSError:
        pass
    else:
        print("Succesfully created ./" + ctx.guild.name)

    with open('./' + ctx.guild.name + '/' + this_track.name + '.txt', 'a+') as f:
        f.write(args + '\n')

    await ctx.send('Time successfully added')

@client.command(aliases=['deltimes', 'Deltimes', 'DelTimes', 'delTimes', 'DELTIMES'])
@bot_has_permissions(manage_roles=True)
async def _deltimes(ctx, *, track):
    try:
        try:
            this_track = Track(track.split()[0] + ' ' + track.split()[1])
            try:
                name = track.split()[2]
                if not ctx.message.author.server_permissions.administrator:
                    raise Exception
            except:
                await ctx.send("Must be admin to delete others' times. Deleting yours instead:")
                name = ctx.message.author.name
            with open('./ourtimes/' + this_track.name + '.txt', 'r') as f:
                lines = f.readlines()
            count = 0
            with open('./ourtimes/' + this_track.name + '.txt', 'w') as f:
                for line in lines:
                    if line.strip('\n').split()[-1] != name:
                        f.write(line)
                    else:
                        count += 1
        except:
            this_track = Track(track.split()[0])
            #print(ctx.message.author.server_permissions)
            try:
                name = track.split()[1]
                if not ctx.message.author.server_permissions.administrator:
                    raise Exception
            except:
                await ctx.send("Must be admin to delete others' times. Deleting yours instead:")
                name = ctx.message.author.name
            with open('./ourtimes/' + this_track.name + '.txt', 'r') as f:
                lines = f.readlines()
            count = 0
            with open('./ourtimes/' + this_track.name + '.txt', 'w') as f:
                for line in lines:
                    if line.strip('\n').split()[-1] != name:
                        f.write(line)
                    else:
                        count += 1
    except:
        raise CommandInvokeError(track)

    await ctx.send('Times deleted: ' + str(count))

@client.command(aliases=['exit', 'close'])
async def _exit(ctx):
    await client.logout()'''

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        pass    # don't want to clutter chats
        # await ctx.send(str(ctx.invoked_with) + ": Command doesn't exist (try .help)")
    elif isinstance(error, UserInputError):
        await ctx.send(str(ctx.invoked_with) + ": Not enough parameters (try .help)")
    elif isinstance(error, CommandInvokeError):
        await ctx.send("Track does not exist")



if __name__ == '__main__':
    client.run('NjQwODIzODU2OTY5NTQ3Nzgz.Xb_b0Q.-Ns0Fuh_vorYPW00dTMtUOXzMO0')
