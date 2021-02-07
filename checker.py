from colorama import Fore, init, Style
import threading, requests
import ctypes, time, os

class Checker:
    def __init__(self):
        self.proxies = []
        self.counter = 0
        self.good = 0
        self.bad = 0

    def save(self, proxy):
        try:
            with open("Good.txt", "a") as f:
                f.write("{}\n".format(proxy))
        except:
            pass
       
    def session(self):
        session = requests.Session()
        session.trust_env = False
        return session

    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW("Proxy Checker | Good: {0} | Bad: {1} | Checked: {2} | Remaining: {3}".format(self.good, self.bad, (self.good + self.bad), (len(self.proxies) - (self.good + self.bad))))

    def check_proxy(self, proxy):
        try:
            self.session().get(self.url, proxies = {"https": "https://{}".format(proxy)})
            self.good += 1
            self.save(proxy)
        except:
            self.bad += 1
        self.title()

    def proxy(self):
        if os.path.exists("proxies.txt"):
            with open("proxies.txt", "r") as f:
                for proxy in f:
                    proxy = proxy.strip("\n")
                    self.proxies.append(proxy)
            return
        os.system("cls"); print("\n{0} > {1}{2}Error: No proxy file found".format(Fore.RED, Fore.WHITE, Style.BRIGHT)); time.sleep(5); exit()
    
    def main(self):
        os.system("cls"); ctypes.windll.kernel32.SetConsoleTitleW("Proxy Checker")
        self.proxy()
        self.url = str(input("\n{0} > {1}{2}URL: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.threads = int(input("{0} > {1}{2}Threads: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))

        def thread_starter():
            self.check_proxy(self.proxies[self.counter])
        
        while True:
            if threading.active_count() <= self.threads:
                threading.Thread(target = thread_starter).start()
                self.counter += 1
            if self.counter >= len(self.proxies): break

Checker().main()
input()
