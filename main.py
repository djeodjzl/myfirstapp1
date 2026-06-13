import streamlit as st

st.set_page_config(
    page_title="🌌 MBTI 전설 포켓몬 매칭",
    page_icon="✨",
    layout="centered"
)

# -------------------------
# 기본 CSS
# -------------------------

st.markdown("""
<style>

.stApp {
    transition: all 0.5s ease;
}

.main-title{
    text-align:center;
    font-size:3rem;
    font-weight:bold;
    color:#FFD700;
}

.sub-title{
    text-align:center;
    color:white;
    font-size:1.2rem;
    margin-bottom:30px;
}

.result-card{
    padding:25px;
    border-radius:20px;
    background:rgba(255,255,255,0.12);
    backdrop-filter:blur(10px);
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🌌 MBTI 전설 포켓몬 매칭 🌌</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">당신과 가장 잘 어울리는 전설 포켓몬은?</div>',
    unsafe_allow_html=True
)

# -------------------------
# MBTI 데이터
# -------------------------

pokemon_data = {

    "INTJ":{
        "name":"뮤츠",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/mewtwo.gif",
        "color":"#8B5CF6",
        "type":"초능력",
        "mbti":"전략적이고 독립적인 천재형",
        "pokemon":"강력한 초능력을 가진 전설의 포켓몬.",
        "reason":"냉철한 분석력과 목표 지향적 성향이 닮았습니다."
    },

    "INTP":{
        "name":"디아루가",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/dialga.gif",
        "color":"#60A5FA",
        "type":"강철/드래곤",
        "mbti":"논리적이고 탐구심 많은 사색가",
        "pokemon":"시간을 관장하는 전설 포켓몬.",
        "reason":"깊은 사고와 탐구 정신이 잘 어울립니다."
    },

    "ENTJ":{
        "name":"레쿠쟈",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/rayquaza.gif",
        "color":"#22C55E",
        "type":"드래곤/비행",
        "mbti":"카리스마 넘치는 지휘관",
        "pokemon":"하늘을 지배하는 강력한 전설 포켓몬.",
        "reason":"강한 리더십과 존재감을 상징합니다."
    },

    "ENTP":{
        "name":"후파",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/hoopa.gif",
        "color":"#F59E0B",
        "type":"에스퍼/고스트",
        "mbti":"창의적인 혁신가",
        "pokemon":"차원을 넘나드는 신비한 포켓몬.",
        "reason":"독창적이고 틀을 깨는 성격과 닮았습니다."
    },

    "INFJ":{
        "name":"루기아",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/lugia.gif",
        "color":"#38BDF8",
        "type":"에스퍼/비행",
        "mbti":"통찰력 있는 이상주의자",
        "pokemon":"바다를 수호하는 전설 포켓몬.",
        "reason":"평화와 조화를 추구하는 모습이 비슷합니다."
    },

    "INFP":{
        "name":"세레비",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/celebi.gif",
        "color":"#4ADE80",
        "type":"에스퍼/풀",
        "mbti":"감성적인 몽상가",
        "pokemon":"숲과 시간을 지키는 환상 포켓몬.",
        "reason":"순수함과 상상력이 닮았습니다."
    },

    "ENFJ":{
        "name":"자시안",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/zacian.gif",
        "color":"#FBBF24",
        "type":"페어리/강철",
        "mbti":"따뜻한 리더",
        "pokemon":"정의를 상징하는 전설 포켓몬.",
        "reason":"사람들을 이끄는 능력이 비슷합니다."
    },

    "ENFP":{
        "name":"지라치",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/jirachi.gif",
        "color":"#FDE047",
        "type":"강철/에스퍼",
        "mbti":"열정적인 자유로운 영혼",
        "pokemon":"소원을 이루어주는 환상 포켓몬.",
        "reason":"긍정적인 에너지와 희망을 상징합니다."
    },

    "ISTJ":{
        "name":"레지기가스",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/regigigas.gif",
        "color":"#A3A3A3",
        "type":"노말",
        "mbti":"책임감 강한 현실주의자",
        "pokemon":"고대 전설 포켓몬.",
        "reason":"묵묵하게 임무를 수행하는 모습이 닮았습니다."
    },

    "ISFJ":{
        "name":"크레세리아",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/cresselia.gif",
        "color":"#F9A8D4",
        "type":"에스퍼",
        "mbti":"헌신적인 수호자",
        "pokemon":"좋은 꿈을 선사하는 포켓몬.",
        "reason":"배려심과 따뜻함이 비슷합니다."
    },

    "ESTJ":{
        "name":"그란돈",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/groudon.gif",
        "color":"#DC2626",
        "type":"땅",
        "mbti":"강력한 관리자",
        "pokemon":"대지를 창조한 전설 포켓몬.",
        "reason":"압도적인 추진력과 결단력을 가졌습니다."
    },

    "ESFJ":{
        "name":"자마젠타",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/zamazenta.gif",
        "color":"#3B82F6",
        "type":"격투/강철",
        "mbti":"사교적인 협력가",
        "pokemon":"동료를 지키는 방패 포켓몬.",
        "reason":"주변 사람을 챙기는 성향이 닮았습니다."
    },

    "ISTP":{
        "name":"제라오라",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/zeraora.gif",
        "color":"#FACC15",
        "type":"전기",
        "mbti":"독립적인 장인",
        "pokemon":"번개처럼 빠른 환상 포켓몬.",
        "reason":"실전 능력과 침착함이 비슷합니다."
    },

    "ISFP":{
        "name":"쉐이미",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/shaymin.gif",
        "color":"#86EFAC",
        "type":"풀",
        "mbti":"예술적인 모험가",
        "pokemon":"감사의 마음을 상징하는 포켓몬.",
        "reason":"따뜻한 감성과 자유로움이 닮았습니다."
    },

    "ESTP":{
        "name":"코라이돈",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/koraidon.gif",
        "color":"#FB7185",
        "type":"격투/드래곤",
        "mbti":"대담한 모험가",
        "pokemon":"강인한 힘을 가진 전설 포켓몬.",
        "reason":"행동력과 도전 정신이 비슷합니다."
    },

    "ESFP":{
        "name":"케르디오",
        "gif":"https://play.pokemonshowdown.com/sprites/ani/keldeo.gif",
        "color":"#60A5FA",
        "type":"물/격투",
        "mbti":"즐거움을 전하는 엔터테이너",
        "pokemon":"용감하고 활기찬 환상 포켓몬.",
        "reason":"밝은 에너지와 긍정성이 닮았습니다."
    }

}

mbti = st.text_input(
    "🔍 MBTI를 입력하세요 (예: INFP)"
).upper().strip()
# -------------------------
# MBTI별 애니메이션 배경
# -------------------------

themes = {

    "INTJ": """
    background:
    radial-gradient(circle at 20% 20%, rgba(168,85,247,.35), transparent 30%),
    radial-gradient(circle at 80% 70%, rgba(139,92,246,.35), transparent 30%),
    #050816;
    """,

    "INTP": """
    background:
    radial-gradient(circle at 10% 30%, rgba(96,165,250,.30), transparent 25%),
    radial-gradient(circle at 80% 60%, rgba(59,130,246,.30), transparent 25%),
    #081120;
    """,

    "ENTJ": """
    background:
    radial-gradient(circle at 30% 20%, rgba(34,197,94,.35), transparent 30%),
    radial-gradient(circle at 70% 70%, rgba(22,163,74,.35), transparent 30%),
    #03140b;
    """,

    "ENTP": """
    background:
    radial-gradient(circle at 30% 30%, rgba(245,158,11,.35), transparent 30%),
    radial-gradient(circle at 70% 60%, rgba(251,191,36,.35), transparent 30%),
    #1a1200;
    """,

    "INFJ": """
    background:
    linear-gradient(135deg,#082f49,#0c4a6e,#164e63);
    """,

    "INFP": """
    background:
    radial-gradient(circle at 20% 20%, rgba(74,222,128,.25), transparent 30%),
    radial-gradient(circle at 70% 60%, rgba(34,197,94,.25), transparent 30%),
    #02150a;
    """,

    "ENFJ": """
    background:
    linear-gradient(135deg,#78350f,#f59e0b,#fbbf24);
    """,

    "ENFP": """
    background:
    linear-gradient(135deg,#facc15,#fde047,#fff7ae);
    """,

    "ISTJ": """
    background:
    linear-gradient(135deg,#262626,#404040,#737373);
    """,

    "ISFJ": """
    background:
    linear-gradient(135deg,#831843,#ec4899,#f9a8d4);
    """,

    "ESTJ": """
    background:
    linear-gradient(135deg,#450a0a,#b91c1c,#dc2626);
    """,

    "ESFJ": """
    background:
    linear-gradient(135deg,#1e3a8a,#2563eb,#60a5fa);
    """,

    "ISTP": """
    background:
    linear-gradient(135deg,#713f12,#eab308,#fde047);
    """,

    "ISFP": """
    background:
    linear-gradient(135deg,#14532d,#22c55e,#86efac);
    """,

    "ESTP": """
    background:
    linear-gradient(135deg,#881337,#e11d48,#fb7185);
    """,

    "ESFP": """
    background:
    linear-gradient(135deg,#0c4a6e,#2563eb,#60a5fa);
    """
}


def apply_theme(mbti):

    if mbti not in themes:
        return

    bg = themes[mbti]

    st.markdown(
        f"""
<style>
.flip-card{
background:transparent;
width:320px;
height:450px;
margin:auto;
perspective:1000px;
}

.flip-card-inner{
position:relative;
width:100%;
height:100%;
text-align:center;
transition:transform .8s;
transform-style:preserve-3d;
}

.flip-card:hover .flip-card-inner{
transform:rotateY(180deg);
}

.flip-card-front,
.flip-card-back{

position:absolute;

width:100%;
height:100%;

backface-visibility:hidden;

border-radius:25px;

overflow:hidden;

border:2px solid rgba(255,255,255,.2);

backdrop-filter:blur(15px);

box-shadow:
0 0 30px rgba(255,255,255,.15),
0 0 80px rgba(255,255,255,.1);

}

.flip-card-front{

background:
linear-gradient(
135deg,
rgba(255,255,255,.15),
rgba(255,255,255,.05)
);

}

.flip-card-back{

background:
linear-gradient(
135deg,
rgba(0,0,0,.65),
rgba(30,41,59,.9)
);

transform:rotateY(180deg);

padding:20px;

box-sizing:border-box;

}
.stApp {{
{bg}
background-size:400% 400%;
animation:gradientMove 12s ease infinite;
}}

@keyframes gradientMove {{
0%{{background-position:0% 50%;}}
50%{{background-position:100% 50%;}}
100%{{background-position:0% 50%;}}
}}

.glow-card {{
border-radius:24px;
padding:25px;
backdrop-filter:blur(12px);
background:rgba(255,255,255,0.10);
box-shadow:
0 0 25px rgba(255,255,255,.15),
0 0 50px rgba(255,255,255,.10);
animation:floatCard 3s ease-in-out infinite;
}}

@keyframes floatCard {{
0%{{transform:translateY(0px);}}
50%{{transform:translateY(-8px);}}
100%{{transform:translateY(0px);}}
}}

.star {{
position:fixed;
width:2px;
height:2px;
background:white;
border-radius:50%;
animation:twinkle 3s infinite;
}}

@keyframes twinkle {{
0%{{opacity:.2;}}
50%{{opacity:1;}}
100%{{opacity:.2;}}
}}

</style>
""",
        unsafe_allow_html=True
    )
    # -------------------------
# 랜덤 명언
# -------------------------

import random

quotes = [
    "🌟 전설은 기다리지 않는다. 스스로 만들어 가는 것이다.",
    "⚡ 너만의 강점은 생각보다 훨씬 강력하다.",
    "🌌 모든 모험은 작은 한 걸음에서 시작된다.",
    "🔥 실패는 끝이 아니라 성장의 경험이다.",
    "💎 진짜 힘은 자신을 믿는 데서 나온다.",
    "🦄 꿈을 꾸는 사람만이 새로운 길을 찾는다.",
    "🌠 오늘의 선택이 미래의 전설이 된다.",
    "🚀 포기하지 않는 사람이 결국 도착한다."
]

# -------------------------
# 결과 출력
# -------------------------

if mbti:

    if mbti in pokemon_data:

        apply_theme(mbti)

        data = pokemon_data[mbti]

        if st.button("✨ 나의 전설 포켓몬 확인하기 ✨", use_container_width=True):

            st.balloons()

            quote = random.choice(quotes)

            st.markdown(
                f"""
                <div class="glow-card">

                <h1 style="text-align:center;color:{data['color']};">
                🌟 {data['name']} 🌟
                </h1>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.image(
                data["gif"],
                width=280
            )

            st.markdown("---")

            st.markdown(
                f"""
### 🧠 MBTI 성향

**{data['mbti']}**

### ⚔️ 타입

**{data['type']}**

### 📖 포켓몬 소개

{data['pokemon']}

### ✨ 왜 잘 어울릴까?

{data['reason']}
"""
            )

            st.markdown("---")

            st.success(quote)

            st.markdown(
                f"""
<div style="
padding:20px;
border-radius:20px;
background:rgba(255,255,255,0.1);
text-align:center;
font-size:22px;
">

🏆 당신은 <b>{data['name']}</b>의 힘을 가진 사람입니다!

</div>
""",
                unsafe_allow_html=True
            )

            st.markdown("")

            st.markdown("### 🎮 비슷한 전설 포켓몬")

            similar = {
                "INTJ": ["다크라이", "기라티나"],
                "INTP": ["펄기아", "데옥시스"],
                "ENTJ": ["제크로무", "이벨타르"],
                "ENTP": ["마샤도", "볼케니온"],
                "INFJ": ["스이쿤", "라티아스"],
                "INFP": ["마나피", "뮤"],
                "ENFJ": ["솔가레오", "비크티니"],
                "ENFP": ["쉐이미", "뮤"],
                "ISTJ": ["레지락", "레지스틸"],
                "ISFJ": ["피오네", "라티아스"],
                "ESTJ": ["디안시", "그란돈"],
                "ESFJ": ["자시안", "비크티니"],
                "ISTP": ["썬더", "제크로무"],
                "ISFP": ["마나피", "쉐이미"],
                "ESTP": ["무한다이노", "레쿠쟈"],
                "ESFP": ["비크티니", "케르디오"]
            }

            st.info(
                " · ".join(similar[mbti])
            )

    else:

        st.error(
            "⚠️ 올바른 MBTI를 입력해 주세요. (예: INFP, ENTJ)"
        )

else:

    st.markdown("""
### 🎯 사용 방법

1. MBTI 입력
2. 버튼 클릭
3. 전설 포켓몬 확인!

예시:
- INTJ
- ENFP
- ISTP
- ESFJ
""")

st.markdown("---")

st.caption(
    "🌌 MBTI와 포켓몬 매칭은 재미를 위한 콘텐츠입니다."
)
