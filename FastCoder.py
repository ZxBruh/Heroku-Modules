#  _ _  _             _       _           
# |  /  /|  \/  ||  \/  |            | |     | |          
#   / /  / / | .  . || .  . |  _    _| |_   _| | _  _ 
#  / /  / /  | |\/| || |\/| | / _ \ / _` | | | | | |/ _ \/ __|
# / /_ / / | |  |  |  |  (_) | (_| | | |_| | |  /\__ \
# /__/_\_|  |_/\_|  |_/ \_/ \,_|_|\,_|_|\_||_/
#                                                             
# meta developer: @zxbruh, @zxmodules

import io
from .. import loader, utils

@loader.tds
class FastCoderMod(loader.Module):
    """Модуль который пишет код в файл под выборочным названием и форматом."""

    strings = {"name": "FastCoder"}

    async def кодcmd(self, message):
        """Пример: .код <название.формат> <код>"""
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("<b>Формат: .код <название.формат> <код></b>")
            return

        split_args = args.split(maxsplit=1)
        if len(split_args) < 2:
            await message.edit("<b>Недостаточно данных! Введите имя файла и текст кода.</b>")
            return

        full_filename, code_content = split_args

        file = io.BytesIO(code_content.encode('utf-8'))
        file.name = full_filename
        file.seek(0)

        await message.client.send_file(
            message.peer_id, 
            file, 
            caption=f"<b>Файл:</b> <code>{full_filename}</code>"
        )
        await message.delete()