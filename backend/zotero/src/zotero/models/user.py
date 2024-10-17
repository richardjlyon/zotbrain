from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    """
    Models the API response for a user
    """

    key: str
    user_id: int = Field(alias="userID")
    username: str
    displayname: str = Field(alias="displayName")
