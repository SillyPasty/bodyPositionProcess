import analysis
import getValue
import jsonProcess as jp
import os
import configparser

CONFIG_FILE = 'bodyPositionDetect.cfg'
config = configparser.ConfigParser()

config.read(CONFIG_FILE)


def pullUpAnalysis(folder_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The times of push-up
    '''
    files = os.listdir(folder_path)

    results = []
    tendency = []
    result = {}
    r_elbow_angle_list = []
    l_elbow_angle_list = []
    eye_distance_list = []
    tick = []
    cnt = 0

    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue

        r_elbow_angle = getValue.getElbowAngle(coor, 'R')
        l_elbow_angle = getValue.getElbowAngle(coor, 'L')
        eye_distance = getValue.getEyeDistance(coor)

        if l_elbow_angle:
            l_elbow_angle_list.append(l_elbow_angle)

        if eye_distance:
            eye_distance_list.append(eye_distance)

        if r_elbow_angle:
            r_elbow_angle_list.append(r_elbow_angle)
            tick.append(r_elbow_angle)
            if len(tick) == 5:
                tend = analysis.getTendency(tick, len(tick), 8)  # One tick
                tick = []
                if tend:
                    tendency.append(tend)
                    if 3 <= len(tendency):
                        if tendency[-1] == 'down':
                            if tendency[-2] == 'upper':  # a period and tendency[-3] == 'upper'
                                cnt += 1
                                result['Num'] = cnt
                                standard = pullUpPeriodJudje(r_elbow_angle_list, l_elbow_angle_list, eye_distance_list)
                                result['IsRElbowStandard'], result['IsLElbowStandard'], result['IsHeightStandard'] = standard
                                result['Flag'] = i
                                r_elbow_angle_list = l_elbow_angle_list = eye_distance_list = []
                                results.append(result)
                                result = {}

    return results


def pullUpPeriodJudje(r_elbow_angle_list, l_elbow_angle_list, eye_distance_list):
    is_r_elbow_standard = is_l_elbow_standard = is_height_standard = True
    ELBOW_TO_BELOW = 60  # int(config.get('PullUp_Config', 'ELBOW_TO_BELOW'))
    ELBOW_TO_ABOVE = 140  # int(config.get('PullUp_Config', 'ELBOW_TO_ABOVE'))
    # NECK_DISTANCE = int(config.get('PullUp_Config', 'NECK_DISTANCE'))
    EYE_DISTANCE = -70  # int(config.get('PullUp_Config', 'EYE_DISTANCE'))
    if not (ELBOW_TO_ABOVE <= max(r_elbow_angle_list) and min(r_elbow_angle_list) <= ELBOW_TO_BELOW):
        is_r_elbow_standard = False

    if not (ELBOW_TO_ABOVE <= max(l_elbow_angle_list) and min(l_elbow_angle_list) <= ELBOW_TO_BELOW):
        is_l_elbow_standard = False

    if not (min(eye_distance_list) <= EYE_DISTANCE):
        is_height_standard = False

    return (is_r_elbow_standard, is_l_elbow_standard, is_height_standard)
