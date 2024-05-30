from instagram_unfollowers_final import *

first_input()
second_input()
create_lists()

while True:
	command = """
	Sizi takip etmeyenleri görmek için 1'e,
	Sizi takip etmeyenlerin sayısı için 2'ye,
	Sizin takip etmediklerinizi görmek için 3'e,
	Sizin takip etmediklerinizin sayısı için 4'e,
	Her şeyi görmek için 5'e tıklayın,
	Çıkmak için kapat yazın...\n
	"""
	user_choice = input(command)
	print("\nSeçiminiz: " + user_choice)

	if user_choice == "kapat":
		break
	if user_choice == "1":
		get_list_not_following_you()
	elif user_choice == "2":
		get_number_not_following_you()
	elif user_choice == "3":
		get_list_you_dont_follow()
	elif user_choice == "4":
		get_number_you_dont_follow()
	elif user_choice == "5":
		get_number_not_following_you()
		get_list_not_following_you()
		get_number_you_dont_follow()
		get_list_you_dont_follow()


