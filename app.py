__author__ = 'spousty'


from bottle import route, run

@route('/')
def index():
    return "<h1> Hello Corelogic OpenShift</h1></BR>
    <h2> Hello Corelogic OpenShift test 1</h2>"
 
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
