import jsonProcess as jp
import os
import getValue


def pushUpTimesCount(folder_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The times of push-up
    '''
    files = os.listdir(folder_path)
    cnt_down = cnt_up = 0
    period_flag = []
    start_flag = 0
    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue
        r_shoulder = coor['RShoulder']
        r_elbow = coor['RElbow']
        r_wrist = coor['RWrist']

        TO_BELOW = 105
        TO_ABOVE = 165

        if r_shoulder[2] != 0 and r_elbow[2] != 0 and r_wrist[2] != 0:
            r_elbow_angle = getValue.get_angle(r_shoulder, r_elbow, r_wrist)
            # print(i, ':', r_elbow_angle)
            if r_elbow_angle < TO_BELOW:
                cnt_down += 1

                if 2 <= cnt_down and cnt_up <= 3:
                    cnt_up = 0

                if 2 <= cnt_down and 5 <= cnt_up:
                    cnt_up = 0
                    period_flag.append((start_flag + i - 2) / 2)
                    start_flag = i - 2

            elif TO_ABOVE < r_elbow_angle:
                cnt_up += 1
                if 2 <= cnt_up and cnt_down <= 3:
                    cnt_down = 0
                    
                if 2 <= cnt_up and 4 <= cnt_down:
                    cnt_down = 0
                    start_flag = i - 2

    return period_flag
