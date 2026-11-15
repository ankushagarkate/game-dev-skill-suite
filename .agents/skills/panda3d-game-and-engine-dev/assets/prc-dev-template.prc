# Panda3D Development Config.prc Template
# Load via loadPrcFileData("", ...) BEFORE importing/creating ShowBase()

window-title Panda3D Dev Build
win-size 1280 720
fullscreen #f
sync-video #t
show-frame-rate-meter #t

# Profiling & Diagnostics
want-pstats #f
notify-level-pgraph warning
notify-level-bullet warning

# Audio (OpenAL)
audio-library-name p3openal_audio
audio-volume 0.8

# Asset Caching
model-cache-dir $MAIN_DIR/.panda_cache
model-cache-textures #t
