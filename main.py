#
# main.py
#
# Generic main who only call the main_local if exist
#
# In your main_local, you can run all your tests as you want
# Example in main_local.py :
# if __name__ == '__main__':
#     exec(open('FeatureTests\AnimationDemo\Test.py').read())
#

if __name__ == '__main__':

    try:
        exec(open('main_local.py').read())
    except FileNotFoundError:
        pass
