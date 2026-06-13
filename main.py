import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 매칭",
    page_icon="✨",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align:center;'>✨ MBTI 포켓몬 매칭 ✨</h1>
    <p style='text-align:center; font-size:20px;'>
    당신과 가장 잘 어울리는 포켓몬은 누구일까요? 🎮⚡
    </p>
    """,
    unsafe_allow_html=True
)

pokemon_data = {
    "INTJ": ("뮤츠", "🧠", "전략적이고 독립적인 천재형. 목표를 향해 묵묵히 나아갑니다."),
    "INTP": ("후딘", "🔮", "호기심이 많고 분석을 즐기는 아이디어 뱅크입니다."),
    "ENTJ": ("리자몽", "🔥", "강한 리더십과 추진력을 가진 카리스마형입니다."),
    "ENTP": ("팬텀", "👻", "창의적이고 재치 넘치는 도전자입니다."),
    "INFJ": ("루기아", "🌊", "깊은 통찰력과 따뜻한 마음을 가진 이상주의자입니다."),
    "INFP": ("이브이", "🌈", "상상력이 풍부하고 감성이 뛰어난 몽상가입니다."),
    "ENFJ": ("피카츄", "⚡", "주변 사람들에게 에너지를 주는 인기쟁이입니다."),
    "ENTP": ("팬텀", "👻", "창의적이고 장난기 많은 혁신가입니다."),
    "ENFP": ("토게키스", "🕊️", "밝고 긍정적이며 사람을 좋아합니다."),
    "ISTJ": ("거북왕", "💧", "책임감이 강하고 믿음직한 현실주의자입니다."),
    "ISFJ": ("해피너스", "💖", "배려심이 많고 헌신적인 수호자입니다."),
    "ESTJ": ("괴력몬", "💪", "조직력과 실행력이 뛰어난 리더입니다."),
    "ESFJ": ("푸크린", "🎵", "친절하고 사교적인 분위기 메이커입니다."),
    "ISTP": ("한카리아스", "🐉", "침착하고 문제 해결 능력이 뛰어납니다."),
    "ISFP": ("나인테일", "🦊", "예술적 감각과 따뜻한 감성을 가졌습니다."),
    "ESTP": ("인텔리레온", "🎯", "대담하고 모험을 즐기는 행동파입니다."),
    "ESFP": ("파이리", "🔥", "활발하고 즐거움을 추구하는 엔터테이너입니다.")
}

st.divider()

mbti = st.text_input(
    "🔍 MBTI를 입력하세요 (예: INFP)",
    max_chars=4
).upper()

if st.button("✨ 포켓몬 찾기! ✨"):

    if mbti in pokemon_data:
        pokemon, emoji, desc = pokemon_data[mbti]

        st.balloons()

        st.success("매칭 완료! 🎉")

        st.markdown(
            f"""
            ## {emoji} 당신의 포켓몬은 **{pokemon}**!

            ### 🌟 성향 분석
            {desc}

            ### 🎮 한마디
            **{pokemon}**처럼 당신만의 강점을 믿고 나아가 보세요!
            """
        )

    else:
        st.error("⚠️ 올바른 MBTI를 입력해주세요. (예: INTJ, ENFP)")
        
st.divider()

st.caption("💖 MBTI와 포켓몬을 재미로 매칭한 웹앱입니다.")
