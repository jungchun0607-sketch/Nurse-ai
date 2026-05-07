import streamlit as st

st.set_page_config(
    page_title="護理國考 AI 學習平台",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 護理國考 AI 學習平台 PRO")

st.markdown("## 📚 國考重點")

subject = st.selectbox(
    "選擇科目",
    ["基醫", "基護行政", "內外", "產兒", "精神社區"]
)

if subject == "內外":

    st.subheader("COPD 慢性阻塞性肺病")

    st.success("✨ 國考超高頻")

    st.write("""
### 重點整理

- 桶狀胸
- 呼氣延長
- 低氧高碳酸血症
- 避免高濃度氧氣
- 姿勢：三腳架姿勢
""")

    st.warning("""
⚠️ 易錯觀念：

COPD 不可以給高濃度氧氣
""")

    st.markdown("---")

    st.subheader("📝 10題章節測驗")

    q1 = st.radio(
        "1. COPD 病人最重要護理措施？",
        ["高濃度氧氣", "監測呼吸", "大量輸液"],
        key="q1"
    )

    if st.button("提交答案"):

        if q1 == "監測呼吸":
            st.success("✅ 正確")

            st.info("""
解析：

COPD 最重要是維持呼吸功能，
避免二氧化碳滯留。
""")

        else:
            st.error("❌ 錯誤")

            st.info("""
解析：

COPD 過高氧氣可能抑制呼吸。
""")

else:
    st.info("此科目內容建置中")

st.markdown("---")

st.subheader("📊 學習分析")

st.write("目前尚無資料")
