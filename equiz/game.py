import random
def start_game(state,questions):
    state.questions=random.sample(
        questions,len(questions)
    )
    state.index=0
    state.score=0
    state.answered=False
def submit_answer(state,selected):
    if state.answered :
        return
    question=state.questions[state.index]
    if selected==question["answer"]:
        state.score+=1
    state.answered =True
def next_question(state):
    state.index+=1
    state.answered=False

def is_finished(state):
    return state.index>=len(state.questions)