'''
from rich.console import Console
from rich.traceback import install
install()

def add (x, y):
    r= 'ok'
    rl = x+y
    console.log("Adding two numbers.", log_locals=True)
    console.log(f"Return value:{rl} ok\n\n")
    pass

console = Console(record=True)

try:
    a= " mostra"
    b=" somente"
    add(a,b)
    add(b,a)
    add(b,b)
except:
    console.print_exception()


console.save_html("demo.html")

'''
#afor

# flask_app.py
from flask import Flask, send_file
app = Flask(__name__)

@app.route('/api/video')
def get_video():
    return send_file(r"C:\Users\igorp\OneDrive\Documentos\docker_test1\Ninja_Kamui.mp4",mimetype="video/mp4",as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)

# app.py
