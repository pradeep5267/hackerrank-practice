#%%
import subprocess

def main():
    subprocess.call(['sudo', 'cd', 'steam', 'remove', 'purge'])
    cmd_list = [
        'cd ~',
        'sudo apt-get remove steam',
        'sudo apt-get purge steam',
        'rm -rf ~/.local/share/Steam && rm -rf ~/.steam',
        'cd ~/.local/share && rm -rf Steam',
        'rm ~/.steampath',
        'rm ~/.steampid'
        ]
    for i in cmd_list:
        subprocess.run(i, shell=True)

if __name__ == '__main__':
    main()