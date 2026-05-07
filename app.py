
import streamlit as st
import pandas as pd

st.set_page_config(page_title="護理國考 AI 學習平台 PRO", layout="wide")

st.title("🩺 護理國考 AI 學習平台 PRO")
st.caption("專為台灣護理國考生打造｜重點整理 × 國考邏輯 × AI解析")

subjects = {
    "內外 - 心衰竭": {
        "summary": [
            "左心衰竭：肺水腫、呼吸困難、粉紅泡沫痰",
            "右心衰竭：下肢水腫、頸靜脈怒張、肝腫大",
            "BNP 上升為重要指標",
            "Digoxin 使用需注意低血鉀"
        ],
        "high_freq": [
            "Orthopnea",
            "BNP",
            "Digoxin",
            "肺水腫",
            "限鈉限水"
        ],
        "easy_wrong": [
            "左右心衰竭症狀混淆",
            "Digoxin 中毒忘記監測 K+"
        ],
        "questions": [
            {
                "q":"左心衰竭最典型症狀為何？",
                "options":["下肢水腫","粉紅泡沫痰","肝腫大","腹水"],
                "answer":"粉紅泡沫痰",
                "analysis":"左心衰竭會導致肺水腫，因此出現粉紅泡沫痰。"
            },
            {
                "q":"使用 Digoxin 最需注意哪項電解質？",
                "options":["Na+","Ca+","K+","Mg+"],
                "answer":"K+",
                "analysis":"低血鉀會增加 Digoxin 中毒風險。"
            }
        ]
    }
}

menu = st.sidebar.radio(
    "功能選單",
    [
        "📚 國考重點",
        "📝 10題小測驗",
        "🔥 高頻考點",
        "⚠️ 易錯題",
        "📊 學習分析"
    ]
)

if menu == "📚 國考重點":
    topic = st.selectbox("選擇章節", list(subjects.keys()))
    data = subjects[topic]

    st.header("📌 國考重點整理")
    for idx, item in enumerate(data["summary"],1):
        st.markdown(f"### {idx}. {item}")

    st.divider()

    st.header("🔥 國考超高頻")
    for item in data["high_freq"]:
        st.success(item)

    st.divider()

    st.header("⚠️ 學生最容易錯")
    for item in data["easy_wrong"]:
        st.error(item)

    st.info("整合：華杏捷徑｜三元及第｜高點｜先鋒｜丁玥 國考觀念")

elif menu == "📝 10題小測驗":
    topic = st.selectbox("選擇測驗章節", list(subjects.keys()))
    data = subjects[topic]

    st.header("📝 章節測驗")

    score = 0

    for idx, q in enumerate(data["questions"],1):
        st.subheader(f"第 {idx} 題")
        ans = st.radio(
            q["q"],
            q["options"],
            key=f"q_{idx}"
        )

        if st.button(f"查看解析 {idx}"):
            if ans == q["answer"]:
                st.success("答對了")
                score += 1
            else:
                st.error(f"答錯，正確答案：{q['answer']}")

            st.info(q["analysis"])

    st.divider()
    st.warning("完整版可擴充：20題混合模擬考、錯題本、AI弱點分析")

elif menu == "🔥 高頻考點":

    st.header("🔥 近年考選部高頻主題")

    df = pd.DataFrame({
        "主題":["COPD","心衰竭","腎衰竭","酸鹼值","糖尿病"],
        "近5年出題次數":[14,12,11,10,9]
    })

    st.dataframe(df, use_container_width=True)

elif menu == "⚠️ 易錯題":

    st.header("⚠️ 學生最容易錯 TOP 題型")

    wrong = [
        "SIADH vs DI",
        "酸鹼值判讀",
        "Digoxin 中毒",
        "產後出血",
        "胰島素作用時間"
    ]

    for idx, item in enumerate(wrong,1):
        st.error(f"{idx}. {item}")

elif menu == "📊 學習分析":

    st.header("📊 AI 學習分析")

    st.metric("今日完成題數", "20")
    st.metric("正確率", "78%")
    st.metric("最弱科目", "內外")

    st.progress(78)

    st.success("建議今天優先複習：心衰竭、酸鹼值、Digoxin")
