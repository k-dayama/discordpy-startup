from discord.ext import commands
import os
import traceback
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
app = Flask(__name__)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@app.route('/post', method=['POST'])
def post_json():
    
    return request.form["comment"]
@app.route('/')
def index():
    return "Hello Flask!"
def get_json():
bot.run(token)

