from ..models import users

async def create_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    user_id = await database.execute(query)
    return {"id": user_id, "name": name, "email": email}