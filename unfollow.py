"""
Author: Kevin Lin
Date: 2023-07-05
Description: A script that uses the instagrapi library to unfollow users that don't follow you back.
             Uses some of the best practices from https://adw0rd.github.io/instagrapi/usage-guide/best-practices.html]
             to try and not arouse suspicion. I've run this a few times without any issues though.

"""
import os

from instagrapi import Client
from dotenv import load_dotenv
load_dotenv()

# 0. Enter your Instagram credentials here
username = os.environ.get("IG_USERNAME")
password = os.environ.get("IG_PASSWORD")
verification_code = os.environ.get("IG_2FA")


def check_if_cached_exists(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return f.read().splitlines()
    else:
        return None


def get_followers() -> list:
    if follower_list := check_if_cached_exists("followers.txt") is not None:
        print("Using cached followers list. Delete followers.txt and rerun if you want to refresh.")
    else:
        print("Getting followers")
        followers = client.user_followers(user_id)
        print(f"Found {len(followers)} followers")
        follower_list = []
        for ig_id, follower in followers.items():
            try:
                # sometimes the user doesn't have a username, not really sure why, maybe they're private/banned
                follower_list.append(follower.username)
            except AttributeError as e:
                print(f"User {ig_id} has no username, skipping them")
                continue

        # Save the followers to a file
        with open("followers.txt", "w") as followers_file:
            followers_file.write("\n".join(follower_list))
    return follower_list


def get_following() -> list:
    if following_list := check_if_cached_exists("following.txt") is not None:
        print("Using cached following list. Delete following.txt and rerun if you want to refresh.")
    else:
        print("Getting following")
        following = client.user_following(user_id)
        print(f"Found {len(following)} following")
        following_list = []
        for ig_id, follower in following.items():
            try:
                following_list.append(follower.username)
            except AttributeError as e:
                print(f"User {ig_id} has no username, skipping them")
                continue

        # Save the following to a file
        with open("following.txt", "w") as following_file:
            following_file.write("\n".join(following_list))
    return following_list


if __name__ == '__main__':
    # 1. Log into Instagram
    client = Client()
    client.delay_range = [1, 3]  # delay between requests to seem more human

    print("Trying to log in...")
    client.login(username, password, verification_code=verification_code)
    user_id = str(client.user_id)
    print("Successfully logged in.")

    # 2. Get a list of your followers.
    follower_usernames = get_followers()

    # 3. Get a list of users you're following.
    following_usernames = get_following()

    # 4. Find users you follow that don't follow you back
    not_following_back = [user for user in following_usernames if user not in follower_usernames]

    # Save the list of users to a file
    if os.path.exists("not_following_back.txt"):
        os.remove("not_following_back.txt")
    with open("not_following_back.txt", "w") as file:
        file.write("\n".join(not_following_back))

    # 5. Prompt user to curate the list of users to unfollow (e.g. maybe you follow celebrities)
    input("Open not_following_back.txt and curate the list (delete people you want to keep following). "
          "Don't leave any blank lines. Remember to save. Press enter in this terminal when done.")

    # 6. Unfollow users that don't follow you back
    with open("not_following_back.txt", "r") as file:
        curated_unfollow_list = file.read().splitlines()

    for user in curated_unfollow_list:
        print(f"Unfollowing {user}")
        client.user_unfollow(client.user_id_from_username(user))

    # 7. Log out of your Instagram account
    client.logout()
