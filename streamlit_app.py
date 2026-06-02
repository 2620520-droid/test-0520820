import streamlit as st
import random

# 저녁 메뉴 후보
menu_list = [
    "삼겹살에 소주",
    "치킨에 맥주",
    "매콤한 떡볶이",
    "깔끔한 초밥",
    "뜨끈한 국밥",
    "백종원 레시피 라면"
]

st.title("🍽️ 오늘의 저녁 메뉴 추천기")
st.write("뭘 먹을지 고민된다면 버튼을 눌러보세요!")

if st.button("🎲 메뉴 추천받기"):
    selected_menu = random.choice(menu_list)
    st.success(f"🎉 오늘의 저녁 메뉴는 **{selected_menu}** 입니다!")