# m3u8-to-mp4

Download unsigned m3u8 to local mp4

# Why use this? 

Smaller VOD sites have been putting their content behind m3u8 links to prevent people from saving their content directly. If you can access the m3u8 link in the page source, this tool is significantly faster than downloading via VLC or other real-time capture methods. This will save the file as quickly as the host can make it available, often many times faster than playback speed.

# Assumptions
CSV parser assumes your list is arranged as: filename, http://<linktoplace>.m3u8 


# Depencenies: 
python3.7,
https://github.com/aminyazdanpanah/python-ffmpeg-video-streaming,
csv,
ffmpeg
