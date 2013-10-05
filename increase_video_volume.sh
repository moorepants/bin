#!/usr/bin/bash

# increase_video_volume.sh /path/to/input/file /path/to/output/file volumepercent
# volume_percent: 256=100%
# example:
# increase_video_volume.sh /home/moorepants/Videos/test.mp4 /home/moorepants/Videos/test-loud.mp4 1280

avconv -i $1 -vol $3 -vcodec copy $2
# this is the audio filter version were the third argument is 1.0 for same
# volume and things like 1.5 for higher or 0.5 for lower. The above will be
# depreciated.
#avconv -i $1 -af "volume=$3" -vcodec copy $2
