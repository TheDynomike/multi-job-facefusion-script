[general]
source_paths =
target_path =
output_path = D:\yt\stls\swaps\tmp

[misc]
force_download =
skip_download =
headless =
log_level =

[execution]
execution_providers = cuda
execution_thread_count = 27
execution_queue_count = 2

[memory]
video_memory_strategy = tolerant
system_memory_limit =

[face_analyser]
face_analyser_order = left-right
face_analyser_age = adult
face_analyser_gender = female
face_detector_model =
face_detector_size =
face_detector_score = .35
face_landmarker_score =

[face_selector]
face_selector_mode = reference
reference_face_position =
reference_face_distance =
reference_frame_number =

[face_mask]
face_mask_types = box region
face_mask_blur = 0.3
face_mask_padding = 0 0 0 0
face_mask_regions = skin left-eyebrow right-eyebrow left-eye glasses right-eye nose mouth upper-lip lower-lip

[frame_extraction]
trim_frame_start =
trim_frame_end =
temp_frame_format = bmp
keep_temp =

[output_creation]
output_image_quality =
output_image_resolution =
output_video_encoder =
output_video_preset = veryfast
output_video_quality = 80
output_video_resolution = 1280x720
output_video_fps = 30
skip_audio =

[frame_processors]
frame_processors = face_swapper face_enhancer
face_debugger_items =
face_enhancer_model = gfpgan_1.4
face_enhancer_blend = 80
face_swapper_model = inswapper_128_fp16
frame_colorizer_model =
frame_colorizer_blend =
frame_enhancer_model =
frame_enhancer_blend =
lip_syncer_model =

[uis]
ui_layouts =
