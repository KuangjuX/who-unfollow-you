import sys
from unfollow import unfollow

def main():
    username = sys.argv[1]
    unfollow(username)

if __name__ == '__main__':
    main()