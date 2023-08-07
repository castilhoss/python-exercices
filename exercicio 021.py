import pygame, random

playlist = ['musica 1.mp3', 'musica 2.mp3', 'musica 3.mp3']

suffle = random.choice(playlist)

def play_music(musica):
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    pygame.event.wait()
    input()

def pause_music():
    pygame.mixer.music.pause()

def main():
    print("MP3 Coxinha + Kibe")
    print("-" * 5)
     
    while True:
        print("Digite 1 para começar a música")
        print("Digite 2 para pausar a música")
        print("Digite 3 para modo aleatório")
        print("Digite 4 para encerrar o mp3")

        menu = input("")

        if menu == "1":
            play_music(musica)
            musica = suffle
            print("Tocando Música")
        elif menu == "2":
            pause_music()
            print("Música Pausada")
        elif menu == "3":
            musica = suffle
            play_music(musica)
            print("Tocando em ordem aleatório")
        elif menu == "4":
            print("Tchau")
            break
        else:
            print("Comando indisponivel")

if __name__ == "__main__":
    main()
    