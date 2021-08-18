import subprocess
from .ctpdf import convert_to_pdf
from .checksum import check
#import re


def rustscan_script(ip, user_name, function_name):
    #"--range", "1-10000"
    p = subprocess.run(["rustscan", "-a", f"{ip}", "--ulimit", "50000"],
                       capture_output=True, encoding="utf-8")
    pre_output = p.stdout.split('\n')
    #pre_output = ' , '.join(str(pre_output))
    #ansi_escape = re.compile(r'(?:\[\d?\;?\d+\w+)')
    #result = ansi_escape.sub('', pre_output)
    pre_output = pre_output[10:-3]
    delete_list = [
                   "increasing ulimit",
                   "lowering it",
                   "the timeout",
                   "Starting Nmap",
                   "nmap","Nmap",
                   "file","be run"
                   ]

    output = pre_output
    for line in pre_output:
        for word in delete_list:
            if word in line:
                output.remove(line)
                break

    if check():
        convert_to_pdf(output, user_name, ip, function_name)

    else:
        exit(1)


#user_name = "sarayloo"
#ip = "192.168.1.0/30"
#function_name = "livehost"
#
#rustscan_script(ip, user_name, function_name)