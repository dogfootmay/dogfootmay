import pygame

pygame.init()  # 초기화 코드 ( 반드시 필요 )

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Test Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()

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

# 이동 속도

character_speed = 0.6

# 적 enemy 캐릭터

enemy = pygame.image.load("E:/code/pywrk/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]  # 캐 가로크기
enemy_height = enemy_size[1]  # 캐 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()  # 시작 틱을 받아옴

# 이벤트 루프
running = True
print("게임 작동 성공")
while running:
    dt = clock.tick(60)  # 게임 화면의 초당 프레임 수
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 누르면 게임 창 끄기
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌을 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 이미지 넣기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 주인공 쨩 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 빌런쨩 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s)단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    pygame.display.update()  # 게임 화면 다시 그리기

# 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()
print("게임 작동 종료")
