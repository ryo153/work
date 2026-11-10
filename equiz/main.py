
import streamlit as st

from questions import questions
from game import (
    start_game,
    submit_answer,
    next_question,
    is_finished
)
from display import (
    show_title,
    show_start_screen,
    show_question,
    show_feedback,
    show_result
)


st.set_page_config(
    page_title="英単語4択クイズ",
    page_icon="📚",
    layout="centered"
)

# 初期化
if "started" not in st.session_state:
    st.session_state.started = False

show_title()

# ゲーム開始前
if not st.session_state.started:

    if show_start_screen():
        start_game(st.session_state, questions)
        st.session_state.started = True
        st.rerun()

# ゲーム中
else:

    if not is_finished(st.session_state):

        index = st.session_state.index
        question = st.session_state.questions[index]

        selected = show_question(
            question,
            index,
            len(st.session_state.questions),
            st.session_state.answered
        )

        # 回答前
        if not st.session_state.answered:

            if st.button("回答する", use_container_width=True):
                submit_answer(st.session_state, selected)
                st.rerun()

        # 回答後
        else:

            show_feedback(question, selected)

            if st.button("次の問題へ", use_container_width=True):
                next_question(st.session_state)
                st.rerun()

    # 結果画面
    else:

        if show_result(
            st.session_state.score,
            len(st.session_state.questions)
        ):
            st.session_state.started = False
            start_game(st.session_state, questions)
            st.session_state.started = False
            st.rerun()
