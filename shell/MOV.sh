#ffmpegを使って連番画像の動画化
#!/bin/sh
rm Move.mp4
ffmpeg -r 12 -i ./IMG%02d.png -vcodec libx264 -pix_fmt yuv420p  Move.mp4
