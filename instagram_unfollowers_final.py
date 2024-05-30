import json

follower_names = []
def first_input():
	file_followers = input("Takipçilerinizin dosya uzantısını giriniz: ")
	with open(file_followers) as f:
		all_follower_data = json.load(f)

	global follower_names

	for follower in all_follower_data:
		follower_name = follower['string_list_data'][0]['value']
		follower_names.append(follower_name)



following_names = []
def second_input():
	file_following = input("\nTakip ettiklerinizin dosya uzantısını giriniz: ")
	with open(file_following) as f:
		all_following_data = json.load(f)

	global following_names

	for following in all_following_data['relationships_following']:
		following_name = following['string_list_data'][0]['value']
		following_names.append(following_name)






list_not_following_you = []
list_you_dont_follow = []
def create_lists():
	global following_names
	global list_not_following_you
	for user in following_names:
		if user not in follower_names:
			list_not_following_you.append(user)

	global list_you_dont_follow
	for user in follower_names:
		if user not in following_names:
			list_you_dont_follow.append(user)




def get_list_not_following_you():
	print(f"\nSizi takip etmeyenler: {list_not_following_you}")

def get_number_not_following_you():
	print(f"\nSizi takip etmeyenlerin sayısı: {len(list_not_following_you)}")

def get_list_you_dont_follow():
	print(f"\nSizin takip etmedikleriniz: {list_you_dont_follow}")

def get_number_you_dont_follow():
	print(f"\nSizin takip etmediklerinizin sayısı: {len(list_you_dont_follow)}")

