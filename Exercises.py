


"""
str = '[ CA310_MINOLTA_Measurement: 	u= 1900	v= 4306	Lv= 306 ]'
str_splt = str.split("	")
#print(data[0])

print(str_splt[1][-4:])
print(str_splt[2][-4:])
print(str_splt[3][-5:])

#print(data[2])
#print(data[3])







        #First Measurement
        current_line_number += 4
        str_sub = current_line.split("	")
        u_list[index] = str_sub[1][-4:]  #Get u value
        v_list[index] = str_sub[2][-4:]  #Get v value
        Lv_list[index] = str_sub[3][-5:] #Get Lv value
        Factory_Comp_list[index] = 'X'   #No setting
        Value_list[index] = 'X'          #No setting
        index +=1

file_path = '/home/murat/Projects/Workbench/Data_Science/Data_Analytics_White_Blance/DATA/HAT2S_T5B_056T49-D51_23.10.2019.TXT'

# Open file
fileHandler = open(file_path, "r")

# Get All lines
listOfLines = fileHandler.readlines()
Total_Line_Numbers = len(listOfLines)
#print('Total_Line_Numbers= ',Total_Line_Numbers)

print(listOfLines[34])
fileHandler.close()

"""
Color_Temp = []
Factory_Comp_list = []
Value_list = []
index_uv = 1
current_line_str = '[ SET_RgbGainOffset: 	ColorTempID= 7	Factory_Comp= 0	VALUE= 124 ]'
str_splt = current_line_str.split(":")
str_sub = current_line_str.split("	")

#print(str_sub)
#print(str_sub[1][-1:])


A = '[ CA310_MINOLTA_Measurement: 	u= 1893	v= 4461	Lv= 335 ]'
sub_A = A.split("	")
print(str_sub[3][-5:-2])



for i in range(1, 5):
    Factory_Comp_list.insert(i, str_sub[1][-1:])
    #Factory_Comp_list.append(str_sub[1][-1:])  # Get "Comp Type" value

Factory_Comp_list.pop(1)
Factory_Comp_list.insert(1, 12)



#print(Factory_Comp_list)



