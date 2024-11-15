import time
from PIL import Image
from JoyStick import Joystick
from Visitor import Visitor
from Point_Heart import PointHeart
from Cook import Cook

# Joystick 인스턴스 생성 및 백라이트 켜기
joystick = Joystick()
joystick.backlight.value = True

# 시작 화면
joystick.display_image("Start.png")

# 버튼 #5 (button_A) 누르기 전까지 대기
while joystick.buttons["A"].value:
    time.sleep(0.1)

initial_background = Image.open("Fund.png").resize((joystick.width, joystick.height)).convert("RGB")
point_heart = PointHeart(joystick)
cook = Cook()
joystick.disp.image(initial_background)

# 최대 등장 횟수와 등장 카운트 설정
max_visits = 7
visit_count = 0

# 게임 루프 - 손님 등장
while visit_count < max_visits:
    visitor = Visitor(joystick, initial_background, point_heart, cook)
    visitor.move_and_display_visitor()
    visit_count += 1
    initial_background = Image.open("Fund.png").resize((joystick.width, joystick.height)).convert("RGB")

print("게임 종료: 손님이 7번 등장했습니다.")
