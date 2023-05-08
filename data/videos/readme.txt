
ffmpeg -framerate 30 -pattern_type glob -i './debug_01/*.jpg'  -c:v libx264 -pix_fmt yuv420p debug_01.mp4
