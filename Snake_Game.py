import random
import random
import time
import math
from tqdm import tqdm
import numpy as np
import pygame

def dis_sn(s_p, display):
    for pos in s_p:
        pygame.draw.rect(display, (255, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))


def dis_ap(a_p, display):
    pygame.draw.rect(display, (255, 0, 0), pygame.Rect(a_p[0], a_p[1], 10, 10))


def st_pos():
    s_st = [100, 100]
    s_pos = [[100, 100], [90, 100], [80, 100]]
    a_p = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
    sc = 0

    return s_st, s_pos, a_p, sc


def ap_dis_fr_sn(a_p, s_p):
    return np.linalg.norm(np.array(a_p) - np.array(s_p[0]))


def gen_sn(s_st, s_pos, a_p, bt_dir, sc):
    if bt_dir == 1:
        s_st[0] += 10
    elif bt_dir == 0:
        s_st[0] -= 10
    elif bt_dir == 2:
        s_st[1] += 10
    else:
        s_st[1] -= 10

    if s_st == a_p:
        a_p, sc = coll_ap(a_p, sc)
        s_pos.insert(0, list(s_st))

    else:
        s_pos.insert(0, list(s_st))
        s_pos.pop()

    return s_pos, a_p, sc


def coll_ap(a_p, sc):
    a_p = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
    sc += 1
    return a_p, sc


def coll_bnd(s_st):
    if s_st[0] >= 500 or s_st[0] < 0 or s_st[1] >= 500 or s_st[1] < 0:
        return 1
    else:
        return 0


def coll_sl(s_st, s_pos):
    if s_st in s_pos[1:]:
        return 1
    else:
        return 0


def bl_dir(s_pos):
    cur_d_v = np.array(s_pos[0]) - np.array(s_pos[1])

    l_d_v = np.array([cur_d_v[1], -cur_d_v[0]])
    r_d_v = np.array([-cur_d_v[1], cur_d_v[0]])

    i_f_b = is_dir_bl(s_pos, cur_d_v)
    i_l_b = is_dir_bl(s_pos, l_d_v)
    i_r_b = is_dir_bl(s_pos, r_d_v)

    return cur_d_v, i_f_b, i_l_b, i_r_b


def is_dir_bl(s_pos, cur_d_v):
    n_st = s_pos[0] + cur_d_v
    s_st = s_pos[0]
    if coll_bnd(n_st) == 1 or coll_sl(n_st.tolist(), s_pos) == 1:
        return 1
    else:
        return 0


def gen_rdm_dir(s_pos, a_w_app):
    direction = 0
    if a_w_app > 0:
        direction = 1
    elif a_w_app < 0:
        direction = -1
    else:
        direction = 0

    return dir_vec(s_pos, a_w_app, direction)


def dir_vec(s_pos, a_w_app, direction):
    cur_d_v = np.array(s_pos[0]) - np.array(s_pos[1])
    l_d_v = np.array([cur_d_v[1], -cur_d_v[0]])
    r_d_v = np.array([-cur_d_v[1], cur_d_v[0]])

    new_direction = cur_d_v

    if direction == -1:
        new_direction = l_d_v
    if direction == 1:
        new_direction = r_d_v

    bt_d = gen_btn_dir(new_direction)

    return direction, bt_d


def gen_btn_dir(new_direction):
    bt_d = 0
    if new_direction.tolist() == [10, 0]:
        bt_d = 1
    elif new_direction.tolist() == [-10, 0]:
        bt_d = 0
    elif new_direction.tolist() == [0, 10]:
        bt_d = 2
    else:
        bt_d = 3

    return bt_d


def ang_ap(s_pos, a_pos):
    a_d_v = np.array(a_pos) - np.array(s_pos[0])
    s_d_v = np.array(s_pos[0]) - np.array(s_pos[1])

    n_f_a_d_v = np.linalg.norm(a_d_v)
    n_f_s_d_v = np.linalg.norm(s_d_v)
    if n_f_a_d_v == 0:
        n_f_a_d_v = 10
    if n_f_s_d_v == 0:
        n_f_s_d_v = 10

    a_dir_v_n = a_d_v / n_f_a_d_v
    s_dir_v_n = s_d_v / n_f_s_d_v
    angle = math.atan2(
        a_dir_v_n[1] * s_dir_v_n[0] - a_dir_v_n[
            0] * s_dir_v_n[1],
        a_dir_v_n[1] * s_dir_v_n[1] + a_dir_v_n[
            0] * s_dir_v_n[0]) / math.pi
    return angle, s_d_v, a_dir_v_n, s_dir_v_n


def play_game(s_st, s_pos, a_pos, bt_d, score, display, clock):
    cr = False
    while cr is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cr = True
        display.fill((0, 0, 0))

        dis_ap(a_pos, display)
        dis_sn(s_pos, display)

        s_pos, a_pos, score = gen_sn(s_st, s_pos, a_pos,
                                                               bt_d, score)
        pygame.display.set_caption("SCORE: " + str(score))
        pygame.display.update()
        clock.tick(500000)

        return s_pos, a_pos, score


window_width = 500
window_height = 500

pygame.init()
display=pygame.display.set_mode((window_width,window_height))
clock=pygame.time.Clock()