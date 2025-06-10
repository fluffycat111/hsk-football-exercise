import streamlit as st

# 初始化状态
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = {}

st.title("《你的足球踢得真好》课后练习平台")

# 模块选择
module = st.sidebar.radio("选择题型模块：", [
    "选择题", "翻牌题", "角色互动题", "填空题", "排序题", "查看成绩"
])

# ========== 模块 1：选择题 ==========
if module == "选择题":
    st.header("📘 选择题模块")
    choice_questions = [
        {
            "question": "小明为什么喜欢踢足球？",
            "options": ["因为他个子高", "因为他跑得快", "因为他觉得踢足球很快乐"],
            "answer": "因为他觉得踢足球很快乐",
        },
        {
            "question": "他们一般在哪里踢足球？",
            "options": ["教室", "操场", "公园"],
            "answer": "操场",
        },
        {
            "question": "老师看到他们踢足球时说了什么？",
            "options": ["不要踢球", "你们踢得真好", "快点回教室"],
            "answer": "你们踢得真好",
        },
        {
            "question": "小明的好朋友是谁？",
            "options": ["小刚", "小红", "小华"],
            "answer": "小刚",
        },
    ]
    for i, q in enumerate(choice_questions):
        st.markdown(f"**Q{i+1}. {q['question']}**")
        key = f"choice_{i}"
        answer_key = f"choice_result_{i}"
        choice = st.radio("请选择：", q["options"], key=key, label_visibility="collapsed")
        if st.button(f"提交第{i+1}题", key=f"submit_choice_{i}"):
            if choice == q["answer"]:
                st.success("回答正确！")
                if not st.session_state.submitted.get(answer_key):
                    st.session_state.score += 1
                    st.session_state.submitted[answer_key] = True
            else:
                st.error("回答错误")
                st.session_state.submitted[answer_key] = False
        elif answer_key in st.session_state.submitted:
            st.success("✅ 正确") if st.session_state.submitted[answer_key] else st.error("❌ 错误")

# ========== 模块 2：翻牌题 ==========
elif module == "翻牌题":
    st.header("🃏 翻牌题模块（词语配对）")
    flip_questions = [
        {"word": "足球", "definition": "一种球类运动，用脚踢"},
        {"word": "操场", "definition": "学生上体育课或课间活动的地方"},
        {"word": "快乐", "definition": "高兴、开心"},
        {"word": "朋友", "definition": "关系亲密的人"},
    ]
    for i, pair in enumerate(flip_questions):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**词语{i+1}:** {pair['word']}")
        with col2:
            user_input = st.text_input("输入对应含义：", key=f"flip_input_{i}")
        result_key = f"flip_result_{i}"
        if st.button(f"提交词语{i+1}", key=f"flip_submit_{i}"):
            if pair["definition"] in user_input:
                st.success("匹配正确！")
                if not st.session_state.submitted.get(result_key):
                    st.session_state.score += 1
                    st.session_state.submitted[result_key] = True
            else:
                st.error("匹配不正确")
                st.session_state.submitted[result_key] = False
        elif result_key in st.session_state.submitted:
            st.success("✅ 正确") if st.session_state.submitted[result_key] else st.error("❌ 错误")

# ========== 模块 3：角色互动题 ==========
elif module == "角色互动题":
    st.header("🎭 角色互动题模块")
    role_plays = [
        {"role": "你是小明，请你介绍你为什么喜欢踢足球。", "hint": "我喜欢踢足球，因为……"},
        {"role": "你是老师，你看到小朋友踢球说些什么？", "hint": "你们踢得真……"},
        {"role": "你是小刚，请你说说你和谁一起踢足球。", "hint": "我和……一起踢足球"},
        {"role": "你是家长，请说一句鼓励孩子运动的话。", "hint": "运动可以让你更……"},
    ]
    for i, rp in enumerate(role_plays):
        st.markdown(f"**Q{i+1}: {rp['role']}**")
        user_text = st.text_area("你的回答：", key=f"rp_input_{i}", placeholder=rp["hint"])
        rp_key = f"rp_{i}"
        if st.button(f"提交角色{i+1}", key=f"submit_rp_{i}"):
            if user_text.strip():
                st.success("提交成功")
                if not st.session_state.submitted.get(rp_key):
                    st.session_state.score += 1
                    st.session_state.submitted[rp_key] = True
            else:
                st.warning("请填写后再提交。")
                st.session_state.submitted[rp_key] = False
        elif rp_key in st.session_state.submitted:
            st.success("✅ 已提交") if st.session_state.submitted[rp_key] else st.warning("❗尚未作答")

# ========== 模块 4：填空题 ==========
elif module == "填空题":
    st.header("✏️ 填空题模块")
    blanks = [
        {"sentence": "小明每天放学后都会去____踢足球。", "answer": "操场"},
        {"sentence": "他和好朋友____一起踢球。", "answer": "小刚"},
        {"sentence": "老师说：“你们踢得____！”", "answer": "真好"},
        {"sentence": "踢足球让小明感到非常____。", "answer": "快乐"},
    ]
    for i, item in enumerate(blanks):
        st.markdown(f"**Q{i+1}. {item['sentence']}**")
        user_fill = st.text_input("填写空白：", key=f"blank_input_{i}")
        fill_key = f"blank_{i}"
        if st.button(f"提交第{i+1}空", key=f"submit_blank_{i}"):
            if user_fill.strip() == item["answer"]:
                st.success("填写正确！")
                if not st.session_state.submitted.get(fill_key):
                    st.session_state.score += 1
                    st.session_state.submitted[fill_key] = True
            else:
                st.error("填写错误")
                st.session_state.submitted[fill_key] = False
        elif fill_key in st.session_state.submitted:
            st.success("✅ 正确") if st.session_state.submitted[fill_key] else st.error("❌ 错误")

# ========== 模块 5：排序题 ==========
elif module == "排序题":
    st.header("🔢 排序题模块")
    order_qs = [
        {
            "instruction": "将以下句子按时间顺序排列：",
            "items": ["他放学去操场", "他回家吃饭", "他和朋友踢足球", "他背着书包走出教室"],
            "answer": ["他背着书包走出教室", "他放学去操场", "他和朋友踢足球", "他回家吃饭"]
        },
        {
            "instruction": "将下列动作排序组成完整句：",
            "items": ["踢足球", "小刚", "喜欢", "很"],
            "answer": ["小刚", "很", "喜欢", "踢足球"]
        },
        {
            "instruction": "整理早晨活动顺序：",
            "items": ["刷牙", "穿衣服", "吃早餐", "起床"],
            "answer": ["起床", "刷牙", "穿衣服", "吃早餐"]
        },
        {
            "instruction": "完成故事情节排序：",
            "items": ["老师表扬他们", "他们踢得很开心", "他们开始踢球", "他们来到操场"],
            "answer": ["他们来到操场", "他们开始踢球", "他们踢得很开心", "老师表扬他们"]
        },
    ]
    for i, q in enumerate(order_qs):
        st.markdown(f"**Q{i+1}. {q['instruction']}**")
        selected = st.multiselect("请选择正确顺序：", q["items"], key=f"order_{i}")
        order_key = f"order_{i}"
        if st.button(f"提交排序{i+1}", key=f"submit_order_{i}"):
            if selected == q["answer"]:
                st.success("排序正确！")
                if not st.session_state.submitted.get(order_key):
                    st.session_state.score += 1
                    st.session_state.submitted[order_key] = True
            else:
                st.error("顺序不对")
                st.session_state.submitted[order_key] = False
        elif order_key in st.session_state.submitted:
            st.success("✅ 正确") if st.session_state.submitted[order_key] else st.error("❌ 错误")

# ========== 模块 6：查看成绩 ==========
elif module == "查看成绩":
    st.header("📊 成绩总结")
    st.info(f"你的总得分是：{st.session_state.score} / 20 分。")
    report = f"《你的足球踢得真好》课后练习报告\n总得分：{st.session_state.score} / 20\n继续努力！"
    st.download_button("📄 下载成绩报告（txt）", report, file_name="成绩报告.txt")
