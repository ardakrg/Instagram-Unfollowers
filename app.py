"""
Instagram Unfollowers, see the unfollowers on Instagram
Copyright (C) 2024 ardakrg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from instagram_unfollowers_final import *

gnu = """
Instagram Unfollowers  Copyright (C) 2024  ardakrg
This program comes with ABSOLUTELY NO WARRANTY;
for details read the license.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
print(gnu)
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


