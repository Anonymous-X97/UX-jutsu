from userge import userge

async def u_n():
    u = await userge.get_me()
    me = f"{name_}"

    def name_():
        user = " ".join([u.first_name, u.last_name or ""])
        return user
