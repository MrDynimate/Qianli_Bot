from nonebot import on_command, CommandSession

@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    city = session.current_arg_text.strip()
    if not city:
        city = (await session.aget(prompt='你想查询哪个城市的天气捏，小主？')).strip()
        while not city:
            city = (await session.aget(prompt='抱歉，小主，要查询的城市信息不能为空哦~ 请再输入一次！')).strip()

    weather_report = await get_weather_of_city(city)

    await session.send(weather_report)
async def get_weather_of_city(city:str) -> str:
    return f'{city}的天气是……'