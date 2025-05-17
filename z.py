from .. import loader, utils


@loader.tds
class z(loader.Module):
    """z"""

    strings = {"name": "Z", "z": "Z"}
    strings_ru = {"z": "Z"}

    @loader.command(
        ru_doc="zov",
    )
    async def h(self, message):
        """z"""
        await utils.answer(message, self.strings("ZzZz...."))