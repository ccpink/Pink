"""
Student Name:Charles    
Program Title:Paint Needed To Paint Walls  
Description:It has variables that can be plugged into for height and
length of both walls it then calculates the dimensions of the walls
then it calculates the combined area of the 4 walls then it divides 
it by a gallon of paint and rounds up     

https://www.dotnetperls.com/math-python Used this to understand how to round up

I accidentally uploaded that one early sorry
"""

def main():

    import math

    RoomHeight1 = input("Enter room height for wall 1 : ")
    RoomHeight2 = input("Enter room height for wall 2 : ")
    RoomLength1 = input("Enter room length for wall 1 : ")
    RoomLength2 = input("Enter room length for wall 2 : ")

    RH1 = int(RoomHeight1) 
    RH2 = int(RoomHeight2)
    RL1 = int(RoomLength1)
    RL2 = int(RoomLength2)

    Dimensions1 = (RL1*RH1)
    Dimensions2 = (RL2*RH2)

    Area = (2*(Dimensions1 + Dimensions2))

    UnroundedPaint = (Area/150)

    PaintNeeded = math.ceil(UnroundedPaint)

    print("You need", PaintNeeded, "buckets worth.")



if __name__ == "__main__":
    main()

