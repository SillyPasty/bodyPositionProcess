import test
import analysis
import pullUp
import pushUp

PULL_UP_FILEPATH = r'E:\Programming\Openpose\openpose\openpose\output\pull-up'
PUSH_UP_FILEPATH = r'E:\Programming\Openpose\openpose\openpose\output\push-up'

times = pushUp.pushUpAnalysis(PUSH_UP_FILEPATH)
# times2 = pullUp.pullUpAnalysis(PULL_UP_FILEPATH)
region = []
for time in times:
    print(time)
    region.append(time['Flag'])
# test.getPullUpInfos(PULL_UP_FILEPATH, True)
test.getPushUpInfos(PUSH_UP_FILEPATH, True, region)
