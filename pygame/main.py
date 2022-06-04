import pygame

pygame.init()  # 초기화 코드 ( 반드시 필요 )

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Test Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("E:/code/pywrk/pygame_basic/background.png")

# 캐릭터 이미지 불러오기
character = pygame.image.load("E:/code/pywrk/pygame_basic/char.png")
character_size = character.get_rect().size
character_width = character_size[0]  # 캐 가로크기
character_height = character_size[1]  # 캐 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True
print("게임 작동 성공")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 누르면 게임 창 끄기
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 배경 그리기

    pygame.display.update()  # 게임 화면 다시 그리기


# pygame 종료
pygame.quit()
print("게임 작동 종료")
