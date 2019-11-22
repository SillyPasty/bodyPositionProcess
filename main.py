import test
import analysis

FILEPATH = r'E:\Programming\Openpose\openpose\openpose\output\push-up'

times = analysis.pushUpTimesCount(FILEPATH)
print(times)
test.getPushUpInfos(FILEPATH)
