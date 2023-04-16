from Snake_Game import *
from Feed_Forward_Neural_Network import *

def game_flow(display, clock, wts):
    max_score = 0
    avg_score = 0
    test_games = 1
    score1 = 0
    steps_per_game = 2500
    score2 = 0

    for _ in range(test_games):
        sss_st, sss_pos, tg_pos, score = st_pos()
        s_d_cnt = 0
        prev_dir = 0
        for _ in range(steps_per_game):
            cdv, ifb, ilb, irb = bl_dir(
                sss_pos)
            angle, snake_dir_vector, t_d_v_r, sdvn = ang_ap(
                sss_pos, tg_pos)
            predictions = []
            nayi_dir = np.argmax(np.array(forward_propagation(np.array(
                [ilb, ifb, irb, t_d_v_r[0],
                 sdvn[0], t_d_v_r[1],
                 sdvn[1]]).reshape(-1, 7), wts))) - 1

            if nayi_dir == prev_dir:
                s_d_cnt += 1
            else:
                s_d_cnt = 0
                prev_dir = nayi_dir

            new_dir = np.array(sss_pos[0]) - np.array(sss_pos[1])
            if nayi_dir == -1:
                new_dir = np.array([new_dir[1], -new_dir[0]])
            if nayi_dir == 1:
                new_dir = np.array([-new_dir[1], new_dir[0]])

            button_dir = gen_btn_dir(new_dir)

            next_step = sss_pos[0] + cdv
            if coll_bnd(sss_pos[0]) == 1 or coll_sl(next_step.tolist(), sss_pos) == 1:
                score1 += -150
                break

            else:
                score1 += 0

            sss_pos, tg_pos, score = play_game(sss_st, sss_pos, tg_pos,
                                                              button_dir, score, display, clock)

            if score > max_score:
                max_score = score

            if s_d_cnt > 8 and nayi_dir != 0:
                score2 -= 1
            else:
                score2 += 2


    return score1 + score2 + max_score * 5000