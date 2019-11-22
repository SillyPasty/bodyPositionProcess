# Test Codes
# Used to get some values
import getValue
import os
import jsonProcess as jp
import matplotlib.pyplot as plt


def getPushUpInfos(folder_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The analysis of some infos of the whole process
    '''
    files = os.listdir(folder_path)
    max_r_elbow_angle = 0
    min_r_elbow_angle = 200
    max_knee_angle = 0
    min_knee_angle = 200
    max_hip_angle = 0
    min_hip_angle = 10000
    max_hip_distance = 0
    min_hip_distance = 10000

    cnt1 = total_elbow_angle = cnt2 = total_hip_distance = 0
    cnt3 = total_knee_angle = cnt4 = total_hip_angle = 0
    elb_ang = []
    hip_dis = []
    knee_ang = []
    hip_ang = []

    for file in files:
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue
        r_shoulder = coor['RShoulder']
        r_elbow = coor['RElbow']
        r_wrist = coor['RWrist']
        m_hip = coor['MidHip']
        r_toe = coor['RBigToe']
        r_knee = coor['RKnee']
        r_anlke = coor['RAnkle']
        neck = coor['Neck']
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

        if r_knee[2] != 0 and r_anlke[2] != 0 and m_hip[2] != 0:
            r_knee_angle = getValue.get_angle(r_anlke, r_knee, m_hip)
            knee_ang.append(r_knee_angle)
            total_knee_angle += r_knee_angle
            cnt3 += 1
            max_knee_angle = max(max_knee_angle, r_knee_angle)
            min_knee_angle = min(min_knee_angle, r_knee_angle)

        if r_knee[2] != 0 and neck[2] != 0 and m_hip[2] != 0:
            hip_angle = getValue.get_angle(r_knee, m_hip, neck)
            hip_ang.append(hip_angle)
            total_hip_angle += hip_angle
            cnt4 += 1
            max_hip_angle = max(max_hip_angle, hip_angle)
            min_hip_angle = min(min_hip_angle, hip_angle)

    aver_r_elbow_angle = total_elbow_angle / cnt1
    aver_hip_distance = total_hip_distance / cnt2
    aver_knee_angle = total_knee_angle / cnt3
    aver_hip_angle = total_hip_angle / cnt4

    print('max elbow angle:', max_r_elbow_angle)
    print('min elbow angle:', min_r_elbow_angle)
    print('aver elbow angle:', aver_r_elbow_angle)

    print('max hip distance:', max_hip_distance)
    print('min hip distance:', min_hip_distance)
    print('aver hip distance:', aver_hip_distance)

    print('max knee angle:', max_knee_angle)
    print('min knee angle:', min_knee_angle)
    print('aver knee angle:', aver_knee_angle)

    print('max hip angle:', max_hip_angle)
    print('min hip angle:', min_hip_angle)
    print('aver hip angle:', aver_hip_angle)

    elb_ang_below_105 = []
    for ans in elb_ang:
        if ans < 105:
            elb_ang_below_105.append(ans)
        else:
            elb_ang_below_105.append(None)

    ax1 = plt.subplot(2, 2, 1)
    # plt.hlines(165, )
    # ax1.scatter(range(cnt1), elb_ang, label='elbow angle', s=10)
    # ax1.scatter(range(cnt1), elb_ang_below_105, label='elbow angle', color='r', s=10)
    ax1.scatter(range(cnt1), elb_ang, label='elbow angle', s=2)
    ax1.scatter(range(cnt1), elb_ang_below_105, label='elbow angle', color='r', s=2)
    ax1.hlines(165, 0, cnt1, colors='c')
    ax1.set_title('elbow_angle')

    # ax2 = plt.subplot(2, 2, 2)
    # ax2.scatter(range(cnt2), hip_dis, label='hip distance', s=2)
    # ax2.set_title('hip_distance')

    # ax3 = plt.subplot(2, 2, 3)
    # ax3.scatter(range(cnt3), knee_ang, label='knee angle', s=2)
    # ax3.set_title('knee_angle')

    # ax4 = plt.subplot(2, 2, 4)
    # ax4.scatter(range(cnt4), hip_ang, label='hip', s=2)
    # ax4.set_title('hip_angle')

    plt.show()
    # plt.savefig(r'E:\University\科研创新\雏燕计划-体测\push-up-side.png')
