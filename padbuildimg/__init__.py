from .padbuildimg import PadBuildImage

__red_end_user_data_statement__ = "No personal data is stored."


async def setup(bot):
    await bot.add_cog(PadBuildImage(bot))
