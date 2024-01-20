
# Modification date: Wed Jun 15 19:11:50 2022

# Production date: Sun Sep  3 15:44:21 2023

import pygame, sys, os
from random import choice, randint
from os import listdir, getcwd
from os.path import isfile, join
"""
yapılacaklar:
bir tuşa basınca listedeki sıradan müzik seçme fonksiyonu yapmak - bitti
müzik bitince müziği değiştir - bitti
müzik bulmak - bitti
müzik klasörünü çalışır hale getirmek - bitti
bütün resimleri vs bir klasörden aldırtmak - bitti
arka plan araba sesini başka klasöre al - bitti
arka plan araba sesine kapat/aç tuşu yap - bitti
Resul'e doğum günü notu hazırla - bitti
arkaplana bir de şehir yap belki - bitti
belki dönüşümlü ay-güneş
müzik sesleri çok fazla onu ayarla - bitti
"""
"""



Hoşgeldin homie



"""
mypath = os.getcwd() + "\\misc\\images\\"


pygame.init()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
#monitor_size = [600, 600]
#width, height = 600, 600
win = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)

class Text:
    def __init__(self, x, y, text, size, variable, speed = 0):
        self.x, self.y, self.size, self.speed = x, y, size, speed
        self.text = text
        self.variable = variable
        self.font = pygame.font.SysFont('Comic Sans MS', self.size)
        self.text_surface = self.font.render(self.text, False, (255, 0, 255))
        self.text_width = self.text_surface.get_width()

    def draw(self, win):
        if self.x + self.text_width > 0:
            self.text_surface1 = self.font.render(self.text + str(self.variable), False, (150, 123, 182))
            self.text_width = self.text_surface1.get_width()
            win.blit(self.text_surface1, (self.x + 2, self.y + 2))
            self.text_surface = self.font.render(self.text + str(self.variable), False, (255, 0, 255))
            self.text_width = self.text_surface1.get_width()
            win.blit(self.text_surface, (self.x, self.y))
            self.x -= self.speed
        return

da_text = Text((width/2) - 150, 10, "Müzikler yükleniyor...", 30, "", 0)
da_text.draw(win)
pygame.display.flip()



real_cycle = pygame.image.load(mypath + "cycle.png")
real_da_height = real_cycle.get_height()
current_height = real_da_height/2

car_day = pygame.image.load(mypath + "pixel_car.png")#73*22
car_night = pygame.image.load(mypath + "pixel_car_edit3 - Kopya (3).png")#"pixel_car_edit3.png")#73*22
palm_images = [pygame.image.load(mypath + "shadow_palm1edit.png"), pygame.image.load(mypath + "shadow_palm2edit.png"), pygame.image.load(mypath + "shadow_palm4edit.png"), pygame.image.load(mypath + "shadow_palm5edit.png"), pygame.image.load(mypath + "shadow_palm6edit.png")]

building_day = pygame.image.load(mypath + "building_day.png")#100*300, 14 per window
building_nights = [pygame.image.load(mypath + "building_night1.png"), pygame.image.load(mypath + "building_night2.png"), pygame.image.load(mypath + "building_night3.png"), pygame.image.load(mypath + "building_night4.png")]#100*300
building_nightsr = [pygame.image.load(mypath + "building_night1r.png"), pygame.image.load(mypath + "building_night2r.png"), pygame.image.load(mypath + "building_night3r.png"), pygame.image.load(mypath + "building_night4r.png")]

da_river = pygame.image.load(mypath + "river.png")
da_river_day2 = pygame.image.load(mypath + "river_day2.png")
da_river_day = pygame.image.load(mypath + "river_day.png")

plane_img = pygame.image.load(mypath + "plane.png")

pygame.display.set_icon(pygame.image.load(mypath + "icon.png"))
pygame.display.set_caption("Vibe check")

mypath = os.getcwd() + "\\misc\\car sound\\"
car_sound = pygame.mixer.Sound(mypath + "Binaural ASMR Car Ride For Relaxation and Sleeping  - No Talking.mp3")
car_sound.set_volume(0.2)
#music = pygame.mixer.Sound("the-weeknd-blinding-lights-80s-remix.mp3")
#music.set_volume(20)


mypath = os.getcwd() + "\\misc\\music"
music_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in range(len(music_list)):
    music_list[i] = pygame.mixer.Sound(mypath + "\\" + music_list[i])
music_names = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in range(len(music_names)):
    music_names[i] = music_names[i][:-4]
print("Müzik listesi:")
for music in music_names:
    print(music)
index = 0
music = music_list[index]
#music.set_volume(20)
for i in range(len(music_list)):
    music_list[i].set_volume(0.3)

platform_height = height/10



class Plane:
    def __init__(self, width, heigth, speed, img):
        self.x = width * randint(10, 30)
        self.y = randint(height//20, height//10)
        self.speed = speed
        self.img = img
    def move(self, width, height):
        self.x -= self.speed
        if self.x < -62:
            self.x = width * randint(10, 30)
            self.y = randint(height//20, height//10)
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class Building:
    def __init__(self, day, nights, nightsr, speed, width, height):
        self.x = width
        self.day = day
        self.nn = randint(0, len(nights) - 1)
        self.night = nights[self.nn]
        self.nightr = nightsr[self.nn]
        num = choice([0, 14, 28, 42])
        self.y = height - platform_height - 165 - 300 + num
        self.yr = height - platform_height - 165  + 50 - num
        self.speed = speed
    def move(self, height, nights, nightsr):
        self.x -= self.speed
        if self.x < -100:
            self.x = width
            self.nn = randint(0, len(nights) - 1)
            self.night = nights[self.nn]
            self.nightr = nightsr[self.nn]
            num = choice([0, 14, 28, 42])
            self.y = height - platform_height - 165 - 300 + num
            self.yr = height - platform_height - 165  + 50 - num
    def draw(self, win, da_height):
        if current_height < -real_da_height/2:#day
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x, self.y, 100, 600 - self.nn * 2))
            #win.blit(self.day, (self.x, self.y))
            #win.blit(self.day, (self.x, self.yr))
        else:
            win.blit(self.night, (self.x, self.y))
            win.blit(self.nightr, (self.x, self.yr))
            


class Palm:
    def __init__(self, images, speed, width, height):
        self.x = width
        self.images = images
        self.image = choice(images)
        self.y = height - (self.image.get_height()/4)*3
        self.speed = speed
    def move(self, height):
        self.x -= self.speed
        if self.x < -150:
            self.x = width
            self.image = choice(self.images)
            self.y = height - (self.image.get_height()/4)*3
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

car_speed = 10

buildings = []
for i in range(((width + 100)//100) + 1):
    buildings.append(Building(building_day, building_nights, building_nightsr, 1, (i * 100) + randint(0, 10), height))

palms = []
for i in range(6):
    palms.append(Palm(palm_images, car_speed, (((width + 150)/6)*(i + 1)), platform_height * 9))

da_plane = Plane(width, height, 3, plane_img)

turn = 2#turn1 = down, turn2 = up (image going _____)
speed = 1
counter = 0
limit = 1
current_height = 0

def da_cycle(turn, speed, counter, limit, cycle, current_height, monitor_size, da_height):
    counter += 1
    if counter >= limit:
        counter = 0
        if turn == 1:
            current_height -= speed
        else:
            current_height += speed
        if current_height >  0:
            turn = 1
            current_height = 0
        elif current_height < -da_height + monitor_size[1]:
            turn = 2
            current_height = -da_height + monitor_size[1]
        
    win.blit(cycle, (0, current_height))
        
    return turn, speed, counter, limit, current_height

def change_music_when_finished(channel2, music_list, music_names, music_text, width, index):
    if not channel2.get_busy():
        if index + 1 > len(music_list) - 1:
            index = 0
        else:
            index += 1
        channel2.play(music_list[index])
        music_text.variable = music_names[index]
        music_text.x = width + 30
        print(f"Şimdi çalıyor: {music_names[index]}")
    return index

def music_picker(music_list, music_names, music_text, width, index, direction):
    if direction == "right":
        if index + 1 > len(music_list) - 1:
            index = 0
        else:
            index += 1
    else:
        if index - 1 < 0:
            index = len(music_list) - 1
        else:
            index -= 1
    channel2.play(music_list[index])
    music_text.variable = music_names[index]
    music_text.x = width + 30
    print(f"Şimdi çalıyor: {music_names[index]}")
    return index

channel1 = pygame.mixer.Channel(0) 
channel2 = pygame.mixer.Channel(1)
channel1.play(car_sound, loops = -1)
channel2.play(music)
#car_sound.play(-1)
#music.play(-1)

music_text = Text(width + car_speed, height - platform_height, f"Şimdi çalıyor: ", int(platform_height/2), music_names[index], car_speed)

pygame.mouse.set_visible(False)
win = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)

clock = pygame.time.Clock()
fps = 60
running = True
while running:
    clock.tick(fps)
    #win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                index = music_picker(music_list, music_names, music_text, monitor_size[0], index, "right")
            if event.key == pygame.K_LEFT:
                index = music_picker(music_list, music_names, music_text, monitor_size[0], index, "left")
            if event.key == pygame.K_SPACE:
                if channel1.get_busy():
                    channel1.stop()
                elif not channel1.get_busy():
                    channel1.play(car_sound, loops = -1)

    turn, speed, counter, limit, current_height = da_cycle(turn, speed, counter, limit, real_cycle, current_height, monitor_size, real_da_height)#cycle(turn, speed, counter, limit, cycle1, cycle2, current_height, monitor_size, da_height)
    index = change_music_when_finished(channel2, music_list, music_names, music_text, monitor_size[0], index)

    #buildings
    da_plane.move(width, height)
    da_plane.draw(win)
    
    for building in buildings:
        building.move(height, building_nights, building_nightsr)
        building.draw(win, height)

    #print(buildings[0].x, buildings[0].y)
    #building platform
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, height - platform_height - 165, width, 50))

    #wa'er
    #if current_height < -real_da_height/3:
        #win.blit(da_river_day, (0, height - platform_height - 140))
    if current_height < -real_da_height/2:
        win.blit(da_river_day2, (0, height - platform_height - 140))
    else:
        win.blit(da_river, (0, height - platform_height - 140))

    for palm in palms:
        palm.move(platform_height * 9)
        palm.draw(win)
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, height - platform_height, width, platform_height + 10))
    if current_height < -real_da_height/2:
        win.blit(car_day, (width/10, height - platform_height - 21))
    else:
        win.blit(car_night, (width/10, height - platform_height - 21))

    music_text.draw(win)

    """
    da_fps = int(clock.get_fps())
    font = pygame.font.Font('freesansbold.ttf', 10)
    text = font.render(str(da_fps), 1, pygame.Color(200, 200, 200))
    win.blit(text, (10, 10))
    """
    
    pygame.display.flip()
