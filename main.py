import test
import analysis

FILEPATH = r'E:\Programming\Openpose\openpose\openpose\output\push-up'

times = analysis.pushUpTimesCountByTendency(FILEPATH)
region = []
for time in times:
    print(time)
    region.append(time['Flag'])
test.getPushUpInfos(FILEPATH, False, region)
