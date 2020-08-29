from flask import Flask, render_template, Response
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', type=int, help='It determines the mode')
args = parser.parse_args()

# 0 -> webcam, 1 -> picamera
if args.mode == 0:
	from camera import Camera
else:
    from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(
        gen(Camera()),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
