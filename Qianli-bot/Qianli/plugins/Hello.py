from nonebot import on_command, CommandSession

@on_command('Hello', aliases=(' ','在么','在嘛','在么?','在嘛?'))
async def Hello(session: CommandSession):
    await session.send('嗯，小主，我在捏~')
    await session.send('小主，我现在仅支持查询群等级的功能哦~查询群等级请随时叫我：“千里，查询群等级”')