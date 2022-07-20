get_messages = """
SELECT 
        u.username,
        dm.content,
        dm.timestamp
FROM
    public.discord_messages dm
LEFT JOIN
    public.discord_user u
    ON u.discord_user_id = dm.author_user_id
WHERE
    dm.timestamp >= '2022-04-20'
"""



# get_messages ="""SELECT *
#              FROM public.discord_messages
#           """


# #get messages
# #this gives you multiple rows for each guild a person is in, need to make those move into a single column
# get_messages ="""SELECT 
#                         DISTINCT dm.content,
#                         u.username,
#                         dr.role_name as guild,
#                         dc.name as channel_name,
#                         dm.timestamp
#                FROM public.discord_messages dm
#                LEFT JOIN public.discord_channels dc
#                   ON dc.discord_channel_id = dm.channel_id
#                LEFT JOIN public.discord_user u
#                   ON u.discord_user_id = dm.author_user_id
#                LEFT JOIN public.discord_roles dr
#                     ON dr.guild_id = dm.guild_id
#           """

# # get_messages ="""SELECT 
# #                         DISTINCT
# #                         u.username,
# #                         dm.content,
# #                         dm.timestamp
# #                FROM public.discord_messages dm
# #                LEFT JOIN public.discord_channels dc
# #                   ON dc.discord_channel_id = dm.channel_id and dc.name = '🌞__gm'
# #                LEFT JOIN public.discord_user u
# #                   ON u.discord_user_id = dm.author_user_id
# #                WHERE dm.timestamp >= '2022-05-20'
#           """