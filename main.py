import matplotlib
import PyQt5
import os
import sys

matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

WB_START_STRING = 'WHITE BALANCE ADJUSTMENT STEP LOG'
Set_RgbGainOffset_STRING = 'SET_RgbGainOffset'
ColorTemp_0_STRING = '[ SET_WBA_ColorTemp= 0 ]'
ColorTemp_1_STRING = '[ SET_WBA_ColorTemp= 1 ]'
ColorTemp_2_STRING = '[ SET_WBA_ColorTemp= 2 ]'
Factory_Comp_STRING = 'Factory_Comp'
WBA_RESULT_OK = 'WBA_RESULT= OK'
WBA_RESULT_NOK = 'WBA_RESULT= NOK'

file_name = 'HAT2S_T5B_056T49-D51_23.10.2019.TXT'

# Open file
print(sys.path[0])
with open(os.path.join(sys.path[0], file_name), "r") as f:
    listOfLines = f.read().splitlines()

Number_Of_TV = 0
Total_Line_Numbers = len(listOfLines)
Factory_Comp_list = []
Value_list = []
Color_Temp_list = []
u_list = []
v_list = []
Lv_list = []
Tv_Number_list = []
WBA_Result_list = []
current_line_str = ''
str_splt = ''
str_sub = ''
index_uv = 0
index_uv_keep = 0
line_index = 0
current_line_index = -1

while True:
    current_line_index += 1
    if current_line_index == Total_Line_Numbers:
        break

    current_line_str = listOfLines[current_line_index]
    if current_line_str == WB_START_STRING:
        Number_Of_TV += 1
        while True:
            current_line_index += 1
            current_line_str = listOfLines[current_line_index]
            index_uv_keep = index_uv
            if current_line_str == ColorTemp_0_STRING:
                current_line_index += 2
                # GET LINE-->[ CA310_MINOLTA_Measurement:
                current_line_str = listOfLines[current_line_index]
                str_sub = current_line_str.split("	")

                for x in range(3):
                    index_uv += x
                    u_list.insert(index_uv, str_sub[1][-4:])
                    v_list.insert(index_uv, str_sub[2][-4:])
                    Lv_list.insert(index_uv, str_sub[3][-5:-2])
                    Color_Temp_list.insert(index_uv, '0')
                    Factory_Comp_list.insert(index_uv, str(x))
                    Value_list.insert(index_uv, '128')
                    Tv_Number_list.insert(index_uv, str(Number_Of_TV))

                while current_line_str != ColorTemp_1_STRING:
                    current_line_index += 1
                    current_line_str = listOfLines[current_line_index]
                    str_splt = current_line_str.split(":")

                    if (str_splt[0][2:]) == Set_RgbGainOffset_STRING:
                        # GET LINE-->[ SET_RgbGainOffset:
                        str_sub = current_line_str.split("	")

                        Color_Temp_list.insert(index_uv, str_sub[1][-1:])
                        Factory_Comp_list.insert(index_uv, str_sub[2][-1:])
                        Value_list.insert(index_uv, str_sub[3][7:10])

                        # GET LINE-->[ CA310_MINOLTA_Measurement:
                        current_line_index += 1
                        current_line_str = listOfLines[current_line_index]
                        str_sub = current_line_str.split("	")
                        u_list.insert(index_uv, str_sub[1][-4:])
                        v_list.insert(index_uv, str_sub[2][-4:])
                        Lv_list.insert(index_uv, str_sub[3][-5:-2])
                        Tv_Number_list.insert(index_uv, str(Number_Of_TV))
                        index_uv += 1

            if current_line_str == ColorTemp_1_STRING:
                current_line_index += 2
                # GET LINE-->[ CA310_MINOLTA_Measurement:
                current_line_str = listOfLines[current_line_index]
                str_sub = current_line_str.split("	")

                for x in range(3):
                    index_uv += x
                    u_list.insert(index_uv, str_sub[1][-4:])
                    v_list.insert(index_uv, str_sub[2][-4:])
                    Lv_list.insert(index_uv, str_sub[3][-5:-2])
                    Color_Temp_list.insert(index_uv, '1')
                    Factory_Comp_list.insert(index_uv, str(x))
                    Value_list.insert(index_uv, '128')
                    Tv_Number_list.insert(index_uv, str(Number_Of_TV))

                while current_line_str != ColorTemp_2_STRING:
                    current_line_index += 1
                    current_line_str = listOfLines[current_line_index]
                    str_splt = current_line_str.split(":")

                    if (str_splt[0][2:]) == Set_RgbGainOffset_STRING:
                        # GET LINE-->[ SET_RgbGainOffset:
                        str_sub = current_line_str.split("	")

                        Color_Temp_list.insert(index_uv, str_sub[1][-1:])
                        Factory_Comp_list.insert(index_uv, str_sub[2][-1:])
                        Value_list.insert(index_uv, str_sub[3][7:10])

                        # GET LINE-->[ CA310_MINOLTA_Measurement:
                        current_line_index += 1
                        current_line_str = listOfLines[current_line_index]
                        str_sub = current_line_str.split("	")
                        u_list.insert(index_uv, str_sub[1][-4:])
                        v_list.insert(index_uv, str_sub[2][-4:])
                        Lv_list.insert(index_uv, str_sub[3][-5:-2])
                        Tv_Number_list.insert(index_uv, str(Number_Of_TV))
                        index_uv += 1

            if current_line_str == ColorTemp_2_STRING:
                current_line_index += 2
                # GET LINE-->[ CA310_MINOLTA_Measurement:
                current_line_str = listOfLines[current_line_index]
                str_sub = current_line_str.split("	")

                for x in range(3):
                    index_uv += x
                    u_list.insert(index_uv, str_sub[1][-4:])
                    v_list.insert(index_uv, str_sub[2][-4:])
                    Lv_list.insert(index_uv, str_sub[3][-5:-2])
                    Color_Temp_list.insert(index_uv, '2')
                    Factory_Comp_list.insert(index_uv, str(x))
                    Value_list.insert(index_uv, '128')
                    Tv_Number_list.insert(index_uv, str(Number_Of_TV))

                while current_line_str != WBA_RESULT_OK:
                    current_line_index += 1
                    current_line_str = listOfLines[current_line_index]
                    str_splt = current_line_str.split(":")

                    if (str_splt[0][2:]) == Set_RgbGainOffset_STRING:
                        # GET LINE-->[ SET_RgbGainOffset:
                        str_sub = current_line_str.split("	")

                        Color_Temp_list.insert(index_uv, str_sub[1][-1:])
                        Factory_Comp_list.insert(index_uv, str_sub[2][-1:])
                        Value_list.insert(index_uv, str_sub[3][7:10])

                        # GET LINE-->[ CA310_MINOLTA_Measurement:
                        current_line_index += 1
                        current_line_str = listOfLines[current_line_index]
                        str_sub = current_line_str.split("	")
                        u_list.insert(index_uv, str_sub[1][-4:])
                        v_list.insert(index_uv, str_sub[2][-4:])
                        Lv_list.insert(index_uv, str_sub[3][-5:-2])
                        Tv_Number_list.insert(index_uv, str(Number_Of_TV))
                        index_uv += 1

            if current_line_str == WBA_RESULT_OK:
                for n in range(index_uv_keep, index_uv):
                    WBA_Result_list.insert(n, 'OK')
                break
            if current_line_str == WBA_RESULT_NOK:
                print('++++++++++++++++++')
                for n in range(index_uv_keep, index_uv):
                    WBA_Result_list.insert(n, 'NOK')
                break

# Adjust Result TEXT FILE
String_To_Write = ' '
Tab_Str = '   '
End_Line = '\n'
Data_Mined_File_Path = sys.path[0] + '/Data_Mined.txt '
File_Result = open(Data_Mined_File_Path, 'w')

print(Number_Of_TV)

for i in range(index_uv):
    String_To_Write = Color_Temp_list[i] + Tab_Str + Factory_Comp_list[i] + Tab_Str + Value_list[i] + Tab_Str + u_list[
        i] + Tab_Str + v_list[i] + Tab_Str + Lv_list[i] + Tab_Str + Tv_Number_list[i] + Tab_Str + WBA_Result_list[
                          i] + End_Line
    File_Result.writelines(String_To_Write)

print(current_line_index)

print(Color_Temp_list)
print(Factory_Comp_list)
print(Value_list)
print(u_list)
print(v_list)
print(Lv_list)
