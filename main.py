import streamlit as st

st.set_page_config(
    page_title="🌌 MBTI 전설 포켓몬 매칭",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}
.title {
    text-align: center;
    color: gold;
    font-size: 3rem;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: white;
    font-size: 1.2rem;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🌌 MBTI 전설 포켓몬 매칭 🌌</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">당신과 가장 잘 어울리는 전설의 포켓몬은?</p>',
    unsafe_allow_html=True
)

pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://play.pokemonshowdown.com/sprites/ani/mewtwo.gif",
        "mbti": "전략적이고 독립적인 천재형",
        "pokemon": "강력한 초능력과 뛰어난 지능을 가진 전설의 포켓몬.",
        "match": "냉철한 분석력과 목표 지향적인 성격이 매우 비슷합니다."
    },
    "INTP": {
        "name": "디아루가",
        "image": "https://play.pokemonshowdown.com/sprites/ani/dialga.gif",
        "mbti": "호기심 많고 논리적인 탐구자",
        "pokemon": "시간을 관장하는 신비로운 전설의 포켓몬.",
        "match": "복잡한 개념을 탐구하는 지적 성향과 잘 어울립니다."
    },
    "ENTJ": {
        "name": "레쿠쟈",
        "image": "https://play.pokemonshowdown.com/sprites/ani/rayquaza.gif",
        "mbti": "카리스마 넘치는 지휘관",
        "pokemon": "하늘을 지배하는 강력한 전설의 포켓몬.",
        "match": "강한 리더십과 압도적인 존재감을 상징합니다."
    },
    "ENTP": {
        "name": "후파",
        "image": "https://play.pokemonshowdown.com/sprites/ani/hoopa.gif",
        "mbti": "창의적이고 아이디어가 넘치는 혁신가",
        "pokemon": "차원을 넘나드는 신비한 힘을 가진 포켓몬.",
        "match": "기발한 발상과 자유로운 사고가 닮았습니다."
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://play.pokemonshowdown.com/sprites/ani/lugia.gif",
        "mbti": "통찰력 있는 이상주의자",
        "pokemon": "바다를 수호하는 위엄 있는 전설의 포켓몬.",
        "match": "깊은 이해력과 평화를 추구하는 성향이 비슷합니다."
    },
    "INFP": {
        "name": "세레비",
        "image": "https://play.pokemonshowdown.com/sprites/ani/celebi.gif",
        "mbti": "감성적이고 상상력이 풍부한 몽상가",
        "pokemon": "숲과 시간을 지키는 귀여운 전설의 포켓몬.",
        "match": "순수한 마음과 따뜻한 공감 능력을 상징합니다."
    },
    "ENFJ": {
        "name": "자시안",
        "image": "https://play.pokemonshowdown.com/sprites/ani/zacian.gif",
        "mbti": "타인을 이끄는 따뜻한 리더",
        "pokemon": "정의와 용기를 상징하는 전설의 포켓몬.",
        "match": "사람들을 돕고 이끄는 성향과 잘 맞습니다."
    },
    "ENFP": {
        "name": "지라치",
        "image": "https://play.pokemonshowdown.com/sprites/ani/jirachi.gif",
        "mbti": "열정적이고 밝은 자유로운 영혼",
        "pokemon": "소원을 이루어 준다고 전해지는 전설의 포켓몬.",
        "match": "희망과 긍정 에너지가 넘치는 점이 닮았습니다."
    },
    "ISTJ": {
        "name": "레지기가스",
        "image": "https://play.pokemonshowdown.com/sprites/ani/regigigas.gif",
        "mbti": "책임감 강한 현실주의자",
        "pokemon": "고대의 거대한 전설 포켓몬.",
        "match": "묵묵하게 자신의 역할을 수행하는 모습이 비슷합니다."
    },
    "ISFJ": {
        "name": "크레세리아",
        "image": "https://play.pokemonshowdown.com/sprites/ani/cresselia.gif",
        "mbti": "배려심 깊은 수호자",
        "pokemon": "좋은 꿈을 가져다주는 전설의 포켓몬.",
        "match": "타인을 돌보고 보호하려는 마음이 닮았습니다."
    },
    "ESTJ": {
        "name": "그란돈",
        "image": "https://play.pokemonshowdown.com/sprites/ani/groudon.gif",
        "mbti": "체계적이고 추진력 있는 관리자",
        "pokemon": "대지를 창조한 전설의 포켓몬.",
        "match": "강한 추진력과 결단력을 상징합니다."
    },
    "ESFJ": {
        "name": "자마젠타",
        "image": "https://play.pokemonshowdown.com/sprites/ani/zamazenta.gif",
        "mbti": "사교적이고 친절한 협력가",
        "pokemon": "동료를 보호하는 방패의 전설 포켓몬.",
        "match": "주변 사람들을 챙기는 성향과 잘 어울립니다."
    },
    "ISTP": {
        "name": "제라오라",
        "image": "https://play.pokemonshowdown.com/sprites/ani/zeraora.gif",
        "mbti": "독립적이고 문제 해결 능력이 뛰어난 장인",
        "pokemon": "번개처럼 빠른 움직임을 가진 환상의 포켓몬.",
        "match": "실전 능력과 침착함이 비슷합니다."
    },
    "ISFP": {
        "name": "쉐이미",
        "image": "https://play.pokemonshowdown.com/sprites/ani/shaymin.gif",
        "mbti": "예술적이고 온화한 모험가",
        "pokemon": "자연과 감사의 마음을 상징하는 포켓몬.",
        "match": "따뜻한 감성과 자유로운 영혼이 닮았습니다."
    },
    "ESTP": {
        "name": "코라이돈",
        "image": "https://play.pokemonshowdown.com/sprites/ani/koraidon.gif",
        "mbti": "대담하고 행동력이 뛰어난 모험가",
        "pokemon": "강인한 힘과 야성을 가진 전설의 포켓몬.",
        "match": "도전을 즐기고 즉시 행동하는 모습이 비슷합니다."
    },
    "ESFP": {
        "name": "케르디오",
        "image": "https://play.pokemonshowdown.com/sprites/ani/keldeo.gif",
        "mbti": "밝고 즐거움을 전하는 엔터테이너",
        "pokemon": "용감하고 활기찬 환상의 포켓몬.",
        "match": "긍정적인 에너지와 활발함이 닮았습니다."
    }
}

st.divider()

mbti = st.text_input(
    "🔍 MBTI를 입력하세요 (예: INFP)"
).upper().strip()

if st.button("✨ 나의 전설 포켓몬 찾기 ✨"):

    if mbti in pokemon_data:
        data = pokemon_data[mbti]

        st.balloons()

        st.success("🎉 매칭 완료!")

        st.image(data["image"], width=250)

        st.markdown(f"""
### 🌟 당신의 전설 포켓몬: **{data["name"]}**

#### 🧠 MBTI 성향
{data["mbti"]}

#### 📖 포켓몬 소개
{data["pokemon"]}

#### ✨ 잘 어울리는 이유
{data["match"]}
""")

    else:
        st.error("⚠️ 올바른 MBTI를 입력해주세요. (예: INTJ, ENFP)")

st.divider()
st.caption("🌌 MBTI와 포켓몬의 매칭은 재미를 위한 콘텐츠입니다.")
