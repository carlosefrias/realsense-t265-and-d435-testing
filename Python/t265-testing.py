import pyrealsense2 as rs

pipe = rs.pipeline()

cfg = rs.config()
cfg.enable_stream(rs.stream.pose)

pipe.start(cfg)

try:
    for _ in range(5000):
        frames = pipe.wait_for_frames()
        pose = frames.get_pose_frame()
        if pose:
            data = pose.get_pose_data()
            print(f"Frame: {pose.frame_number}\nPosition: {data.translation}\nVelocity: {data.velocity}\nAccelearion: {data.acceleration}")
except:
    print("something bad happened")
finally:
    pipe.stop()