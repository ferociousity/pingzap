import subprocess
import speedtest

def install_speedtest_cli():
    try:
        subprocess.check_call(["pip", "install", "speedtest-cli"])
    except subprocess.CalledProcessError:
        print("Error installing speedtest-cli. Make sure you have pip installed.")

def main():
    install_speedtest_cli()

    st = speedtest.Speedtest()
    option = int(input('''What speed do you want to test:
    1) Download Speed
    2) Upload Speed
    3) Ping
    Your Choice: '''))

    if option == 1:
        print("Download Speed:", st.download())
    elif option == 2:
        print("Upload Speed:", st.upload())
    elif option == 3:
        servernames = []
        st.get_servers(servernames)
        print("Ping:", st.results.ping)
    else:
        print("Please enter the correct choice!")

if __name__ == "__main__":
    main()
