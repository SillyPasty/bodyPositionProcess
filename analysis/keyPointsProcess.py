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


def getKeyPoints(keyPointsList):
    coor = {}
    for x in range(25):
        s = ()
        s = (keyPointsList[x][0], keyPointsList[x][1], keyPointsList[x][2])
        coor[BODY_PATRS[x]] = s
    return coor
