import pygame
import random
import glob
import os
import time

pygame.mixer.init()
pygame.init()

folder_path = str(os.getcwd())

body_parts_files = glob.glob(folder_path + '/files_en/categories/body parts/*.wav')
type_of_movement_files = glob.glob(folder_path + '/files_en/categories/type of movement/*.wav')
timing_files = glob.glob(folder_path + '/files_en/categories/timing/*.wav')
quality_of_movement_files = glob.glob(folder_path + '/files_en/categories/quality/*.wav')
space_files = glob.glob(folder_path + '/files_en/categories/space/*.wav')
technique_files = glob.glob(folder_path + '/files_en/categories/technique/*.wav')
figure_files = glob.glob(folder_path + '/files_en/categories/figure/*.wav')

jam_files = sorted(glob.glob(folder_path + '/jam/*.ogg'))


def input_combination():
    while True:
        try:
           combination = int(input('Enter the combination(1 — 7): '))
        except ValueError:
           print('Enter the number.')
           continue
        else:
           return list(str(combination))
           break

def input_time_delay():
    while True:
        try:
           time_delay = int(input('Enter a pause between repetitions: '))
        except ValueError:
           print('Enter the number.')
           continue
        else:
           return time_delay
           break

def input_repeat_number():
    while True:
        try:
           repeat_number = int(input('Enter the number of repetitions: '))
        except ValueError:
           print('Enter the number.')
           continue
        else:
           return repeat_number
           break


categories_list = ['body_parts_files', 'type_of_movement_files', 'timing_files', 'quality_of_movement_files',
'space_files', 'technique_files', 'figure_files']


def play_combination(combination):
    for i in range(0, len(combination)):
        combination_path =  random.choice(eval(categories_list[int(combination[i]) - 1]))
        play_combination = pygame.mixer.Sound(combination_path)
        play_combination.play()

        pronunciation_interval = pygame.mixer.Sound(play_combination).get_length()
        pause = int(1) # пауза между словами
        time.sleep(pronunciation_interval + pause)


def play_and_repeat_combination(time_delay):
    combination = input_combination()
    repeat_number = input_repeat_number()
    for _ in range(0, repeat_number):
        play_combination(combination)
        time_delay -= 1
        if time_delay < 1:
            time.sleep(1)
        else:
            time.sleep(time_delay)


def play_ready_steady_improvise():
    impro = pygame.mixer.Sound(folder_path + '/transition/ready.wav')
    impro.play()
    time.sleep(pygame.mixer.Sound(impro).get_length())

def play_scratch():
    scratch = pygame.mixer.Sound(folder_path + '/transition/scratch.ogg')
    scratch.play()
    time.sleep(pygame.mixer.Sound(scratch).get_length())

def play_jam():
    track = pygame.mixer.Sound(random.choice(jam_files))
    track_duration = pygame.mixer.Sound(track).get_length()
    print()
    print('Track duration:', time.strftime("%M:%S", time.gmtime(track_duration)))
    print()
    track.play()
    time.sleep(track_duration)


def main():
    while True:
        time_delay = input_time_delay()
        play_and_repeat_combination(time_delay)
        play_ready_steady_improvise()
        play_scratch()
        play_jam()


if __name__=='__main__':
    main()
