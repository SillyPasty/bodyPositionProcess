import jsonProcess as jp
import os
import configparser
import getValue
import numpy as np

CONFIG_FILE = 'bodyPositionDetect.cfg'
config = configparser.ConfigParser()

config.read(CONFIG_FILE)


def getTendency(tick, n, var):
    """ Get the tendency of a tick
        Args: tick a list of data
              n the size of judge
        Output: string
    """
    first_value = tick[0]
    upper = down = 0
    tick_var = np.var(tick)
    for i in range(n):
        if tick[i] < first_value:
            down += 1
        elif first_value < tick[i]:
            upper += 1
    if tick_var <= var:
        return None
    elif 3 <= down:
        return 'down'
    elif 3 <= upper:
        return 'upper'
    else:
        return None


def pushUpTimesCountByTendency(folder_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The times of push-up
    '''
    files = os.listdir(folder_path)

    cnt = 0
    cnt_knee_down = cnt_knee_up = 0
    cnt_hip_down = cnt_hip_up = 0
    results = []
    result = {}
    period_cnt = 0

    tendency = []
    tick = []
    is_hip_angle_standard_flag = True
    is_knee_angle_standard_flag = True

    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue

        r_elbow_angle = getValue.getElbowAngle(coor, 'R')
        r_knee_angle = getValue.getKneeAngle(coor, 'R')
        hip_angle = getValue.getHipAngle(coor, 'R')

        if r_elbow_angle:
            tick.append(r_elbow_angle)
            period_cnt += 1
            if period_cnt == 5:
                tend = getTendency(tick, 5, 1.5)
                tick = []
                if tend:
                    tendency.append(tend)
                    if 1 <= len(tendency):
                        print(cnt, 'tendency:', tendency[-1])
                    if 3 <= len(tendency):
                        if tendency[-1] == 'down':
                            if tendency[-2] == 'upper':  # a periodt and  endency[-3] == 'upper'
                                cnt += 1
                                result['Num'] = cnt
                                result['IsStandard'] = (is_hip_angle_standard_flag and is_knee_angle_standard_flag)
                                result['IsHipStandard'] = is_hip_angle_standard_flag
                                result['IsKneeStandard'] = is_knee_angle_standard_flag
                                result['Flag'] = i
                                results.append(result)
                                result = {}
                                is_hip_angle_standard_flag = True
                                is_knee_angle_standard_flag = True

        if hip_angle:
            if hip_angle <= 150:
                cnt_hip_down += 1
                if 2 <= cnt_hip_down:
                    is_hip_angle_standard_flag = False
            else:
                cnt_hip_up += 1
                if 2 <= cnt_hip_up:  # debounce
                    cnt_hip_down = 0

        if r_knee_angle:
            if r_knee_angle <= 155:
                cnt_knee_down += 1
                if 2 <= cnt_knee_down:
                    is_knee_angle_standard_flag = False
            else:
                cnt_knee_up += 1
                if 2 <= cnt_knee_up:  # debounce
                    cnt_knee_down = 0

    return results


def pushUpTimesCountByAngle(folder_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The times of push-up
    '''
    files = os.listdir(folder_path)
    cnt_down = cnt_up = cnt = 0
    cnt_knee_down = cnt_knee_up = 0
    cnt_hip_down = cnt_hip_up = 0
    results = []
    result = {}
    period_flag = []
    start_flag = 0
    is_hip_angle_standard_flag = True
    is_knee_angle_standard_flag = True

    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue
        TO_BELOW = int(config.get('PushUp_Config', 'ELBOW_TO_BELOW'))
        TO_ABOVE = int(config.get('PushUp_Config', 'ELBOW_TO_ABOVE'))
        r_elbow_angle = getValue.getElbowAngle(coor, 'R')
        r_knee_angle = getValue.getKneeAngle(coor, 'R')
        hip_angle = getValue.getHipAngle(coor, 'R')

        if r_elbow_angle:
            if r_elbow_angle < TO_BELOW:
                cnt_down += 1
                if 2 <= cnt_down and cnt_up <= 3:
                    cnt_up = 0

                if 2 <= cnt_down and 5 <= cnt_up:
                    cnt_up = 0
                    cnt += 1
                    result['Num'] = cnt
                    result['IsStandard'] = (is_hip_angle_standard_flag and is_knee_angle_standard_flag)
                    result['IsHipStandard'] = is_hip_angle_standard_flag
                    result['IsKneeStandard'] = is_knee_angle_standard_flag
                    results.append(result)
                    result = {}

                    period_flag.append((start_flag + i - 2) / 2)
                    start_flag = i - 2
                    is_hip_angle_standard_flag = True
                    is_knee_angle_standard_flag = True
            elif TO_ABOVE < r_elbow_angle:
                cnt_up += 1
                if 2 <= cnt_up and cnt_down <= 3:
                    cnt_down = 0

                if 2 <= cnt_up and 4 <= cnt_down:
                    cnt_down = 0
                    start_flag = i - 2

        if hip_angle:
            if hip_angle <= 160:
                cnt_hip_down += 1
                if 2 <= cnt_hip_down:
                    is_hip_angle_standard_flag = False
            else:
                cnt_hip_up += 1
                if 2 <= cnt_hip_up:  # debounce
                    cnt_hip_down = 0

        if r_knee_angle:
            if r_knee_angle <= 160:
                cnt_knee_down += 1
                if 2 <= cnt_knee_down:
                    is_knee_angle_standard_flag = False
            else:
                cnt_knee_up += 1
                if 2 <= cnt_knee_up:  # debounce
                    cnt_knee_down = 0

    return period_flag, results
