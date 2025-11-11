import discord
from discord.ext import commands
import random
import re

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------------------
# Événement quand le bot est prêt
# ---------------------------
@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

# ---------------------------
# Gestionnaire global des erreurs
# ---------------------------
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("⚠️ Commande inconnue. Essaie `!r 1d100` ou `!hello`")
    else:
        raise error

# ---------------------------
# Commande simple pour test
# ---------------------------
@bot.command()
async def hello(ctx):
    await ctx.send(f"Salut {ctx.author.mention} 👋")




bot.load_extension("roll.roll")
@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    print("📜 Commandes disponibles :", [cmd.name for cmd in bot.commands])










# Commande roll avec alias "r"
@bot.command(name="roll", aliases=["r"])
async def roll(ctx, dice: str):
    match = re.fullmatch(r"(\d+)d(\d+)", dice.lower())
    if not match:
        await ctx.send("⚠️ Format invalide. Utilise !r XdY, ex: !r 3d6")
        return

    nb_dice, nb_faces = map(int, match.groups())

    if nb_dice <= 0 or nb_faces <= 0:
        await ctx.send("⚠️ Le nombre de dés et de faces doit être positif.")
        return

    if nb_dice > 50:
        await ctx.send("⚠️ Trop de dés à lancer à la fois (max 50).")
        return

    # ---------------------------
    # Le reste doit être indenté ICI
    # ---------------------------
    results = [random.randint(1, nb_faces) for _ in range(nb_dice)]
    total = sum(results)

    # ✅ Initialisation de message avant tout
    message = ""

    # Message de base
    if nb_dice == 1:
        message = f"🎲 Résultat de {dice} : **{total}**"
    else:
        message = f"🎲 Résultats de {dice} : {results} → **Total = {total}**"

    # Gestion réussite / échec critique uniquement pour d100
    if nb_faces == 100:
        critiques = []
        for r in results:
            if r <= 5:
                critiques.append(f"{r} ✅ Réussite critique")
            elif r >= 95:
                critiques.append(f"{r} ❌ Échec critique")
        if critiques:
            message += "\n" + "\n".join(critiques)

    await ctx.send(message)







# ---------------------------
# Lancer le bot
# ---------------------------
try:
    print("🔄 Lancement du bot...")
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ Erreur au lancement : {e}")