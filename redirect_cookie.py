# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

REDIRECT_URL = 'http://index.com:5000/rd'


@app.route('/index.html')
def index():
    return render_template('redirect_index.html', redirect_js_url=REDIRECT_URL)


@app.route('/rd')
def redirect1():
    dest_host = 'index805.com'
    dest_url = 'http://{}:5000/static/rd.js'.format(dest_host)
    return redirect(dest_url, code=302)


'''
  var host_name = window.location.hostname;
  if (host_name.startsWith('www')) {
    host_name = host_name.substr(4);
  }
  var url = 'd.' + host_name + '/static/rd.js';
  document.write('<script src="http://' + url + '"> <\/script>');

'''



@app.route('/static/rd.js')
def redirect_js():
    dest_host = 'index805.com'
    print(1)
    js_template = '''
    var host_name = window.location.hostname;
    var dest_host_name = 'index805.com'
    if (host_name != dest_host_name) {
      var new_url = window.location.protocol + "//" + dest_host_name + window.location.pathname + window.location.search;
      //window.location.href=new_url;
    }
    '''
    resp = make_response(js_template)
    print(2)
    resp.set_cookie('is_redirected', max_age=3600 * 24, domain='index805.com')
    print(3)
    return resp


@app.route('/request_info')
def request_info():
    return render_template("request_info.html", headers=request.headers)
