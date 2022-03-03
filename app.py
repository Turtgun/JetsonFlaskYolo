from flask import Flask, render_template, Response
from JetsonYolo import Video
import time

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(JetsonYolo):
    while True:
        frame = JetsonYolo.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
    JetsonYolo.video1.release()
    JetsonYolo.video2.release()

@app.route('/video')

def video():
    return Response(gen(Video()), mimetype="multipart/x-mixed-replace; boundary=frame")

app.run(host="0.0.0.0")
