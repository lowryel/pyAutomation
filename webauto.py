import webbrowser

def webauto():
    browser = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(browser).open('facebook.com')
    
webauto()
    # URLS = (
    #     'google.com',
    #     'facebook.com',
    #     'gmail.com'
    # )

    # for url in URLS:
    #     print("Opening:", url)
    #     webbrowser.get(browser).open(url)
     


