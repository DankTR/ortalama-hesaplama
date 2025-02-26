vize = int(input("Please enter your midterm grade: ")) # we got the midterm grade from the user
final = int(input("Please enter your final grade: ")) # we got the final grade from the user
def calculate(): # we created a function to calculate
    vize_puani = vize * 0.4 # midterm calculation math
    final_puani = final * 0.6 # final calculation math
    average = vize_puani + final_puani # we summed the midterm and final
    return average # we returned the result
print(calculate()) # we printed the result of the function