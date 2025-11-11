# roll/roll.py
import random
import re
from discord.ext import commands

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commande roll avec alias "r"
    @commands.command(name="roll", aliases=["r"])
    async def roll(self, ctx, dice: str):
        match = re.fullmatch(r"(\d+)d(\d+)", dice.lower())
        if not match:
            await ctx.send("⚠️ Format invalide. Utilise `!roll XdY`, ex: `!roll 3d6`, ou `!r 3d6`")
            return

        nb_dice, nb_faces = map(int, match.groups())

        if nb_dice <= 0 or nb_faces <= 0:
            await ctx.send("⚠️ Le nombre de dés et de faces doit être positif.")
            return

        if nb_dice > 50:
            await ctx.send("⚠️ Trop de dés à lancer à la fois (max 50).")
            return

        results = [random.randint(1, nb_faces) for _ in range(nb_dice)]
        total = sum(results)

        if nb_dice == 1:
            await ctx.send(f"🎲 Résultat de {dice} : **{total}**")
        else:
            await ctx.send(f"🎲 Résultats de {dice} : {results} → **Total = {total}**")

# Fonction de setup pour le bot
def setup(bot):
    bot.add_cog(Roll(bot))
