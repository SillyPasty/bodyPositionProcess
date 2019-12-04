import configparser
import numpy as np

CONFIG_FILE = r'C:\Users\Lenovo\Desktop\雏燕2019\后端部分所需资料\bodyPositionDetect.cfg'
config = configparser.ConfigParser()

config.read(CONFIG_FILE)


def getTendency(tick, var):
    """ Get the tendency of a tick
        Args: tick a list of data
              n the size of judge
        Output: string
    """
    for j in range(len(tick)):
        if tick[j] is not None:
            return j
        continue
    first_value = tick[j]
    upper = down = 0
    for i in range(len(tick)):
        if tick[i] is not None:
            tick_var = np.var(tick)
        for i in range(1,len(tick)):
            if tick[i] is not None:
                if tick[i] < first_value:
                    down += 1
                elif first_value < tick[i]:
                    upper += 1
                if tick_var <= var:
                    return 'stable'
                elif 3 <= down:
                    return 'down'
                elif 3 <= upper:
                    return 'upper'
                else:
                    return 'stable'


def pushUpPeriodJudge(r_elbow_angle_list, hip_angle_list, r_knee_angle_list):
    is_r_elbow_standard = is_hip_standard = is_r_knee_standard = True
    ELBOW_TO_BELOW = int(config.get('PushUp_Config', 'ELBOW_TO_BELOW'))
    ELBOW_TO_ABOVE = int(config.get('PushUp_Config', 'ELBOW_TO_ABOVE'))
    KNEE_TO_ABOVE = int(config.get('PushUp_Config', 'KNEE_TO_ABOVE'))
    HIP_ANGLE_TO_ABOVE = int(config.get('PushUp_Config', 'HIP_ANGLE_TO_ABOVE'))
    if not (ELBOW_TO_ABOVE <= max(r_elbow_angle_list) and min(r_elbow_angle_list) <= ELBOW_TO_BELOW):
        is_r_elbow_standard = False

    if not (HIP_ANGLE_TO_ABOVE <= min(hip_angle_list)):
        is_hip_standard = False

    if not (KNEE_TO_ABOVE <= min(r_knee_angle_list)):
        is_r_knee_standard = False

    return (is_r_elbow_standard, is_hip_standard, is_r_knee_standard)


def pullUpPeriodJudge(r_elbow_angle_list, l_elbow_angle_list, eye_distance_list):
    is_r_elbow_standard = is_l_elbow_standard = is_height_standard = True
    ELBOW_TO_BELOW = int(config.get('PullUp_Config', 'ELBOW_TO_BELOW'))
    ELBOW_TO_ABOVE = int(config.get('PullUp_Config', 'ELBOW_TO_ABOVE'))
    # NECK_DISTANCE = int(config.get('PullUp_Config', 'NECK_DISTANCE'))
    EYE_DISTANCE = int(config.get('PullUp_Config', 'EYE_DISTANCE'))
    if not (ELBOW_TO_ABOVE <= max(r_elbow_angle_list) and min(r_elbow_angle_list) <= ELBOW_TO_BELOW):
        is_r_elbow_standard = False

    if not (ELBOW_TO_ABOVE <= max(l_elbow_angle_list) and min(l_elbow_angle_list) <= ELBOW_TO_BELOW):
        is_l_elbow_standard = False

    if not (min(eye_distance_list) <= EYE_DISTANCE):
        is_height_standard = False

    return (is_r_elbow_standard, is_l_elbow_standard, is_height_standard)


def sitUpPeriodJudge(r_waist_angle_list,l_waist_angle_list,r_knee_angle_list,l_knee_angle_list):
    #r_shouldertowrist_distance_list l_shouldertowrist_distance_list
    is_r_waist_standard = is_l_waist_standard = is_r_knee_standard = is_l_knee_standard = is_r_shouldertowrist_standard = is_l_shouldertowrist_standard= True
    WAIST_TO_BELOW = int(config.get('SitUp_Config', 'WAIST_TO_BELOW'))
    WAIST_TO_ABOVE = int(config.get('SitUp_Config', 'WAIST_TO_ABOVE'))
    KNEE_TO_BELOW = int(config.get('SitUp_config','KNEE_TO_BELOW'))
    KNEE_TO_ABOVE = int(config.get('SitUp_config','KNEE_TO_ABOVE'))
    #STW_TO_BELOW = int(config.get('SitUp_config','STW_TO_BELOW'))
    #STW_TO_ABOVE = int(config.get('SitUp_config','STW_TO_ABOVE'))

    if not (WAIST_TO_ABOVE <= max(r_waist_angle_list) and min(r_waist_angle_list) <= WAIST_TO_BELOW):
        is_r_waist_standard = False

    if not (WAIST_TO_ABOVE <= max(l_waist_angle_list) and min(l_waist_angle_list) <= WAIST_TO_BELOW):
        is_l_waist_standard = False

    if not (KNEE_TO_ABOVE <= max(r_knee_angle_list) and min(r_knee_angle_list) <= KNEE_TO_BELOW):
        is_r_knee_standard = False

    if not (KNEE_TO_ABOVE <= max(l_knee_angle_list) and min(l_knee_angle_list) <= KNEE_TO_BELOW):
        is_l_knee_standard = False

    #if not (STW_TO_ABOVE <= max(r_shouldertowrist_distance_list) and min(r_shouldertowrist_distance_list) <= STW_TO_BELOW):
        #is_r_shouldertowrist_standard =False

    #if not (STW_TO_ABOVE <= max(l_shouldertowrist_distance_list) and min(l_shouldertowrist_distance_list) <= STW_TO_BELOW):
        #is_l_shouldertowrist_standard = False

    return (is_r_waist_standard,is_l_waist_standard,is_r_knee_standard,is_l_knee_standard,is_r_shouldertowrist_standard,is_l_shouldertowrist_standard)

