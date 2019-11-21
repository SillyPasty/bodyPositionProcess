import json
import math
import os

BODY_PATRS = ['Nose', 'Neck',
              'RShoulder', 'RElbow', 'RWrist',
              'LShoulder', 'LElbow', 'LWrist',
              'MidHip',
              'RHip', 'RKnee', 'RAnkle',
              'LHip', 'LKnee', 'LAnkle',
              'REye', 'LEye', 'REar', 'LEar',
              'LBigToe', 'LSmallToe', 'LHeel',
              'RBigToe', 'RSmallToe', 'RHeel',
              'Background']
FILEPATH = r'E:\Programming\Openpose\openpose\openpose\output\push-up'
# with open(FILEPATH + r'\俯卧撑－斜侧_000000000000_keypoints.json') as f:
#     obj = json.load(f)
#     body_list = obj['people'][0]['pose_keypoints_2d']  # Store body position
#     coor = []
#     s = ()
#     print(type(body_list[0]))
#     for x in range(25):
#         i = x * 3
#         s = ()
#         s = (body_list[i], body_list[i + 1], body_list[i + 2])
#         coor[BODY_PATRS[x]] = s

#     print(coor)


def get_angle(d1, d2, d3):
    """ Get the angle bewteen point d1, d2, d3
        Use Cosine theorem
        input: tuple or list of the three coordinate
        output: the degree of ∠d1d2d3
    """
    x1, y1, x2, y2, x3, y3 = d1[0], d1[1], d2[0], d2[1], d3[0], d3[1]
    a = math.sqrt((x1-x2)**2+(y1-y2)**2)
    b = math.sqrt((x3-x2)**2+(y3-y2)**2)
    c_2 = ((x1-x3)**2+(y1-y3)**2)
    cos = (a**2 + b**2 - c_2) / (2 * a * b)
    return math.acos(cos) / math.pi * 180


def get_distance(d1, d2, d3):
    """ Get the distance between dot d1 and line d2-d3
        input: tuple or list of the three coordinate
        output: the distance between dot d1 and line d2-d3
    """
    x1, y1, x2, y2, x3, y3 = d1[0], d1[1], d2[0], d2[1], d3[0], d3[1]
    distance = abs((y2 - y3) * x1 - (x2 - x3) * y1 + (x2 * y3) - (y2 * x3)) / math.sqrt((y2 - y3) ** 2 + (x2 - x3) ** 2)
    return distance


def get_files(file_path):
    '''Open folder and process .json into a dict
       input:
       ouput:
    '''
    files = os.listdir(file_path)
    max_r_elbow_angle = 0
    min_r_elbow_angle = 200
    max_hip_distance = 0
    min_hip_distance = 10000
    for file in files:
        with open(file_path + '\\' + file) as f:
            obj = json.load(f)
            if not obj['people']:
                continue
            body_list = obj['people'][0]['pose_keypoints_2d']  # Store body position

            coor = {}  # Store each body part into a dictionary

            for x in range(25):
                i = x * 3
                s = ()
                s = (body_list[i], body_list[i + 1], body_list[i + 2])
                coor[BODY_PATRS[x]] = s
            
            r_shoulder = coor['RShoulder']
            r_elbow = coor['RElbow']
            r_wrist = coor['RWrist']
            m_hip = coor['MidHip']
            r_toe = coor['RBigToe']
            if r_shoulder[2] != 0 and r_elbow[2] != 0 and r_wrist[2] != 0:
                r_elbow_angle = get_angle(r_shoulder, r_elbow, r_wrist)
                max_r_elbow_angle = max(max_r_elbow_angle, r_elbow_angle)
                min_r_elbow_angle = min(min_r_elbow_angle, r_elbow_angle)
            if m_hip[2] != 0 and r_toe[2] != 0 and r_wrist[2] != 0:
                hip_distance = get_distance(m_hip, r_toe, r_wrist)
                max_hip_distance = max(max_hip_distance, hip_distance)
                min_hip_distance = min(min_hip_distance, hip_distance)
    print('max elbow angle:', max_r_elbow_angle)
    print('min elbow angle:', min_r_elbow_angle)

    print('max hip distance:', max_hip_distance)
    print('min hip distance:', min_hip_distance)

        
get_files(FILEPATH)
