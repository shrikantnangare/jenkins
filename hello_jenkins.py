#! /usr/bin/env python3
import os
if __name__ == "__main__":
    print("Hello from jenkins")
    for root,dirs,files in os.walk("."):
        for f in files:
            print(os.path.join(root,f))
    with open("/home/shrikant/temp/jenkins_test.txt","w") as fwriter:
        for root,dirs,files in os.walk("."):
            for f in files:
                fwriter.write(os.path.join(root, f) + os.linesep)



#shrikant
