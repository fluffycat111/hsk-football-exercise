import streamlit as st

# 初始化状态
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = {}

st.title("课后练习平台")

# 模块选择
module = st.sidebar.radio("选择题型模块：", [
    "选择题", "翻牌题", "角色互动题", "填空题", "排序题", "查看成绩"
])

# ========== 模块 1：选择题 ==========
if module == "选择题":
    st.header("📘 选择题模块")
    choice_questions = [
        {
            "question": "莎莉每天跑步多长时间？",
            "options": ["十分钟", "三十分钟", "一小时"],
            "answer": "三十分钟",
        },
        {
            "question": "大卫是从几岁开始踢足球的？",
            "options": ["六岁", "八岁", "十岁"],
            "answer": "八岁",
        },
        {
            "question": "莎莉跑步已经跑了多久？",
            "options": ["三年", "五年", "八九年"],
            "answer": "八九年",
        },
        {
            "question": "大卫除了踢足球，还喜欢什么运动？",
            "options": ["打篮球和游泳", "跳舞和唱歌", "打羽毛球和乒乓球"],
            "answer": "打篮球和游泳",
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
            if st.session_state.submitted[answer_key]:
                st.success("✅ 正确")
            else:
                st.error("❌ 错误")

# ========== 模块 2：翻牌题 ==========
elif module == "翻牌题":
    st.header("🃏 翻牌题模块（词语配对）")
    flip_questions = [
        {"word": "跑步", "definition": "一种锻炼身体的有氧运动"},
        {"word": "游泳", "definition": "在水里移动身体的一种运动"},
        {"word": "打篮球", "definition": "用手投球进篮筐的运动"},
        {"word": "踢足球", "definition": "用脚踢球的运动"},
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
            if st.session_state.submitted[result_key]:
                st.success("✅ 正确")
            else:
                st.error("❌ 错误")

# ========== 模块 3：角色互动题 ==========
elif module == "角色互动题":
    st.header("🎭 角色互动题模块")
    role_plays = [
        {"role": "你是莎莉，请介绍你从什么时候开始跑步。", "hint": "我从十岁开始……"},
        {"role": "你是大卫，请介绍你喜欢的运动。", "hint": "我喜欢……"},
        {"role": "你是莎莉，请说说你每天跑多长时间。", "hint": "我每天跑……"},
        {"role": "你是大卫，请说说你踢足球多久了。", "hint": "我已经踢了……"},
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
            if st.session_state.submitted[rp_key]:
                st.success("✅ 已提交")
            else:
                st.warning("❗尚未作答")

# ========== 模块 4：填空题 ==========
elif module == "填空题":
    st.header("✏️ 填空题模块")
    blanks = [
        {"sentence": "莎莉每天早上跑____分钟。", "answer": "三十"},
        {"sentence": "大卫从____岁开始踢足球。", "answer": "八"},
        {"sentence": "莎莉已经跑了____年了。", "answer": "八九"},
        {"sentence": "大卫说他篮球打得____。", "answer": "不好"},
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
            if st.session_state.submitted[fill_key]:
                st.success("✅ 正确")
            else:
                st.error("❌ 错误")

# ========== 模块 5：排序题 ==========
elif module == "排序题":
    st.header("🔢 排序题模块")
    order_qs = [
        {
            "instruction": "将莎莉跑步的过程按顺序排列：",
            "items": ["从十岁开始跑步", "跑三十分钟", "每天早上跑步", "已经跑了八九年"],
            "answer": ["从十岁开始跑步", "每天早上跑步", "跑三十分钟", "已经跑了八九年"]
        },
        {
            "instruction": "整理大卫的运动兴趣介绍顺序：",
            "items": ["喜欢打篮球", "喜欢游泳", "从八岁开始踢足球", "已经踢了十多年"],
            "answer": ["从八岁开始踢足球", "已经踢了十多年", "喜欢打篮球", "喜欢游泳"]
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
            if st.session_state.submitted[order_key]:
                st.success("✅ 正确")
            else:
                st.error("❌ 错误")

# ========== 模块 6：查看成绩 ==========
elif module == "查看成绩":
    st.header("📊 成绩总结")
    st.info(f"你的总得分是：{st.session_state.score} / 18 分。")
    report = f"《二语最后一节课》课后练习报告\n总得分：{st.session_state.score} / 18\n继续努力！"
    st.download_button("📄 下载成绩报告（txt）", report, file_name="成绩报告.txt")
