# Test Codes
# Used to get some values
import getValue
import os
import jsonProcess as jp
import matplotlib.pyplot as plt

def getPushUpInfos(folder_path, is_print, region=[]):
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
    cnt = 0
    cnt1 = total_elbow_angle = cnt2 = total_hip_distance = 0
    cnt3 = total_knee_angle = cnt4 = total_hip_angle = 0
    elb_ang = []
    hip_dis = []
    knee_ang = []
    hip_ang = []

    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue
        cnt = i
        r_elbow_angle = getValue.getElbowAngle(coor, 'R')
        r_knee_angle = getValue.getKneeAngle(coor, 'R')
        hip_angle = getValue.getHipAngle(coor, 'R')
        hip_distance = getValue.getHipDistance(coor, 'R')

        if r_elbow_angle:
            elb_ang.append(r_elbow_angle)
            total_elbow_angle += r_elbow_angle
            cnt1 += 1
            max_r_elbow_angle = max(max_r_elbow_angle, r_elbow_angle)
            min_r_elbow_angle = min(min_r_elbow_angle, r_elbow_angle)
        else:
            elb_ang.append(0)

        if hip_distance:
            hip_dis.append(hip_distance)
            total_hip_distance += hip_distance
            cnt2 += 1
            max_hip_distance = max(max_hip_distance, hip_distance)
            min_hip_distance = min(min_hip_distance, hip_distance)
        else:
            hip_dis.append(0)

        if r_knee_angle:
            knee_ang.append(r_knee_angle)
            total_knee_angle += r_knee_angle
            cnt3 += 1
            max_knee_angle = max(max_knee_angle, r_knee_angle)
            min_knee_angle = min(min_knee_angle, r_knee_angle)
        else:
            knee_ang.append(0)

        if hip_angle:
            hip_ang.append(hip_angle)
            total_hip_angle += hip_angle
            cnt4 += 1
            max_hip_angle = max(max_hip_angle, hip_angle)
            min_hip_angle = min(min_hip_angle, hip_angle)
        else:
            hip_ang.append(0)

    aver_r_elbow_angle = total_elbow_angle / cnt1
    aver_hip_distance = total_hip_distance / cnt2
    aver_knee_angle = total_knee_angle / cnt3
    aver_hip_angle = total_hip_angle / cnt4
    if is_print:
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
    cnt += 1

    ax1 = plt.subplot(2, 2, 1)
    # plt.hlines(165, )
    # ax1.scatter(range(cnt1), elb_ang, label='elbow angle', s=10)
    # ax1.scatter(range(cnt1), elb_ang_below_105, label='elbow angle', color='r', s=10)
    # actu = [89, 149, 238, 328, 418, 597, 686, 746, 836, 955, 985]
    # region = 0
    ax1.scatter(range(cnt), elb_ang, label='elbow angle', s=2)
    ax1.scatter(range(cnt), elb_ang_below_105, label='elbow angle', color='r', s=2)
    ax1.hlines(165, 0, cnt, colors='c')
    ax1.vlines(region, 0, 180)
    # ax1.vlines(actu, 0, 180, colors='r')
    ax1.set_title('elbow_angle')

    ax2 = plt.subplot(2, 2, 2)
    ax2.scatter(range(cnt), hip_dis, label='hip distance', s=2)
    ax2.set_title('hip_distance')

    ax3 = plt.subplot(2, 2, 3)
    ax3.scatter(range(cnt), knee_ang, label='knee angle', s=2)
    ax3.vlines(region, 0, 180)
    # ax3.vlines(actu, 0, 180, colors='r')
    ax3.set_title('knee_angle')

    ax4 = plt.subplot(2, 2, 4)
    ax4.scatter(range(cnt), hip_ang, label='hip', s=2)
    ax4.vlines(region, 0, 180)
    # ax4.vlines(actu, 0, 180, colors='r')
    ax4.set_title('hip_angle')

    plt.show()
    # plt.savefig(r'E:\University\科研创新\雏燕计划-体测\push-up-side.png')


def getPullUpInfos(folder_path, is_print, region=[]):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The analysis of some infos of the whole process
    '''
    files = os.listdir(folder_path)
    max_r_elbow_angle = max_l_elbow_angle = 0
    min_r_elbow_angle = min_l_elbow_angle = 200
    r_elb_ang = []
    l_elb_ang = []
    neck_horizontalbar_distance = []
    eye_wrist_distance_list = []
    cnt1 = cnt2 = 0
    total_r_elbow_angle = total_l_elbow_angle = 0

    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue
        cnt = i
        r_elbow_angle = getValue.getElbowAngle(coor, 'R')
        l_elbow_angle = getValue.getElbowAngle(coor, 'L')
        head_wrist_distance = getValue.getHeadDistance(coor)
        eye_wrist_distance = getValue.getEyeWristDistance(coor)

        if r_elbow_angle:
            r_elb_ang.append(r_elbow_angle)
            total_r_elbow_angle += r_elbow_angle
            cnt1 += 1
            max_r_elbow_angle = max(max_r_elbow_angle, r_elbow_angle)
            min_r_elbow_angle = min(min_r_elbow_angle, r_elbow_angle)
        else:
            r_elb_ang.append(0)

        if l_elbow_angle:
            l_elb_ang.append(l_elbow_angle)
            total_l_elbow_angle += l_elbow_angle
            cnt2 += 1
            max_l_elbow_angle = max(max_l_elbow_angle, l_elbow_angle)
            min_l_elbow_angle = min(min_l_elbow_angle, l_elbow_angle)
        else:
            l_elb_ang.append(0)

        if head_wrist_distance:
            neck_horizontalbar_distance.append(head_wrist_distance)
        else:
            neck_horizontalbar_distance.append(0)

        if eye_wrist_distance:
            eye_wrist_distance_list.append(eye_wrist_distance)
        else:
            eye_wrist_distance_list.append(0)

    aver_r_elbow_angle = total_r_elbow_angle / cnt1
    aver_l_elbow_angle = total_l_elbow_angle / cnt2
    if is_print:
        print('max r_elbow angle:', max_r_elbow_angle)
        print('min r_elbow angle:', min_r_elbow_angle)
        print('aver r_elbow angle:', aver_r_elbow_angle)

        print('max l_elbow angle:', max_l_elbow_angle)
        print('min l_elbow angle:', min_l_elbow_angle)
        print('aver l_elbow angle:', aver_l_elbow_angle)

    # elb_ang_below_105 = []
    # for ans in elb_ang:
    #     if ans < 105:
    #         elb_ang_below_105.append(ans)
    #     else:
    #         elb_ang_below_105.append(None)
    cnt += 1

    ax1 = plt.subplot(2, 2, 1)
    ax1.scatter(range(cnt), r_elb_ang, label='relbow angle', s=2)
    ax1.vlines(region, 0, 180)
    ax1.set_title('relbow_angle')

    ax2 = plt.subplot(2, 2, 2)
    ax2.scatter(range(cnt), l_elb_ang, label='lelbow angle', s=2)
    ax2.set_title('lelbow_angle')

    ax3 = plt.subplot(2, 2, 3)
    ax3.scatter(range(cnt), neck_horizontalbar_distance, label='neck bar distance', s=2)
    ax3.set_title('neck bar distance')

    ax4 = plt.subplot(2, 2, 4)
    ax4.scatter(range(cnt), eye_wrist_distance_list, label='eye bar distance', s=2)
    ax4.set_title('eye bar distance')
    plt.show()
    # plt.savefig(r'E:\University\科研创新\雏燕计划-体测\push-up-side.png')


def getSitUpInfos(folder_path, is_print, region=[]):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The analysis of some infos of the whole process
    '''
    files = os.listdir(folder_path)
    max_r_waist_angle = 0
    min_r_waist_angle = 200
    max_r_s_knee_angle = 0
    min_r_s_knee_angle = 200
    s_knee_ang = []
    wai_ang = []
    cnt = 0
    cnt1 = cnt2 = 0
    cnt3 = 0
    total_waist_angle = total_s_knee_angle = 0

    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue
        cnt = i
        r_s_knee_angle = getValue.getKneeAngle(coor, 'R')
        r_waist_angle = getValue.getWaistAngle(coor, 'R')

        if r_s_knee_angle:
            s_knee_ang.append(r_s_knee_angle)
            total_s_knee_angle += r_s_knee_angle
            cnt1 += 1
            max_r_s_knee_angle = max(max_r_s_knee_angle, r_s_knee_angle)
            min_r_s_knee_angle = min(min_r_s_knee_angle, r_s_knee_angle)
        else:
            s_knee_ang.append(0)

        if r_waist_angle:
            wai_ang.append(r_waist_angle)
            total_waist_angle += r_waist_angle
            cnt2 += 1
            max_r_waist_angle = max(max_r_waist_angle, r_waist_angle)
            min_r_waist_angle = min(min_r_waist_angle, r_waist_angle)
        else:
            wai_ang.append(0)

    aver_r_s_knee_angle = total_s_knee_angle / cnt1
    aver_r_waist_angle = total_waist_angle / cnt2

    if is_print:
        print('max sit-up knee angle:', max_r_s_knee_angle)
        print('min sit-up knee angle:', min_r_s_knee_angle)
        print('aver sit-up knee angle:', aver_r_s_knee_angle)

        print('max sit-up waist angle:', max_r_waist_angle)
        print('min sit-up waist angle:', min_r_waist_angle)
        print('aver sit-up waist angle:', aver_r_waist_angle)

    s_knee_ang_below_60 = []
    for ans in s_knee_ang:
        if ans < 105:
            s_knee_ang_below_60.append(ans)
        else:
            s_knee_ang_below_60.append(None)
    cnt += 1

    wai_ang_above_140 = []
    for wans in s_knee_ang:
        if wans > 140:
            wai_ang_above_140.append(wans)
        else:
            wai_ang_above_140.append(None)
    cnt3 += 1
    cnt = 0
    for i in s_knee_ang:
        if s_knee_ang[i] is not None:
            cnt += 1
        return cnt

    ax1 = plt.subplot(1, 2, 1)  # 第一行的左图 第一个参数代表子图的行数，第二个参数代表该行图像的列数，第三个参数代表每行的第几个图像
    # plt.hlines(165, )
    # ax1.scatter(range(cnt1), elb_ang, label='elbow angle', s=10)
    # ax1.scatter(range(cnt1), elb_ang_below_105, label='elbow angle', color='r', s=10)
    # actu = [89, 149, 238, 328, 418, 597, 686, 746, 836, 955, 985]
    # region = 0
    ax1.scatter(range(cnt), s_knee_ang, label='s_knee angle', s=2)  # range(cnt)表示绘制散点图的数据点，s_knee_ang:图名，s:一个实数？
    ax1.scatter(range(cnt), s_knee_ang_below_60, label='s_knee_angle', color='r', s=2)  # color表示颜色
    ax1.hlines(70, 0, cnt, colors='c')  # 绘制水平辅助线 70：横坐标，0：ymin,cnt: ymax(辅助线纵坐标的最大最小值) colors:颜色
    ax1.vlines(region, 0, 180)  # 绘制竖直辅助线
    # ax1.vlines(actu, 0, 180, colors='r')
    ax1.set_title('s_knee_angle')

    ax2 = plt.subplot(1, 2, 2)
    ax2.scatter(range(cnt), wai_ang, label='waist angle', s=2)
    ax1.scatter(range(cnt), wai_ang_above_140, label='waist_angle', color='r', s=2)  # color表示颜色
    ax1.hlines(140, 0, cnt, colors='c')  # 绘制水平辅助线 140：横坐标，0：ymin,cnt: ymax(辅助线纵坐标的最大最小值) colors:颜色
    ax2.set_title('waist_angle')
    #fig, ax2 = plt.subplots(figsize=(12, 12))
    #ax2.imshow(ax2, aspect='waist_angle')  # im是要显示的图案
    plt.savefig(r"C:\Users\Lenovo\Desktop\雏燕2019\后端部分所需资料\sit-up.png")
    plt.show()
