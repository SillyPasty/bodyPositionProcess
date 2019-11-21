import json


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


def getJson(file_path):
    '''Open folder and process .json into a dict
       input: The file path
       ouput: A dictionay of parts' name and cooridnates
    '''
    with open(file_path) as f:
        obj = json.load(f)
        if not obj['people']:
            return None
        body_list = obj['people'][0]['pose_keypoints_2d']  # Store body position

        coor = {}  # Store each body part into a dictionary

        for x in range(25):
            i = x * 3
            s = ()
            s = (body_list[i], body_list[i + 1], body_list[i + 2])
            coor[BODY_PATRS[x]] = s
        return coor
