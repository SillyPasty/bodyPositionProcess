import math


def getAngle(d1, d2, d3):
    """ Get the angle bewteen point d1, d2, d3
        Use Cosine theorem
        input: tuple or list of the three coordinate
        output: the degree of ∠d1d2d3
    """
    x1, y1, x2, y2, x3, y3 = d1[0], d1[1], d2[0], d2[1], d3[0], d3[1]
    a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c_2 = ((x1 - x3)**2 + (y1 - y3)**2)
    cos = (a**2 + b**2 - c_2) / (2 * a * b)
    return math.acos(cos) / math.pi * 180


def getDistance(d1, d2, d3):
    """ Get the distance between dot d1 and line d2-d3
        input: tuple or list of the three coordinate
        output: the distance between dot d1 and line d2-d3
    """
    x1, y1, x2, y2, x3, y3 = d1[0], d1[1], d2[0], d2[1], d3[0], d3[1]
    distance = abs((y2 - y3) * x1 - (x2 - x3) * y1 + (x2 * y3) -
                   (y2 * x3)) / math.sqrt((y2 - y3)**2 + (x2 - x3)**2)
    return distance


def getElbowAngle(coor, side=''):
    """ Get the elbow angle
        Args: coor: dictionary of body coordinates
              side: L/R
        output: The elbow angle
    """
    shoulder = coor[side + 'Shoulder']
    elbow = coor[side + 'Elbow']
    wrist = coor[side + 'Wrist']
    if shoulder[2] != 0 and elbow[2] != 0 and wrist[2] != 0:
        return getAngle(shoulder, elbow, wrist)
    else:
        return None


def getHipAngle(coor, side=''):
    """ Get the hip angle
        Args: coor: dictionary of body coordinates
              side: L/R
        output: The hip angle
    """
    knee = coor[side + 'Knee']
    m_hip = coor['MidHip']
    neck = coor['Neck']
    if knee[2] != 0 and neck[2] != 0 and m_hip[2] != 0:
        return getAngle(knee, m_hip, neck)
    else:
        return None


def getKneeAngle(coor, side=''):
    """ Get the knee angle
        Args: coor: dictionary of body coordinates
              side: L/R
        output: The knee angle
    """
    knee = coor[side + 'Knee']
    m_hip = coor['MidHip']
    ankle = coor[side + 'Ankle']
    if knee[2] != 0 and ankle[2] != 0 and m_hip[2] != 0:
        return getAngle(m_hip, knee, ankle)
    else:
        return None


def getHipDistance(coor, side=''):
    """ Get the knee angle
        Args: coor: dictionary of body coordinates
              side: L/R
        output: The knee angle
    """
    r_wrist = coor[side + 'Wrist']
    m_hip = coor['MidHip']
    r_toe = coor[side + 'BigToe']
    if m_hip[2] != 0 and r_toe[2] != 0 and r_wrist[2] != 0:
        return getDistance(m_hip, r_toe, r_wrist)
    else:
        return None


def getHeadDistance(coor):
    """ Get the head and wrist distance
        Args: coor: dictionary of body coordinates
              side: L/R
        output: The distance between head and wrist
    """
    r_wrist = coor['RWrist']
    l_wrist = coor['LWrist']
    neck = coor['Neck']
    dist = getDistance(neck, r_wrist, l_wrist)
    if r_wrist[2] != 0 and l_wrist[2] != 0 and neck[2] != 0:
        if neck[0] < r_wrist[0]:
            return -dist
        else:
            return dist
    else:
        return None


def getEyeDistance(coor):
    """ Get the head and wrist distance
        Args: coor: dictionary of body coordinates
        output: The distance between head and wrist
    """
    r_wrist = coor['RWrist']
    l_wrist = coor['LWrist']
    eye = coor['REye']
    dist = getDistance(eye, r_wrist, l_wrist)
    if r_wrist[2] != 0 and l_wrist[2] != 0 and eye[2] != 0:
        if eye[0] < r_wrist[0]:
            return -dist
        else:
            return dist
    else:
        return None
