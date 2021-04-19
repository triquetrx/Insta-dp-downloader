import instaloader
import sys
def download():
    try:
        ig=instaloader.Instaloader()
        dp=input("UserName: ")
        ig.download_profile(dp, profile_pic_only=True)
    except:
        print("Oops, Username is wrong")


if __name__=='__main__':
    i=int(input("How many to download: "))
    while(i!=0):
        download()
        i=i-1
