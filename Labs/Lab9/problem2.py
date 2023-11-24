import pygame
pygame.init()

#Set buttons
global play_button, next_button, prev_button, music
play_button_img = pygame.transform.scale(pygame.image.load('player_images/play.png'), (80,80))
pause_button_img = pygame.transform.scale(pygame.image.load('player_images/pause.png'), (80,80))
next_button_img = pygame.transform.scale(pygame.image.load('player_images/next.png'), (60,60))
prev_button_img = pygame.transform.scale(pygame.image.load('player_images/prev.png'), (60,60))

#Set background
background = pygame.transform.scale(pygame.image.load('player_images/background.jpg'), (400, 500))

#Set display
size = width, height = 400, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Music Player')

#Set clock
FPS = 60
clock = pygame.time.Clock()

music = {
    1: 'Imagine Dragons - Enemy (Feat. JID)',
    2: 'Meric Again - Industry Baby (feat. 22angels)',
    3: 'T3NZU - Balenciaga',
    4: 'Varien ft. Andrew Zink - Can You Feel My Heart'
}

music_len = {
    1: 173, 
    2: 136, 
    3: 168, 
    4: 232
}

def player(num, in_pause, timestamp):
    if not in_pause:
        pygame.mixer_music.load('songs_audio/' + music[num] + '.mp3')
        pygame.mixer_music.play()
    else:
        pygame.mixer_music.play(start = timestamp)


def player_status(num):
    artist_name = music[num][:music[num].find('-') - 1]
    song_name = music[num][music[num].find('-') + 2:]

    font = pygame.font.SysFont('Verdana', 20)
    song_name_result = font.render(song_name, True, (255, 255, 255))
    screen.blit(song_name_result, (10, 410))

    font = pygame.font.SysFont('Verdana', 16)
    artist_name_result = font.render(artist_name, True, (255, 255, 255))
    screen.blit(artist_name_result, (10, 433))

    try:
        album_cover = pygame.transform.scale(pygame.image.load('songs_images/' + music[num] + '.jpg'), (300, 300))
    except FileNotFoundError:
        album_cover = pygame.transform.scale(pygame.image.load('songs_images/' + music[num] + '.png'), (300, 300))
    screen.blit(album_cover, (50, 70))
    
    ramka = pygame.transform.scale(pygame.image.load('player_images/vec.png'), (325, 325))
    screen.blit(ramka, (35, 55))

    pygame.draw.rect(screen, (255, 255, 255), (47, 67, 303, 303), 5)

start = 0

def game():
    running = True
    is_playing = False
    n_of_track = 1
    paused = False
    time_stamp = int()
    last_time_stamp = 0

    while running:
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (25, 25, 25), (0, 470, 400, 400))
        
        global start
        
        if start == 0: player_status(1)
        else:
            screen.blit(background, (0, 0))
            pygame.draw.rect(screen, (25, 25, 25), (0, 470, 400, 400))

        if is_playing:
            play_button = screen.blit(pause_button_img, (165, 490))
        else:
            play_button = screen.blit(play_button_img, (165, 487))

        next_button = screen.blit(next_button_img, (265, 500))
        prev_button = screen.blit(prev_button_img, (85, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                start = 1
                x, y = event.pos
                if play_button.collidepoint(x, y):
                    if is_playing:
                        is_playing = False
                        paused = True
                        pygame.mixer.music.stop()
                    else:
                        player(n_of_track, paused, time_stamp + last_time_stamp)
                        is_playing = True
                        last_time_stamp = time_stamp
                        start_ticks = pygame.time.get_ticks()
                elif next_button.collidepoint(x, y):
                    last_time_stamp = 0
                    is_playing = True
                    paused = False
                    n_of_track += 1
                    while n_of_track > len(music): n_of_track -= len(music)
                    player(n_of_track, paused, time_stamp + last_time_stamp)
                    start_ticks = pygame.time.get_ticks()
                elif prev_button.collidepoint(x, y):
                    last_time_stamp = 0
                    is_playing = True
                    paused = False
                    n_of_track -= 1
                    while n_of_track < 1: n_of_track = len(music)
                    player(n_of_track, paused, time_stamp + last_time_stamp)
                    start_ticks = pygame.time.get_ticks()

        if is_playing: time_stamp = (pygame.time.get_ticks() - start_ticks) / 1000


        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 471), 3)
        pygame.draw.rect(screen, (0, 0, 0), (0, 470, 400, 597), 3)
        
        passed_time = min(394 * (last_time_stamp + time_stamp) / music_len[n_of_track], 394)
        pygame.draw.rect(screen, (63, 186, 255), (3, 468, passed_time, 5))

        if is_playing or paused: player_status(n_of_track)

        pygame.display.flip()
        clock.tick(FPS)

game()
pygame.quit()