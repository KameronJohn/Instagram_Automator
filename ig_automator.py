from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import webbrowser
import os
import pyperclip

class ig:
    new_conf=0.7
    tag_list=[]
    new_list=[]
    times = 0
    fdd_list = ['@ac1', '@ac2 ', '@ac3', '@ac4', '@ac5', '@ac6']
    random.shuffle(fdd_list)
    removed3 = ""
    def __init__(self):
        self.new_conf = new_conf
        self.tag_list = tag_list
        self.new_list = new_list
        self.times = times
        self.n_times = n_times
        self.removed = removed

    def click():
        win32api.mouse_event(win32con.MOUSEE2VENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def tagging1():
        removed = ig.fdd_list.pop(0)
        pyautogui.write(f'{removed} ')
        ig.fdd_list.append(removed)
        # print(f'{ig.n_times+1} tagged')
        pyautogui.press('alt') #clear bug
        if ig.times >= 6:
            ig.times = 0
            random.shuffle(ig.fdd_list)
            print('times has been reseted')
        else:
            pass
    def tagging2():
        removed = ig.fdd_list.pop(0)
        pyautogui.write(f'{removed} ')
        ig.fdd_list.append(removed)

        removed = ig.fdd_list.pop(0)
        pyautogui.write(f'{removed} ')
        ig.fdd_list.append(removed)

        pyautogui.press('alt') #clear bug
        if ig.times >= 3:
            ig.times = 0
            random.shuffle(ig.fdd_list)
            print('times has been reseted')
        else:
            pass
    def tagging3():
        for i in range(3):
            removed = ig.fdd_list.pop(0)
            ig.fdd_list.append(removed)
            pyautogui.write(f'{removed} ')
        pyautogui.press('alt') #clear bug
        if ig.times >= 2:
            ig.times = 0
            random.shuffle(ig.fdd_list)
            print('times has been reseted')
        else:
            pass
    def tag(num):
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen('cls.png', region = (500,0,1500,1450), confidence=ig.new_conf)
                if x is not None:
                    pyautogui.moveTo(x-50, y)
                    time.sleep(0.1)
                    click()
                    pyautogui.moveTo(x, y)
                    time.sleep(0.1)
                    click()
                    time.sleep(0.7)
                    if num == 1:
                        if ig.full_auto:
                            for i in range(6):
                                ig.times += 1
                                ig.tagging1()
                                if ig.comment:
                                    pyautogui.hotkey('win', 'v', delay=0.25) #clipboard
                                    pyautogui.press('enter')
                                pyautogui.press('enter')
                        else:
                            ig.tagging1()
                    elif num == 2:
                        if ig.full_auto:
                            for i in range(3):
                                ig.times += 1
                                ig.tagging2()
                                if ig.comment:
                                    pyautogui.hotkey('win', 'v', delay=0.25)
                                    pyautogui.press('enter')
                                pyautogui.press('enter')
                        else:
                            ig.tagging2()
                    elif num == 3:
                        if ig.full_auto:
                            for i in range(2):
                                ig.times += 1
                                ig.tagging3()
                                if ig.comment:
                                    pyautogui.hotkey('win', 'v', delay=0.25)
                                    pyautogui.press('enter')
                                pyautogui.press('enter')
                        else:
                            ig.tagging3()
                    break
            except:
                time.sleep(0.1)
                print('nope')
    def step1():
        theinitialpos = pyautogui.position()
        click()
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('copy1.png', region = (1565,65,50,50), grayscale=True, confidence=ig.new_conf) #exact location
                if start3 is not None:
                    time.sleep(0.5)
                    pyautogui.moveTo(1589, 85)
                    click()
                    break
            except:
                time.sleep(0.1)
        time.sleep(0.4)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('copy2.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if start3 is not None:
                    time.sleep(0.5)
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.6)
                    a = pyperclip.paste()
                    ig.tag_list.append(a)
                    ig.new_list = [s.replace("https://instagram.com/", "") for s in ig.tag_list]
                    ig.new_list = [s.replace("?utm_medium=copy_link", "") for s in ig.new_list]
                    print(f'Tagging: {ig.new_list}')
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('profile_page.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if start3 is not None:
                    break
            except:
                pass
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('follow.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    pyautogui.moveTo(x=1934, y=389)
                    click()
                    while True:
                        try:
                            start3 = pyautogui.locateCenterOnScreen('following.png', region = (500,240,1500,350), grayscale=True, confidence=ig.new_conf)
                            if start3 is not None:
                                pyautogui.moveTo(start3)
                                click()
                                break
                        except:
                            time.sleep(0.25) 
                    time.sleep(0.5)
                    pyautogui.moveTo(x=876, y=1281)
                    click()
                    time.sleep(0.5)
                    pyautogui.moveTo(x=1587, y=1163)
                    click()
                    pyautogui.moveTo(x=1586, y=1221)
                    click()
                    time.sleep(0.2)
                    while True:
                        try:
                            start3 = pyautogui.locateCenterOnScreen('back.png', region = (500,1000,1500,700), grayscale=True, confidence=ig.new_conf) #exact location
                            if start3 is not None:
                                time.sleep(0.5)
                                pyautogui.moveTo(start3)
                                click()
                                break
                        except:
                            time.sleep(0.1)
                    time.sleep(0.4)
                    pyautogui.press('esc')  
                    x,y = theinitialpos
                    pyautogui.moveTo(x+100,y)
                    break
                else:
                    break
            except:
                pass
        time.sleep(0.75)
        pyautogui.press('esc')     
        x,y = theinitialpos
        pyautogui.moveTo(x+100,y)
        pyautogui.press('alt') #clear bug
    def step2():
        ig.step1()
        time.sleep(1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('01.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.5)
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('addposttoyourstory.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(1)
                    break
            except:
                time.sleep(0.1)
            try:
                start3 = pyautogui.locateCenterOnScreen('addvideotoyourstory.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(1)
                    break
            except:
                time.sleep(0.1)
                # print('cant find: addposttoyourstory')


        pyautogui.moveTo(1314, 82)
        time.sleep(0.2)
        click()
        time.sleep(0.3)
        pyautogui.screenshot('my_screenshot.png', region = (820,955,100,100))
        for i in ig.new_list:
            i = '@'+i
            pyautogui.write(i)
            pyautogui.moveTo(x=615, y=757)
            click()
            time.sleep(0.2)
            while True:
                try:
                    startt = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (820,955,130,130), grayscale=True, confidence=ig.new_conf)
                    if startt is None:
                        pyautogui.moveTo(x=879, y=993)
                        time.sleep(0.2)
                        while True:
                            click()
                            startt = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (820,955,130,130), grayscale=True, confidence=ig.new_conf)
                            if startt is not None:
                                break
                            else:
                                print('clicked')
                        pyautogui.press('alt') #clear bug
                        break
                except:
                    time.sleep(0.1)

            time.sleep(0.5)
            pyautogui.press('enter')
        time.sleep(0.5)

                                                    #font size
        fontsize = random.randint(425, 520)
        pyautogui.moveTo(840, fontsize)
        time.sleep(0.2)
        click()
                                                    #font location
        pyautogui.moveTo(1547, 75) #done
        click()
        time.sleep(0.2)
        pyautogui.moveTo(1225, 720)
        time.sleep(0.1)
        height = random.randint(100, 200)
        x_axis = random.randint(1100, 1300)
        pyautogui.dragTo(x_axis, height, 0.5, button='left')
        pyautogui.moveTo(1020,1396)  # post
        time.sleep(0.2)
        click()
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('esc')
        ig.tag_list = []
        ig.new_list = []
        print('Cleared')
        pyautogui.press('alt') #clear bug
    def copy_post_link():
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('copy1.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf) #exact location
                if start3 is not None:
                    time.sleep(0.5)
                    pyautogui.moveTo(start3)
                    click()
                    break
            except:
                time.sleep(0.1)
        time.sleep(0.4)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('copy_link.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if start3 is not None:
                    time.sleep(0.5)
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.5)
                    break
            except:
                time.sleep(0.25)
        a = str(pyperclip.paste())
        time.sleep(0.2)
        webbrowser.open(a)


    def ig_automator(full_auto=False, comment=False):
        ig.full_auto = full_auto
        ig.comment = comment
        time.sleep(0.5)
        if (ig.full_auto is False) or (ig.full_auto is False):
            print('BASIC.ig is running')
        else:
            print('\U0001F6A8\U0001F6A8\U0001F6A8 AUTO COMMENT.ig is initiated \U0001F6A8\U0001F6A8\U0001F6A8')
            time.sleep(0.2)
            print('Commenting:\U0001F7E1',pyperclip.paste(),'\U0001F7E1')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('press 1/2/3 if you wish to continue')

        while True:
            if keyboard.is_pressed('1'):
                ig.tag(1)
                pyautogui.press('alt') #clear bug
                return()
            if keyboard.is_pressed('2'):
                ig.tag(2)
                pyautogui.press('alt') #clear bug
                return()
            if keyboard.is_pressed('3'):
                ig.tag(3)
                pyautogui.press('alt') #clear bug
                return()
            if keyboard.is_pressed('q'):
                ig.ig_automator(ig.step1())
                pyautogui.press('alt') #clear bug
                # print(f"prog3 done")
            if keyboard.is_pressed('w'):
                ig.ig_automator(ig.step2())
                pyautogui.press('alt') #clear bug
                # print(f"prog4 done")
                return()
    def liker(num, comment=False):
        count = 0
        if comment == 'y':
            print ('Liker is initiated...')
            print('This prog is running for\U0001F7E1', num, '\U0001F7E1times')
            time.sleep(0.2)
            print('Commenting:\U0001F7E1',pyperclip.paste(),'\U0001F7E1')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('press 1 if you wish to continue')
            while True:
                if keyboard.is_pressed('1'):
                    break
        while True:
            try:
                time.sleep(0.3)
                x, y = pyautogui.locateCenterOnScreen('cls.png', region = (500,0,1500,1450), grayscale=True, confidence=ig.new_conf)
                if x is not None:
                    pyautogui.moveTo(x-50, y)
                    time.sleep(0.2)
                    if pyautogui.pixelMatchesColor(pyautogui.position().x, pyautogui.position().y, (237,73,86), tolerance=10): #scroll
                        pyautogui.moveTo(x=1220, y=1350)
                        time.sleep(0.1)
                        pyautogui.dragTo(1220, 0, 0.33, button='left')
                    else:
                        click()
                        # print(x, y)
                        if comment == 'y':
                            time.sleep(0.1)
                            pyautogui.moveTo(x, y)
                            time.sleep(0.1)
                            click()
                            time.sleep(0.1)
                            pyautogui.hotkey('win', 'v', delay=0.25) #clipboard
                            pyautogui.press('enter')
                            pyautogui.press('enter')
                            pyautogui.press('esc')
                            pyautogui.press('esc')
                        else:
                            time.sleep(0.3)
                        count += 1
                        print('liked x', count)
                        if count >=num:
                            return() 
                else:
                    pass
            except:
                pyautogui.moveTo(x=1220, y=859)
                time.sleep(0.1)
                pyautogui.dragTo(1220, 58, 0.5, button='left')
                time.sleep(0.3)
                # print('scrolled2')

    def mute ():
        print('ig.mute is running1')
        while True:
            if keyboard.is_pressed('1'):
                a = pyautogui.position()
                pyautogui.moveTo(x=1934, y=389)
                click()
                while True:
                    try:
                        start3 = pyautogui.locateCenterOnScreen('following.png', region = (500,240,1500,350), grayscale=True, confidence=ig.new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            break
                    except:
                        time.sleep(0.25)
                time.sleep(0.5)
                pyautogui.moveTo(x=876, y=1281)
                click()
                time.sleep(0.5)
                pyautogui.moveTo(x=1587, y=1163)
                click()
                pyautogui.moveTo(x=1586, y=1221)
                click()
                time.sleep(0.2)
                pyautogui.press('esc')
                time.sleep(0.4)
                pyautogui.press('esc')
                time.sleep(0.2)
                pyautogui.press('esc')
                pyautogui.moveTo(a)
    def unfollow(times):
        del_count = 0
        while True:
            try:
              x, y = pyautogui.locateCenterOnScreen('following2.png', region = (0,0,2500,1450), grayscale=True, confidence=0.9)
              if x is not None:
                  print('found')
                  pyautogui.moveTo(x, y)
                  # time.sleep(0.1)
                  click()
                  del_count +=1
                  if del_count >= times:
                    return() 
              else:
                  print('cant')
            except:
              print('nope')



print('running...')
while True:
    if keyboard.is_pressed('1'):
        ig.ig_automator()
        print('=   =   =   =   =   =   =prog1 done=   =   =   =   =   =   =')
    if keyboard.is_pressed('2'):
        ig.ig_automator(full_auto='y', comment='y')
        print(f"=   =   =   =   =   =   =prog2 done=   =   =   =   =   =   =")
    if keyboard.is_pressed('q'):
        ig.step1()
        pyautogui.press('alt') #clear buqg
        print(f"=   =   =   =   =   =   =prog3 done=   =   =   =   =   =   =")
    if keyboard.is_pressed('w'):
        ig.step2()
        pyautogui.press('alt') #clear bug
        print(f"=   =   =   =   =   =   =prog4 done=   =   =   =   =   =   =")
    if keyboard.is_pressed('e'):
        ig.copy_post_link()
        pyautogui.press('alt') #clear bug
        print(f"=   =   =   =   =   =   =prog5 done=   =   =   =   =   =   =")
    if keyboard.is_pressed('r'):
        ig.liker(6, comment='n')
        pyautogui.press('alt') #clear bug
        print(f"=   =   =   =   =   =   =prog6 done=   =   =   =   =   =   =")
    if keyboard.is_pressed('\\'):
        ig.unfollow()
