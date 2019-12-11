import analysis
import getValue
import jsonProcess as jp
import os


def sitUpAnalysis(folder_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: The times of push-up
    '''
    files = os.listdir(folder_path)

    results = []
    tendency = []
    tick = []
    result = {}
    r_waist_angle_list = []
    l_waist_angle_list = []
    r_s_knee_angle_list = []
    l_s_knee_angle_list = []
    r_elbowtoneck_dist_list = []
    l_elbowtoneck_dist_list = []

    total_r_elbowtoneck_dist = 0
    total_l_elbowtoneck_dist = 0
    cnt = cnt_1 = cnt_2 = 0

    for i, file in enumerate(files):
        coor = jp.getJson(folder_path + '\\' + file)
        if not coor:
            continue

        r_waist_angle = getValue.getWaistAngle(coor,'R')
        l_waist_angle = getValue.getWaistAngle(coor,'L')
        r_s_knee_angle = getValue.getKneeAngle(coor,'R')
        l_s_knee_angle = getValue.getKneeAngle(coor,'L')
        r_elbowtoneck_dist = getValue.getElbowToNeckDistance(coor,'R')
        l_elbowtoneck_dist = getValue.getElbowToNeckDistance(coor,'L')
        tick.append(r_waist_angle)

        if r_waist_angle:
            r_waist_angle_list.append(r_waist_angle)
        if l_waist_angle:
            l_waist_angle_list.append(l_waist_angle)
        if r_s_knee_angle:
            r_s_knee_angle_list.append(r_s_knee_angle)
        if l_s_knee_angle:
            l_s_knee_angle_list.append(l_s_knee_angle)
        if r_elbowtoneck_dist:
            r_elbowtoneck_dist_list.append(r_elbowtoneck_dist)
            cnt_1 += 1
            total_r_elbowtoneck_dist += r_elbowtoneck_dist
        aver_r_elbowtoneck_dist = total_r_elbowtoneck_dist/cnt_1
        if l_elbowtoneck_dist:
            l_elbowtoneck_dist_list.append(l_elbowtoneck_dist)
            cnt_2 += 1
            total_l_elbowtoneck_dist += l_elbowtoneck_dist
        aver_l_elbowtoneck_dist = total_l_elbowtoneck_dist/cnt_2


        if len(tick) == 5:
            tend = analysis.getTendency(tick, 8)  # One tick
            tick = []
            if tend:
                tendency.append(tend)
                if 3 <= len(tendency):
                    if tendency[-1] == 'down':
                        if tendency[-2] == 'upper':  # a period and tendency[-3] == 'upper'
                            cnt += 1
                            result['Num'] = cnt
                            standard = analysis.SitUpPeriodJudge(r_waist_angle_list,l_waist_angle_list,r_s_knee_angle_list,l_s_knee_angle_list,r_elbowtoneck_dist_list,l_elbowtoneck_dist_list,aver_r_elbowtoneck_dist,aver_l_elbowtoneck_dist)
                            result['IsRWaistStandard'], result['IsLWaistStandard'] = standard
                            result['IsRKneeAngle'],result['IsLKneeAngle'] = standard
                            result['IsRElbowtoNeckStandard'],result['IsLElbowtoNeckStandard'] = standard
                            result['Flag'] = i
                            r_waist_angle_list = l_waist_angle_list = []
                            r_s_knee_angle_list = l_s_knee_angle_list = []
                            r_elbowtoneck_dist_list = l_elbowtoneck_dist_list = []#序列置空
                            results.append(result)
                            result = {}

    print(tendency)

    return results
