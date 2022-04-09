import subprocess as sb

def cancelpoweroff():
    sb.run(['shutdown', '-c'])

#cancelpoweroff()