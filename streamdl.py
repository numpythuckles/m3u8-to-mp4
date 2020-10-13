import ffmpeg_streaming
import csv
from ffmpeg_streaming import Formats

with open('<your list of m3u8s>.csv', newline='') as csvfile:
	data = list(csv.reader(csvfile))


for x in range(len(data)):
	filename = data[x][0]
	streamlink = data[x][1]
	print("Writing File: " + filename)
	video = ffmpeg_streaming.input(streamlink)
	stream = video.stream2file(Formats.h264())
	stream.output('<your local directory>' + filename + '.mp4')
