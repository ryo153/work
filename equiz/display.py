import streamlit as st
def show_title():
    st.title("English quiz")
    st.write("英単語の意味を四択から選んでください")
def show_start_screen():
    st.write("全5問の英単語クイズです")
    return st.button("ゲーム開始", use_container_width=True)
def show_question(question,index,total,answered):
    st.progress((index+1)/total)
    st.caption(f"Question{index+1}/{total}")
    st.subheader(question["word"])
    selected=st.radio(
        "正しい意味を選択してください",
        question["choices"],
        key=f"choices_{index}",
        disabled=answered
    )
    return selected
def show_feedback(question,selected):
    if selected==question["answer"]:
        st.success("正解です")
    else:
         st.error("不正解です")
    st.write(f"正解:{question['answer']}")

def show_result(score,total):
    st.title("結果発表")
    st.metric("正解数", f"{score} / {total}")

    accuracy = score / total * 100

    st.metric("正答率", f"{accuracy:.1f}%")

    if accuracy == 100:
        st.success("全問正解！素晴らしい！")
    elif accuracy >= 60:
        st.info("よくできました！")
    else:
        st.warning("もう一度挑戦してみましょう！")

    return st.button(
        "もう一度プレイ",
        use_container_width=True
    )
