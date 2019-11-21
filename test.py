# Test Codes
# Used to get some values
import getValue
import os
import jsonProcess as jp
import matplotlib.pyplot as plt


def get_infos(folder_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: A dictionay of parts' name and cooridnates
    '''
    files = os.listdir(folder_path)
    max_r_elbow_angle = 0
    min_r_elbow_angle = 200
    max_hip_distance = 0
    min_hip_distance = 10000
    cnt1 = total_elbow_angle = cnt2 = total_hip_distance = 0
    elb_ang = []
    hip_dis = []
    for file in files:
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue
        r_shoulder = coor['RShoulder']
        r_elbow = coor['RElbow']
        r_wrist = coor['RWrist']
        m_hip = coor['MidHip']
        r_toe = coor['RBigToe']
        if r_shoulder[2] != 0 and r_elbow[2] != 0 and r_wrist[2] != 0:
            r_elbow_angle = getValue.get_angle(r_shoulder, r_elbow, r_wrist)
            elb_ang.append(r_elbow_angle)
            total_elbow_angle += r_elbow_angle
            cnt1 += 1
            max_r_elbow_angle = max(max_r_elbow_angle, r_elbow_angle)
            min_r_elbow_angle = min(min_r_elbow_angle, r_elbow_angle)
        if m_hip[2] != 0 and r_toe[2] != 0 and r_wrist[2] != 0:
            hip_distance = getValue.get_distance(m_hip, r_toe, r_wrist)
            hip_dis.append(hip_distance)
            total_hip_distance += hip_distance
            cnt2 += 1
            max_hip_distance = max(max_hip_distance, hip_distance)
            min_hip_distance = min(min_hip_distance, hip_distance)
    aver_r_elbow_angle = total_elbow_angle / cnt1
    aver_hip_distance = total_hip_distance / cnt2

    print('max elbow angle:', max_r_elbow_angle)
    print('min elbow angle:', min_r_elbow_angle)
    print('aver elbow angle:', aver_r_elbow_angle)

    print('max hip distance:', max_hip_distance)
    print('min hip distance:', min_hip_distance)
    print('aver hip distance:', aver_hip_distance)
    elb_ang_below_105 = []
    for ans in elb_ang:
        if ans < 105:
            elb_ang_below_105.append(ans)
        else:
            elb_ang_below_105.append(None)

    ax1 = plt.subplot(2, 1, 1)

    # ax1.scatter(range(cnt1), elb_ang, label='elbow angle', s=10)
    # ax1.scatter(range(cnt1), elb_ang_below_105, label='elbow angle', color='r', s=10)
    ax1.plot(range(cnt1), elb_ang, label='elbow angle')
    ax1.plot(range(cnt1), elb_ang_below_105, label='elbow angle', color='r')
    ax1.set_title('elbow_angle')

    ax2 = plt.subplot(2, 1, 2)
    ax2.scatter(range(cnt2), hip_dis, label='hip distance')
    ax2.set_title('hip_distance')
    plt.show()
