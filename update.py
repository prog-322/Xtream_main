#!/usr/bin/python3
import os
import sys

baseDir = "/home/xtreamcodes/"
PHPDir = baseDir + "bin/php/bin/php"

if __name__ == "__main__":
    # stop xtreamcodes
    os.system(f"sudo sh {baseDir}service.sh stop")
    # move update files
    os.system(f"rsync -a {baseDir}update/ {baseDir}")
    # add permissions
    os.system('sudo chown -R xtreamcodes:xtreamcodes "%s"' % baseDir)
    os.system(f"sudo sh {baseDir}permissions.sh")
    # Transferring control further
    os.system("sudo %s %stools/update.php post-update" % (PHPDir, baseDir))
    # start xtreamcodes
    os.system(f"sudo sh {baseDir}service.sh start")
    # remove update_tmp
    os.system(f"rm -rf {baseDir}update/")
    sys.exit(1)