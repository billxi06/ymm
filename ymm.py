import streamlit as st
import os

# 设置页面标题
st.set_page_config(page_title="宝贝别生气了")

# 模拟导航栏
nav_style = """
<style>
nav {
    background-color: #ac0fac3e;
    overflow: hidden;
}
nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}
nav ul li {
    float: left;
}
nav ul li a {
    display: block;
    color: rgb(220, 239, 11);
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}
nav ul li a:hover {
    background-color: #12e80f;
}
</style>
"""
st.markdown(nav_style, unsafe_allow_html=True)
nav_html = """
<nav>
    <ul>
        <li><a href="#">沉鱼落雁</a></li>
        <li><a href="#">闭月羞花</a></li>
        <li><a href="#">亭亭玉立</a></li>
        <li><a href="#">明眸皓齿</a></li>
        <li><a href="#">光彩照人</a></li>
    </ul>
</nav>
"""
st.markdown(nav_html, unsafe_allow_html=True)

# 模拟浮动框
box_style = """
<style>
.float-box {
    float: left;
    width: 30%;
    margin: 1.5%;
    padding: 20px;
    background-color: #970af6;
    box-sizing: border-box;
}
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
a {
    color: #f30808;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
"""
st.markdown(box_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='float-box'>", unsafe_allow_html=True)
    st.header("美照")
    image1_path = "微信图片_20250720181826.jpg"
    if os.path.exists(image1_path):
        st.image(image1_path, width=205, caption="图片 1")
    else:
        st.write("未找到图片 1")
    st.write("实在是太漂亮了")
    st.markdown("<a href='#'>了解更多</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='float-box'>", unsafe_allow_html=True)
    st.header("美照")
    image2_path = "微信图片_20250720181844.jpg"
    if os.path.exists(image2_path):
        st.image(image2_path, width=250, caption="图片 2")
    else:
        st.write("未找到图片 2")
    st.write("实在是太可爱了")
    st.markdown("<a href='#'>了解更多</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='float-box'>", unsafe_allow_html=True)
    st.header("美照")
    gif_path = "微信图片_20250720181850.jpg"
    if os.path.exists(gif_path):
        st.image(gif_path, width=250, caption="图片 3")
    else:
        st.write("未找到图片 3")
    st.write("实在是太好看了")
    st.markdown("<a href='#'>了解更多</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)