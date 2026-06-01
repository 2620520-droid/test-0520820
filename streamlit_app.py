import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import random
import time

# 저녁 메뉴 후보들
menu_list = ["삼겹살에 소주", "치킨에 맥주", "매콤한 떡볶이", "깔끔한 초밥", "뜨끈한 국밥", "백종원 레시피 라면"]

print("🤖: 오늘 뭐 먹을지 고민이신가요? 제가 골라드릴게요.")
time.sleep(1)
print("🤖: 주방장 빙의해서 고민 중...")
time.sleep(1.5)

# 랜덤으로 하나 선택
selected_menu = random.choice(menu_list)

print(f"\n🎉 짜잔! 오늘 저녁 메뉴는 **[{selected_menu}]** 어떠세요?")