import random 

def born():
	alive = True 
	return alive 

def learn():
	print("love")

def enjoy():
    print("joy")

def share(): 
    print("retribute")

def main():
	yearsOfLiving = random.randint(0,100)
	alive = born() 
	for year in range(0, yearsOfLiving):
		learn()
		enjoy()
		share()
			
if __name__ == "__main__":
    main()