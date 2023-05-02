
#Grace Meredith
#CS333 Testing & Devops final project
#2 May 2023

#This project was my hw1 assignment in Fall 2022 Design Patterns re-written in python.

def getLocation():
	print("Welcome to shaved ice!")

	while True:

		l = input("What location are you? enter 'k' or 's'")

		if 'k' in l or 's' in l:
			break;
	if 'k' in l:
		return Kiosk()
	else:
		return Store()

def main():
    loc = getLocation()
	loc.order()
	loc.pay()

if __name__ == "__main__":
	main()