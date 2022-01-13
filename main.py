from selenium import webdriver
import speedtest
import speech_recognition as sr
from text_to_speech import speak
import pywhatkit as kit
import datetime
import pyjokes
import requests
import bs4
import subprocess




r = sr.Recognizer()
speak('Hello, I am a developing voice assistant....i would be glad to take your command and find things that you need')
speak('What can i do for you...')
print()
driver = webdriver.Chrome(executable_path=r'C:\Users\KIIT\Desktop\chromedriver.exe')


def talk(text):
    speak(text)


def take_command():
    global query
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Taking command...")
        query = r.recognize_google(audio, language='en')
        print(f'You said: {query}')

    except Exception as e:
        speak('i could not understand you please repeat again and run once more')
        print("Please repeat..")

    return query.lower()


def run_extreme():
    command = take_command()
    value = False
    explorer = r'C:\Users\KIIT\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\File Explorer.lnk'
    pretzel = r'C:\Users\KIIT\AppData\Local\Programs\PretzelDesktop\Pretzel.exe'
    search = ['can you tell me about ', 'can you tell me what is this', 'can you tell me what is this thing called',
              'what is this thing called', 'please tell me about', 'tell me about', 'who is this person named',
              'who is this person called', 'who is', 'what is', 'search']
    songs = ['play', 'song', 'song named']
    date = ['date', 'what is the date today']
    time = ['time', 'what is the time now']
    joke = ['joke', 'tell a joke']
    weather = ['weather', 'how is']
    speed_test = ['speed test', 'do a speed test']
    open_notepad = ['make a note', 'write', 'open Notepad']
    open_spotify = ['open spotify']
    open_calc = ['open calculator']
    open_explorer = ['open file explorer', 'open explorer']
    open_pretzel = ['open pretzel']
    news = ['tell me news about', 'news']
    about = ['what are you', 'who are you', 'tell me about yourself']

# about bot
    for emp in about:
        if emp in command:
            talk('I am a voice assistant still in development and evolving....i was made by Adesh Senapati..')
            talk('i can do many stuffs for you...but still i am developing so bear with me')
            return

# opening news
    for emp in news:
        if emp in command:
            sliced_command = command.replace(emp, '')
            talk('here are the search results...')
            if 'headlines' in sliced_command:
                com1 = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'showcase' in sliced_command:
                com1 = 'https://news.google.com/showcase?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'covid 19' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'india' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'world' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'local' in sliced_command:
                com1 = 'CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNRE5qZW5GemVnc0tDUzl0THpBelkzcHhjeWdBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNRE5qZW5GektBQVABUAE'
                driver.get(com1)
            elif 'business' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'technology' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'entertainment' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'sports' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'science' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            elif 'health' in sliced_command:
                com1 = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'
                driver.get(com1)
            else:
                com1 = f"https://news.google.com/search?q={sliced_command}"
                driver.get(com1)
            print(sliced_command)
            return
# google searching using selenium
    for emp in search:
        if emp in command:
            command = command.replace(emp, '')
            com = f"https://www.google.com/search?q={command}"
            driver.get(com)
            try:
                result = driver.find_element_by_xpath(
                    '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div/div/span[1]').text
            except:
                result = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]').text
            print(result)
            talk(result)
            value = True

    if value == False:
        # playing songs on youtube using py_what_kit package
        for emp in songs:
            if emp in command:
                command = command.replace(emp, '')
                talk('playing '+command+'.....on Youtube')
                kit.playonyt(command)
                return

# telling the date...this one is extra and its acts as an extra command a user can give..in short useful for date
        for emp in date:
            if emp in command:
                today = datetime.date.today()
                today = str(today)
                print(today)
                talk('today is'+today)
                return

# telling the time
        for emp in time:
            if emp in command:
                mytime = datetime.datetime.now().strftime('%I:%M %p')
                print(mytime)
                talk('the time is'+mytime)
                return

# telling jokes
        for emp in joke:
            if emp in command:
                tell_joke=pyjokes.get_joke()
                print(tell_joke)
                talk(tell_joke)
                return

# telling weather
        for emp in weather:
            if emp in command:
                search = command
                url = f"https://www.google.com/search?q={search}"
                res = requests.get(url)
                soup = bs4.BeautifulSoup(res.text, 'lxml')
                temp = soup.find("div", class_="BNeawe").text
                st = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                data = st.split('\n')
                sky = data[1]
                print(temp)
                print(sky)
                talk("the current temperature is"+temp)
                talk("the current condition of the sky is"+sky)
                return

# doing speed test
        for emp in speed_test:
            if emp in command:
                print('running speedtest...')
                talk('running speed test')
                st = speedtest.Speedtest()
                print('loading server list....')
                talk('loading server list...')
                st.get_servers()
                print('choosing best server...')
                talk('choosing best server....')
                best = st.get_best_server()
                print(f"found:{best['host']} located in {best['country']}")
                talk(f"found:{best['host']} located in {best['country']}")
                print("performing download speed test..")
                talk("performing download speed test..")
                dl=str(round((st.download()/8e+6), 2))
                print("performing upload speed test..")
                talk("performing upload speed test...")
                ul=str(round((st.upload()/8e+6), 2))
                ping_result = str(st.results.ping)
                print('download speed='+dl)
                talk('download speed is'+dl+'mega byte per second')
                print('upload speed='+ul)
                talk('upload speed is'+ul+'mega byte per second')
                print("ping="+ping_result)
                talk('ping is'+ping_result+'milli seconds')

# opening notepad
        for emp in open_notepad:
            if emp in command:
                print('opening notepad...')
                talk('opening notepad..')
                subprocess.Popen(r'notepad.exe', shell=True)
                return

# opening spotify
        for emp in open_spotify:
            if emp in command:
                print('opening spotify...')
                talk('opening spotify')
                subprocess.Popen(r'spotify.exe', shell=True)
                return

# opening calculator
        for emp in open_calc:
            if emp in command:
                print('opening calculator...')
                talk('opening calculator...')
                subprocess.Popen(r'calc.exe', shell=True)
                return

# opening file explorer
        for emp in open_explorer:
            if emp in command:
                print('opening file explorer...')
                talk('opening file explorer...')
                subprocess.Popen(explorer, shell=True)
                return

# opening pretzel
        for emp in open_pretzel:
            if emp in command:
                print('opening pretzel...')
                talk('opening pretzel...')
                subprocess.Popen(pretzel, shell=True)
                return

        else:
            print('I could not understand please repeat')
            talk('i could not understand what you were saying please repeat..am still developing..')


def shut_down():
    cont = ''
    while cont not in ['yes', 'no']:
        cont = (input('Do you wanna run again yes or no')).lower()
    if cont == 'yes':
        talk('please tell me what can i do for you..')
        return True
    else:
        talk('Shutting down...')
        return False


def running_program():
    game_on = True
    while game_on:
        run_extreme()
        game_on = shut_down()
    driver.close()


running_program()



