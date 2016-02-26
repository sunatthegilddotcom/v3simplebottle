__author__ = 'spousty'


from bottle import route, run

@route('/')
def index():
    return "<h1> Hello Corelogic OpenShift</h1>"
    return "<h2> CI/CD with agile development</h2>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
