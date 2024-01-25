from pydantic import BaseModel
from typing import List, Optional


class Owner(BaseModel):
    reputation: int
    user_id: int
    user_type: str
    profile_image: str
    display_name: str
    link: str


class Answer(BaseModel):
    tags: List[str]
    owner: Owner
    is_answered: bool
    view_count: int
    answer_count: int
    score: int
    last_activity_date: int
    creation_date: int
    question_id: int
    content_license: Optional[str] = None
    link: str
    title: str


class Answers(BaseModel):
    items: List[Answer]
    has_more: bool
    quota_max: int
    quota_remaining: int


class AnswersStatus(BaseModel):
    unanswered: int
    answered: int


class AnswersFirstLast(BaseModel):
    old: Answer
    new: Answer
