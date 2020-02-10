import pygame
import os
import webbrowser
import time

def load_image(name, colorkey=None): 
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    return image

def txt_to_sc(screen, text, x, y, size = 20, color = (0, 0, 0)):
    text = str(text)
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
        
    
curs = load_image("ground.jpg")
curs = pygame.transform.scale(curs, (20, 20))    
curs1 = load_image("straight1.png")
curs1 = pygame.transform.scale(curs1, (20, 20))
curs2 = load_image('ug_00.png')
curs2 = pygame.transform.scale(curs2, (20, 20))
curs3 = load_image('kran.png')
curs3 = pygame.transform.scale(curs3, (20, 20))
curs4 = load_image('center1.png')
curs4 = pygame.transform.scale(curs4, (20, 20))
cursors = [curs, curs1, curs2, curs3, curs3, curs4]

background = load_image("backgroundnew.png")
start_button = load_image("start.jpg")
start_button = pygame.transform.scale(start_button, ( 143 * 3, 43 * 3))
count_button = load_image("count_button.png")
count_button = pygame.transform.scale(count_button, ( 400, 200))
truba = load_image('ground.jpg')
trubaex = load_image('ground.jpg')
trubaex = pygame.transform.scale(trubaex, (100, 100))
straight = load_image('straight.png')
straightex = load_image('straight.png')
straightex = pygame.transform.scale(straightex, (100, 100))
angle = load_image('ug_0.png')
angleex = load_image('ug_0.png')
angleex = pygame.transform.scale(angleex, (100, 100))
back = load_image('back.png')
back = pygame.transform.scale(back, (100, 100))
kist = load_image('kist.png')
kist = pygame.transform.scale(kist, (100, 100))
zaliv = load_image('zaliv.png')
zaliv = pygame.transform.scale(zaliv, (113, 100))
kran = load_image('kran.png')
kranright = load_image('kranright.png')
kranex = load_image('kran.png')
kranex = pygame.transform.scale(kranex, (100, 100))
next_ = load_image('next.png')
next_ = pygame.transform.scale(next_, (150, 100))
loading = load_image('loading.jpg')
loading = pygame.transform.scale(loading, (1600, 900))
shit = load_image('shit.jpg')
shit = pygame.transform.scale(shit, (1000, 1000))
ground = load_image("ground.jpg")
ground = pygame.transform.scale(ground, (1200, 800))
center = load_image('center.png')
center1 = load_image('center1.png')
centerex = load_image('center.png')
centerex = pygame.transform.scale(centerex, (100, 100))

straight1 = load_image('straight1.png')
straight2 = load_image('straight2.png')
angle1 = load_image('ug_00.png')
angle2 = load_image('ug_90.png')
angle3 = load_image('ug_180.png')
angle4 = load_image('ug_270.png')


pygame.init()
width, height = 1600, 1000
size = width, height
screen = pygame.display.set_mode(size)
co1 = 3
co2 = 3
l1 = 0
r1 = 0
last = 0

running = True
answering = 0

curs_flag = 0
check_mas = [[], [], []]

#ini
#stage 1.337
check_mas[0].append([0, 1100, 800, 1100 + 143*3, 800 + 43 * 3])
check_mas[0].append([1, 600, 330, 85])
check_mas[0].append([1, 800, 330, 85])
check_mas[0].append([1, 600, 630, 85])
check_mas[0].append([1, 800, 630, 85])

#stage 2.28

check_mas[1].append([1, 100, 920, 50])
check_mas[1].append([0, 25, 250, 125, 350])
check_mas[1].append([0, 40, 400, 140, 500])
check_mas[1].append([0, 40, 600, 140, 700])

check_mas[1].append([0, 1425, 250, 1525, 350])
check_mas[1].append([0, 1440, 430, 1540, 530])
check_mas[1].append([0, 1440, 600, 1540, 700])
check_mas[1].append([0, 1440, 770, 1540, 870])
check_mas[1].append([0, 1150, 890, 1300, 990])
check_mas[1].append([0, 1440, 130, 1540, 230])
check_mas[1].append([0, 40, 130, 140, 230])



#stage 3

check_mas[2].append([1, 100, 920, 50])

#ini

def check(ev, x, y):
    for i in range(len(check_mas[ev])):
        if (check_mas[ev][i][0] == 0):
            if (check_mas[ev][i][1] <= x <= check_mas[ev][i][3] and check_mas[ev][i][2] <= y <= check_mas[ev][i][4]):
                return i
        else:
            if ((check_mas[ev][i][1] - x)**2 +  (check_mas[ev][i][2] - y)**2 <= check_mas[ev][i][3]**2):
                return i

def draw_counters():
    global co1, co2
    text1 = 'width: {}'.format(co1)
    text2 = 'height: {}'.format(co2)   
    txt_to_sc(screen, text1, 100, 300, 100)   
    txt_to_sc(screen, text2, 100, 600, 100)
    screen.blit(count_button, (500, 230))
    screen.blit(count_button, (500, 530))
    
def draw_choice():
    screen.blit(zaliv, (35, 0))
    screen.blit(centerex, (40, 130))
    txt_to_sc(screen, 'Не без урода', 10, 235, 40)  
    screen.blit(angleex, (25, 250))
    txt_to_sc(screen, 'Угол', 50, 360, 40)
    screen.blit(straightex, (40, 400))
    txt_to_sc(screen, 'Прямая труба', 10, 480, 40)
    screen.blit(trubaex, (40, 600))   
    txt_to_sc(screen, 'Стена', 50, 710, 40)
    
    screen.blit(kist, (1450, 10))
    screen.blit(centerex, (1440, 130))
    txt_to_sc(screen, 'Не без урода', 1410, 235, 40)    
    screen.blit(angleex, (1425, 250))
    txt_to_sc(screen, 'Угол', 1450, 360, 40)
    screen.blit(straightex, (1440, 430))
    txt_to_sc(screen, 'Прямая труба', 1410, 510, 40)
    screen.blit(trubaex, (1440, 600))   
    txt_to_sc(screen, 'Стена', 1450, 710, 40)
    
    screen.blit(kranex, (1440, 770))   
    txt_to_sc(screen, 'Кран', 1450, 860, 40)
    

    
class graph():
    def __init__(self, w, h):
        global truba, straight, angle, kran, kranright, straight1, angle1, angle2, angle3, angle4, straight2, center, center1
        self.w = w
        self.h = h
        self.width = 1200//w * w
        self.height = 800//h * h
        self.size = (1200//w, 800//h)
        
        #us
        truba = pygame.transform.scale(truba, self.size)
        straight = pygame.transform.scale(straight, self.size)
        center = pygame.transform.scale(center, self.size)
        center1 = pygame.transform.scale(center1, self.size)        
        angle = pygame.transform.scale(angle, self.size)
        kran = pygame.transform.scale(kran, self.size)
        kranright = pygame.transform.scale(kranright, self.size)
        
        #ans
        straight2 = pygame.transform.scale(straight2, self.size)
        straight1 = pygame.transform.scale(straight1, self.size)
        angle1 = pygame.transform.scale(angle1, self.size)
        angle2 = pygame.transform.scale(angle2, self.size)
        angle3 = pygame.transform.scale(angle3, self.size)
        angle4 = pygame.transform.scale(angle4, self.size)
        
        self.fill(0)
        
    
    def fill(self, num):
        self.grr = [[num] for i in range(self.w * self.h)]
        global l1, r1
        l1 = 0
        r1 = 0
        
    def draw_lines(self):
        for i in range(self.h + 1):
            pygame.draw.line(screen, (200, 255, 255), [200, 80 + self.size[1] * i], [200 + self.width, 80 + self.size[1] * i], 3)
        for i in range(self.w + 1):
            pygame.draw.line(screen, (200, 255, 255), [200 + self.size[0] * i, 80], [200 + self.size[0] * i, 80 + self.height], 3)
            
    def get_coords(self, num):
        x1 = num//self.w
        y1 = num%self.w
        return (200 + self.size[0] * y1, 80 + self.size[1] * x1)

    def get_num(self, x, y):
        x -= 200
        y -= 80
        x1 = x//self.size[0]
        y1 = y//self.size[1]
        return y1 * self.w + x1
        
    def get_image(self, num):
        if num == 0:
            return truba
        elif num == 1:
            return straight
        elif num == 2:
            return angle
        elif num == 3:
            return kran
        elif num == 4:
            return kranright
        elif num == 5:
            return truba
        elif num == 6:
            return straight1
        elif num == 7:
            return angle1
        elif num == 8:
            return angle2
        elif num == 9:
            return angle3
        elif num == 10:
            return angle4   
        elif num == 11:
            return straight2
        elif num == 12:
            return center
        elif num == 13:
            return center1
                     
    def draw_elems(self):
        for i in range(self.w * self.h):
            if len(self.grr[i]) == 1 or time.time() - self.time < self.grr[i][2]/5:
                screen.blit(truba, gr.get_coords(i))
                screen.blit(self.get_image(self.grr[i][0]), gr.get_coords(i))
            else:
                screen.blit(truba, gr.get_coords(i))
                screen.blit(self.get_image(self.grr[i][1]), gr.get_coords(i))
    
    
def process():
    a = open('input.txt', 'w')
    b = open('output.txt', 'w')
    b.close()
    a.write(str(gr.w) + " " + str(gr.h) + ' ')
    for i in gr.grr:
        a.write(str(i[0]) + ' ')
    a.close()
    screen.fill((255, 255, 255))
    screen.blit(background, (1400, 900))
    screen.blit(loading, (0, 0))    
    os.system('solution.exe')
    
def process_answer(answer):
    try:
        answer = list(map(int, answer.split()))
        le = len(answer)
        for i in range(1, le - 1):
            now = answer[i]
            cl = gr.grr[now][0]
            if cl == 1:
                if abs(now - answer[i + 1]) == 1:
                    gr.grr[now].append(6) 
                    gr.grr[now].append(i) 
                else:
                    gr.grr[now].append(11) 
                    gr.grr[now].append(i) 
            elif cl == 2:
                pred = answer[i - 1]
                nex = answer[i + 1]
                ch1 = [pred, nex]
                j = 0
                for _ in range(2):
                    if (abs(now - ch1[_]) == 1):
                        j = now - ch1[_]
                        del ch1[_]
                        break
                if j == -1 and ch1[0] < now:
                    gr.grr[now].append(10) 
                    gr.grr[now].append(i) 
                elif j == -1 and ch1[0] > now:
                    gr.grr[now].append(7) 
                    gr.grr[now].append(i) 
                elif j == 1 and ch1[0] < now:
                    gr.grr[now].append(9) 
                    gr.grr[now].append(i) 
                elif j == 1 and ch1[0] > now:
                    gr.grr[now].append(8) 
                    gr.grr[now].append(i) 
            else:
                gr.grr[now].append(13) 
                gr.grr[now].append(i)                 
        gr.time = time.time() 
    except:
        pass
    
def check_file():
    a = open('output.txt', 'r').read()
    if a == '' or '-1' in a:
        return 0
    return a
    
while running:
    if answering == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                f = check(1, x, y)
                if f == 0:
                    answering = 0
                elif f == 1:
                    gr.fill(2)
                elif f == 2:
                    gr.fill(1)
                elif f == 3:
                    gr.fill(0)
                elif f == 4:
                    curs_flag = 2
                elif f == 5:
                    curs_flag = 1
                elif f == 6:
                    curs_flag = 0
                elif f == 7:
                    curs_flag = 3
                elif f == 8 and l1 + r1 == 2:
                    answering = 2
                    process()
                elif f == 9:
                    curs_flag = 5
                elif f == 10:
                    gr.fill(12)
                elif 200 <= x <= gr.width + 200 and 80 <= y <= gr.height + 80:
                    e = gr.get_num(x, y)
                    if curs_flag == 3:
                        if e % gr.w == 0 and l1 == 0:
                            gr.grr[e][0] = curs_flag
                            l1 = 1
                        elif (e + 1) % gr.w == 0 and r1 == 0:
                            gr.grr[e][0] = curs_flag + 1
                            r1 = 1
                    else:
                        if gr.grr[e][0] == 3:
                            l1 -= 1
                        elif gr.grr[e][0] == 4:
                            r1 -= 1
                        if curs_flag == 5:
                            gr.grr[e][0] = 12
                        else:
                            gr.grr[e][0] = curs_flag
                    
            if event.type == pygame.KEYDOWN:
                if event.scancode == 33:
                    try:
                        webbrowser.open_new('https://money.yandex.ru/to/410014391030188')  
                    except:
                        pass
        screen.fill((255, 255, 255))
        screen.blit(background, (1400, 900))
        txt_to_sc(screen, 'Занесите уровень', 500, 0, 100)
        screen.blit(back, (50, 870))
        gr.draw_elems()
        gr.draw_lines()
        draw_choice()   
        screen.blit(next_, (1150, 890)) 
        if pygame.mouse.get_focused() == 1:
            screen.blit(cursors[curs_flag], (pygame.mouse.get_pos()[0] + 5, pygame.mouse.get_pos()[1] + 15))
        
        pygame.display.flip()
        
        
    elif answering == 2:      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False       
            
            if event.type == pygame.KEYDOWN:
                if event.scancode == 33:
                    try:
                        webbrowser.open_new('https://money.yandex.ru/to/410014391030188')  
                    except:
                        pass
        if last == 0:
            last = time.time() 
        if (time.time() - last > 0.5):
            k = check_file()
            if check_file() != 0:
                process_answer(k)
                answering = 5
                last = 0
        if last != 0 and time.time() - last >= 10:
            answering = 4
        screen.fill((255, 255, 255))
        screen.blit(background, (1400, 900))
        screen.blit(loading, (0, 0))
        pygame.display.flip()  
        
        
    elif answering == 4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False       
            if event.type == pygame.KEYDOWN:
                if event.scancode == 33:
                    try:
                        webbrowser.open_new('https://money.yandex.ru/to/410014391030188')  
                    except:
                        pass
        screen.fill((255, 255, 255))
        screen.blit(shit, (0, 0))
        screen.blit(background, (1400, 900))
        txt_to_sc(screen, 'Shit happened', 1050, 300, 80)
        txt_to_sc(screen, 'Try to reboot', 1050, 500, 80)
        txt_to_sc(screen, '(or no solution)', 1050, 600, 30)
          
        pygame.display.flip()     
        
        
    elif answering == 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False      
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                f = check(2, x, y)
                if f == 0:
                    answering = 0
            if event.type == pygame.KEYDOWN:
                if event.scancode == 33:
                    try:
                        webbrowser.open_new('https://money.yandex.ru/to/410014391030188')  
                    except:
                        pass
        screen.fill((255, 255, 255))
        txt_to_sc(screen, 'Ответ убил', 500, 0, 100)
        screen.blit(background, (1400, 900))
        screen.blit(back, (50, 870))
        gr.draw_elems()
        gr.draw_lines()       
        pygame.display.flip()           
        
    
    elif answering == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False       
            if event.type == pygame.KEYDOWN:
                if event.scancode == 33:
                    try:
                        webbrowser.open_new('https://money.yandex.ru/to/410014391030188')  
                    except:
                        pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                f = check(0, pos[0], pos[1])
                if f == 0:
                    answering = 1
                    gr = graph(co1, co2)
                elif f == 1:
                    co1 += 1
                    co1 %= 12
                    if co1 == 0:
                        co1 = 12
                    co1 = max(co1, 3)
                elif f == 2:
                    co1 -= 1
                    if co1 == 2:
                        co1 = 12
                elif f == 3:
                    co2 += 1
                    co2 %= 12
                    if co2 == 0:
                        co2 = 12                    
                    co2 = max(co2, 3)
                elif f == 4:
                    co2 -= 1
                    if co2 == 2:
                        co2 = 12    
        screen.fill((255, 255, 255))
        txt_to_sc(screen, 'МАМИН ВОДОПРОВОДЧИК', 300, 0, 100)
        txt_to_sc(screen, 'Выбирите параметры водопровода', 50, 150, 60)
        screen.blit(start_button, (1100, 800)) 
        screen.blit(background, (1400, 900))
        draw_counters() 
        pygame.display.flip()  
        
pygame.quit()
 