import asyncio
import aiomysql
loop = asyncio.get_event_loop()


async def mysql_start():
    global base, cur
    base = await aiomysql.connect(host='localhost', user='root', password='tU^3UUmtTty1', db='GIBuilds_bot', loop=loop)
    if base:
        print('Data base connected OK')
    cur = await base.cursor()
    #await cur.execute('CREATE TABLE IF NOT EXISTS `gibuilds_bot`.`characters` (`img` TEXT(1000), `name` TEXT(25), `description` TEXT(1000), PRIMARY KEY (`name`(25)))')
    #await cur.execute('CREATE TABLE IF NOT EXISTS `gibuilds_bot`.`menu`(`img` TEXT(1000), `name` TEXT(25), `description` TEXT(1000), PRIMARY KEY(`name`(25)))')
    #await cur.execute('CREATE TABLE IF NOT EXISTS `gibuilds_bot`.`properties`(`img` TEXT(1000), `name` TEXT(25), `description` TEXT(1000), PRIMARY KEY(`name`(25)))')
    #await cur.execute('CREATE TABLE IF NOT EXISTS `gibuilds_bot`.`teams`(`img` TEXT(1000), `name` TEXT(25), `description` TEXT(1000), PRIMARY KEY(`name`(25)))')
    #await cur.execute('CREATE TABLE IF NOT EXISTS `gibuilds_bot`.`weapons`(`img` TEXT(1000), `name` TEXT(25), `description` TEXT(1000), PRIMARY KEY(`name`(25)))')
    #await cur.execute('CREATE TABLE IF NOT EXISTS `gibuilds_bot`.`artifacts`(`img` TEXT(1000), `name` TEXT(25), `description` TEXT(1000), PRIMARY KEY(`name`(25)))')
    #await base.commit()


async def sql_add_command(state, info):
    if info == 'characters':
        async with state.proxy() as data:
            sql = "INSERT INTO characters (img,name,description) VALUES (%s, %s, %s)"
            await cur.execute(sql, tuple(data.values()))
    elif info == 'menu':
        async with state.proxy() as data:
            sql = "INSERT INTO menu (img,name,description) VALUES (%s, %s, %s)"
            await cur.execute(sql, tuple(data.values()))
    elif info == 'properties':
        async with state.proxy() as data:
            sql = "INSERT INTO properties (img,name,description) VALUES (%s, %s, %s)"
            await cur.execute(sql, tuple(data.values()))
    elif info == 'teams':
        async with state.proxy() as data:
            sql = "INSERT INTO teams (img,name,description) VALUES (%s, %s, %s)"
            await cur.execute(sql, tuple(data.values()))
    elif info == 'weapons':
        async with state.proxy() as data:
            sql = "INSERT INTO weapons (img,name,description) VALUES (%s, %s, %s)"
            await cur.execute(sql, tuple(data.values()))
    elif info == 'artifacts':
        async with state.proxy() as data:
            sql = "INSERT INTO artifacts (img,name,description) VALUES (%s, %s, %s)"
            await cur.execute(sql, tuple(data.values()))
    await base.commit()


async def sql_readMenu(data):
    sql = "SELECT * FROM menu WHERE name = %s"
    await cur.execute(sql, data)
    res = await cur.fetchall()
    await base.commit()
    return res


async def sql_readCh(data):
    sql = "SELECT * FROM characters WHERE name = %s"
    await cur.execute(sql, data)
    res = await cur.fetchall()
    await base.commit()
    return res


async def sql_readProp(data):
    sql = "SELECT * FROM properties WHERE name = %s"
    await cur.execute(sql, data)
    res = await cur.fetchall()
    await base.commit()
    return res


async def sql_readArt(data):
    sql = "SELECT * FROM artifacts WHERE name = %s"
    await cur.execute(sql, data)
    res = await cur.fetchall()
    await base.commit()
    return res


async def sql_readTeams(data):
    sql = "SELECT * FROM teams WHERE name = %s"
    await cur.execute(sql, data)
    res = await cur.fetchall()
    await base.commit()
    return res


async def sql_readWeap(data):
    sql = "SELECT * FROM weapons WHERE name = %s"
    await cur.execute(sql, data)
    res = await cur.fetchall()
    await base.commit()
    return res


async def sql_read2(data):
    if data == 'characters':
        sql = "SELECT * FROM characters"
        await cur.execute(sql)
        return cur.fetchall()
    elif data == 'menu':
        sql = "SELECT * FROM menu"
        await cur.execute(sql)
        return cur.fetchall()
    elif data == 'properties':
        sql = "SELECT * FROM properties"
        await cur.execute(sql)
        return cur.fetchall()
    elif data == 'teams':
        sql = "SELECT * FROM teams"
        await cur.execute(sql)
        return cur.fetchall()
    elif data == 'weapons':
        sql = "SELECT * FROM weapons"
        await cur.execute(sql)
        return cur.fetchall()
    elif data == 'artifacts':
        sql = "SELECT * FROM artifacts"
        await cur.execute(sql)
        return cur.fetchall()
    await base.commit()


async def sql_delete(data, info):
    if data == 'characters':
        sql = "DELETE FROM characters WHERE name = %s"
        await cur.execute(sql, info)
    elif data == 'menu':
        sql = "DELETE FROM menu WHERE name = %s"
        await cur.execute(sql, info)
    elif data == 'properties':
        sql = "DELETE FROM properties WHERE name = %s"
        await cur.execute(sql, info)
    elif data == 'teams':
        sql = "DELETE FROM teams WHERE name = %s"
        await cur.execute(sql, info)
    elif data == 'weapons':
        sql = "DELETE FROM weapons WHERE name = %s"
        await cur.execute(sql, info)
    elif data == 'artifacts':
        sql = "DELETE FROM artifacts WHERE name = %s"
        await cur.execute(sql, info)
    await base.commit()
