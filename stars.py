x = [4,6,1,3,5,7,25]

def draw_stars(arr):
	print "array = ",arr
	for i in range(0,len(arr)):
		star_result = ""
		for item in range(0,x[i]):
			star_result += "*"
		print star_result

draw_stars(x)

# Part 2

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


def draw_stars2(arr):
	print "array = ",arr
	for i in range(0,len(arr)):
		if isinstance(arr[i], str) == False:
			arr[i] = "*" * arr[i]
		else:
			arr[i] = arr[i][0].lower() * len(arr[i])
		print arr[i]

draw_stars2(y)