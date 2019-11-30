import configparser

CONFIG_FILE = r'D:\Programming\PYTHON\bodyPosit\bodyPositionDetect.cfg'
conf = configparser.ConfigParser()
with open(CONFIG_FILE, 'w') as cfgfile:
    conf.add_section('PullUp_Config')
    conf.set('PullUp_Config', 'ELBOW_TO_BELOW', '60')
    conf.set('PullUp_Config', 'ELBOW_TO_ABOVE', '140')
    conf.set('PullUp_Config', 'NECK_DISTANCE', '0')
    conf.set('PullUp_Config', 'EYE_DISTANCE', '-70')
    conf.add_section('PushUp_Config')
    conf.set('PushUp_Config', 'ELBOW_TO_BELOW', '105')
    conf.set('PushUp_Config', 'ELBOW_TO_ABOVE', '165')
    conf.set('PushUp_Config', 'KNEE_TO_ABOVE', '155')
    conf.set('PushUp_Config', 'HIP_ANGLE_TO_ABOVE', '150')
    conf.write(cfgfile)
