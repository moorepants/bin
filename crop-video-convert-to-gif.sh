# crop the video
ffmpeg -i P5210592.MOV -strict -2 -filter:v "crop=837:676:704:396" cropped.mov
# convert to jpegs
mkdir frames
ffmpeg -i cropped.mov -r 5 'frames/frame-%03d.jpg'
cd frames
# convert to gif
convert -delay 20 -loop 0 *.jpg falkor-eyes.gif
# resize to make it smaller
convert falkor-eyes.gif -coalesce temporary.gif
convert -size 836x676 temporary.gif -resize 400x323 smaller.gif
