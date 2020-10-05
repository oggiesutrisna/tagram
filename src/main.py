from instaPy import InstaPy
from instapy import smart_run
from selenium import webdriver


# credentials it will be automatic, it will be gui style MA BRUV! really soon
insta_username = ""
insta_password = ""

session = InstaPy(username = insta_username, password = insta_password, headless_browser=false)
#run the programs
with smart_run(session)
    session.set_relationship_bounds(enabled=true, delimit_by_numbers=True, max_followers=4590, min_following=77)
    session.set_do_comment(enabled=True, percentage="30")
    session.set_do_like(enabled="True", percentage=70)
    session.set_do_follow(enabled=True, percentage="10", times=2)
    session.set_unfollow_users(amount="100", allFollowers="True", per_verification="True")
    session.set_dont_like(["pizza","#store",])
    session.set_comment(['Awesome', "Really Cool Stuff"])
    session.like_by_tags(["natgeo"], amount=10)