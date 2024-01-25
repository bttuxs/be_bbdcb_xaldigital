import requests
import json
from ..schema.AnswerSchema import Answers, AnswersStatus, Answer, AnswersFirstLast


def getAnswers() -> Answers:
    url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
    response = requests.get(url)
    return Answers(**json.loads(response.text))


def answerState():
    ListAnswers: Answers = getAnswers()
    unanswered = 0
    answered = 0

    for answer in ListAnswers.items:
        if answer.is_answered:
            answered += 1
        else:
            unanswered += 1
    status = AnswersStatus(answered=answered, unanswered=unanswered)
    print(status)
    return status


def answerBetter():
    ListAnswers: Answers = getAnswers()
    answerIndex = 0
    answerResult: Answer

    for answer in ListAnswers.items:
        if answer.answer_count > answerIndex:
            answerIndex = answer.answer_count
            answerResult = answer

    print(answerResult)
    return answerResult


def answerViewLess():
    ListAnswers: Answers = getAnswers()
    newList = sorted(ListAnswers.items, key=lambda x: x.view_count)
    answerResult: Answer = newList[0]
    print(answerResult)
    return answerResult


def answerFirstAndLast():
    ListAnswers: Answers = getAnswers()
    newList = sorted(ListAnswers.items, key=lambda x: x.creation_date)
    result = AnswersFirstLast(old=newList[0], new=newList[-1])
    print(result)
    return result
