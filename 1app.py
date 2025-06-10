import streamlit as st

st.set_page_config(page_title="《你的足球踢得真好》练习平台", layout="centered")
st.title("⚽ 《你的足球踢得真好》课后练习平台")

# 分数管理
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.answered = set()

# 页面导航
page = st.sidebar.radio("请选择模块：", [
    "词汇翻牌题",
    "选择题练习",
    "角色互动题",
    "填空题",
    "排序题",
    "小结与反馈"
])

### 1. 🃏 翻牌题
if page == "词汇翻牌题":
    st.subheader("🃏 词汇翻牌题")
    cards = {
        "跑步": "running", "足球": "football", "喜欢": "to like", "每天": "every day",
        "开始": "to start", "从": "from", "十岁": "ten years old",
        "游泳": "swimming", "篮球": "basketball", "踢得真好": "play really well"
    }
    if "flipped" not in st.session_state:
        st.session_state.flipped = {k: False for k in cards}
    cols = st.columns(2)
    for i, (ch, en) in enumerate(cards.items()):
        with cols[i % 2]:
            if st.button(f"🔄 {ch}", key=ch):
                st.session_state.flipped[ch] = not st.session_state.flipped[ch]
            if st.session_state.flipped[ch]:
                st.success(f"👉 {en}")
            else:
                st.info("点击查看英文")

### 2. 📝 选择题
elif page == "选择题练习":
    st.subheader("📝 阅读理解与语法选择题")
    questions = [
        {
            "q": "David 是从几岁开始踢足球的？",
            "options": ["A. 六岁", "B. 八岁", "C. 十岁", "D. 十二岁"],
            "answer": "B. 八岁"
        },
        {
            "q": "下列哪句用了“得”字结构来表示程度？",
            "options": ["A. 我喜欢踢足球。", "B. 他每天跑三十分钟。", "C. 你踢得真好。", "D. 我从十岁开始跑步。"],
            "answer": "C. 你踢得真好。"
        },
        {
            "q": "Sally 每天跑步多久？",
            "options": ["A. 十分钟", "B. 二十分钟", "C. 三十分钟", "D. 一个小时"],
            "answer": "C. 三十分钟"
        },
        {
            "q": "“我从八岁开始踢足球”中的“从”是什么意思？",
            "options": ["A. with", "B. from", "C. for", "D. to"],
            "answer": "B. from"
        }
    ]
    for i, item in enumerate(questions):
        ans = st.radio(item["q"], item["options"], key=f"mcq{i}")
        if f"mcq{i}" not in st.session_state.answered:
            if ans == item["answer"]:
                st.success("✅ 正确")
                st.session_state.score += 1
            else:
                st.error(f"❌ 正确答案是：{item['answer']}")
            st.session_state.answered.add(f"mcq{i}")

### 3. 🎭 角色互动题
elif page == "角色互动题":
    st.subheader("🎭 模拟对话角色题")
    scenarios = [
        {
            "q": "Sally 被问到喜欢什么运动，她会说：",
            "options": [
                "A. 我喜欢跑步，因为我每天都跑三十分钟。",
                "B. 我喜欢踢足球，但是我踢得不好。",
                "C. 我喜欢游泳，因为我每天都游。"
            ],
            "answer": "A. 我喜欢跑步，因为我每天都跑三十分钟。"
        },
        {
            "q": "David 会说：",
            "options": [
                "A. 我从十岁开始打篮球。",
                "B. 我踢得不好。",
                "C. 我从八岁开始踢足球，现在已经十多年了。"
            ],
            "answer": "C. 我从八岁开始踢足球，现在已经十多年了。"
        },
        {
            "q": "Sally 为什么喜欢跑步？",
            "options": [
                "A. 因为她跑得快。",
                "B. 因为她从十岁开始跑步。",
                "C. 因为她每天早上跑三十分钟。"
            ],
            "answer": "C. 因为她每天早上跑三十分钟。"
        },
        {
            "q": "哪项最像 Sally 的生活习惯？",
            "options": [
                "A. 每天看电视一个小时。",
                "B. 每天早上跑步三十分钟。",
                "C. 每天下午踢足球。"
            ],
            "answer": "B. 每天早上跑步三十分钟。"
        }
    ]
    for i, s in enumerate(scenarios):
        ans = st.radio(s["q"], s["options"], key=f"role{i}")
        if f"role{i}" not in st.session_state.answered:
            if ans == s["answer"]:
                st.success("✅ 正确")
                st.session_state.score += 1
            else:
                st.error(f"❌ 正确答案是：{s['answer']}")
            st.session_state.answered.add(f"role{i}")

### 4. ✍️ 填空题
elif page == "填空题":
    st.subheader("✍️ 完成句子填空")
    blanks = [
        {"q": "我喜欢____，因为我每天都跑三十分钟。", "answer": "跑步"},
        {"q": "你踢得真____。", "answer": "好"},
        {"q": "我从八岁开始____足球。", "answer": "踢"},
        {"q": "Sally 每天早上____三十分钟。", "answer": "跑步"},
    ]
    for i, item in enumerate(blanks):
        user_input = st.text_input(item["q"], key=f"blank{i}")
        if f"blank{i}" not in st.session_state.answered and user_input:
            if item["answer"] in user_input:
                st.success("✅ 正确")
                st.session_state.score += 1
            else:
                st.error(f"❌ 正确答案是：{item['answer']}")
            st.session_state.answered.add(f"blank{i}")

### 5. 📊 排序题
elif page == "排序题":
    st.subheader("📊 按顺序排列事件")
    orders = [
        {
            "q": "下列事情按时间先后排序（选择第一个发生的）：",
            "options": ["A. Sally 每天跑步", "B. David 八岁开始踢足球", "C. Sally 十岁开始跑步"],
            "answer": "B. David 八岁开始踢足球"
        },
        {
            "q": "Sally 先开始跑步，还是先开始游泳？",
            "options": ["A. 跑步", "B. 游泳"],
            "answer": "A. 跑步"
        },
        {
            "q": "哪件事最早发生？",
            "options": ["A. David 开始踢足球", "B. Sally 喜欢跑步", "C. Sally 每天跑步"],
            "answer": "A. David 开始踢足球"
        },
        {
            "q": "哪个顺序正确？",
            "options": [
                "A. 喜欢运动 → 每天锻炼 → 开始踢球",
                "B. 开始踢球 → 喜欢运动 → 每天锻炼",
                "C. 每天锻炼 → 喜欢运动 → 开始踢球"
            ],
            "answer": "B. 开始踢球 → 喜欢运动 → 每天锻炼"
        }
    ]
    for i, item in enumerate(orders):
        sel = st.selectbox(item["q"], item["options"], key=f"order{i}")
        if f"order{i}" not in st.session_state.answered:
            if sel == item["answer"]:
                st.success("✅ 正确")
                st.session_state.score += 1
            else:
                st.error(f"❌ 正确答案是：{item['answer']}")
            st.session_state.answered.add(f"order{i}")

### 6. ✅ 总结页
elif page == "小结与反馈":
    st.subheader("✅ 总结与得分反馈")
    total = 20  # 每类4题，共5类答题题型
    score = st.session_state.score
    percent = round(score / total * 100)

    st.markdown(f"### 🎯 总得分：{score} / {total}（{percent}%）")

    if percent == 100:
        st.balloons()
        st.success("🎉 完美掌握！")
    elif percent >= 80:
        st.success("👍 很棒，已经掌握大部分内容！")
    elif percent >= 60:
        st.warning("📘 有一些错误，可以回顾课文后再练。")
    else:
        st.error("📖 建议回顾课文内容，多做练习题。")
