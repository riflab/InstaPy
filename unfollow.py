"""
This template is written by arif.darmawan@riflab.com
What does this quickstart script aim to do?
- This is my simple but effective script.
"""

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
# from instapy import Settings
# import schedule
import time
import sys
import os

insta_username = sys.argv[1]
insta_password = sys.argv[2]

ammount_number = 20 
# userTarget = ['zaidulakbar', sys.argv[1]]
# userTarget = ['khalidbasalamahofficial', 'madu.abuhafs']

workspace = os.getcwd()+"\\"+sys.argv[1]+"\\"
set_workspace(workspace)
# Settings.database_location = workspace + "\\db\\instapy_{}.db".format(insta_username)
# set_workspace("D:\\git\\docinstapy\\")

def job():
    session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
    with smart_run(session):
        # general settings
        # session.set_relationship_bounds(enabled=False,
        #                                 potency_ratio=None,
        #                                 delimit_by_numbers=True,
        #                                 max_followers=6000,
        #                                 max_following=3000,
        #                                 min_followers=30,
        #                                 min_following=30)
        
        session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=20,
                              peak_likes_daily=150,
                               peak_comments_hourly=20,
                               peak_comments_daily=150,
                                peak_follows_hourly=10,
                                peak_follows_daily=75,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)

        # session.set_user_interact(amount=ammount_number, randomize=True, percentage=80)
        # session.set_do_follow(enabled=False, percentage= 70)
        # session.set_do_like(enabled=True, percentage= 100)
        # session.set_comments(['Assalamualaikum... Sehat selalu','Assalamualaikum'])
        # session.set_do_comment(enabled=True, percentage= 60)
        # session.interact_user_followers(userTarget, amount=ammount_number*10, randomize=True)
        # session.interact_user_following(userTarget, amount=ammount_number*10, randomize=True)
        # unfollow activity
        session.set_dont_include(['arif.darma1', 'madu.abuhafs', 'umrahtravel.id','tokoalhaf','alhafpustaka','riflabcom','darmawanpropertindo','endahsofakomaladewi'])
        session.unfollow_users(amount=ammount_number, nonFollowers=True, style="RANDOM", sleep_delay=300)
        # follow activity
        # session.follow_user_followers(['khalidbasalamahofficial'], amount=ammount_number, randomize=False, interact=True, sleep_delay=240)
        # Joining engagement pods
        # session.join_pods(topic='general', engagement_mode='no_comments')

#schedule.every().day.at("06:00").do(job)
#schedule.every().day.at("12:22").do(job)
#schedule.every().day.at("15:42").do(job)
#schedule.every().day.at("19:00").do(job)
#schedule.every().day.at("20:30").do(job)

while True:
    # schedule.run_pending()
    try:
        job()
        a = 60*60*1
    except:
        a = 60
    print()
    print()
    print('Istirahat dulu bos ' + str(a) + ' detik')
    print()
    print()
    time.sleep(a)

