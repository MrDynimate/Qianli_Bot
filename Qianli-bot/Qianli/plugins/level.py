from nonebot import on_command, CommandSession
from nonebot import get_bot

bot = get_bot()

@on_command('Level', aliases=('查等级','查询群等级','查群等级','等级','群等级'))
async def Level(session: CommandSession):
    qqnum=str(session.ctx['user_id'])
    group_member_info = await bot.get_group_member_list(group_id=317420914)

    await session.send(str(group_member_info))