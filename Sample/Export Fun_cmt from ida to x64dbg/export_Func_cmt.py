import idautils
import idaapi

ea = BeginEA()
module =idaapi.get_root_filename()
imagebase = idaapi.get_imagebase()

f  = open("D:\\Func.txt", "w+")
# here we will export all functions name and (start,End)
for funcea in Functions(SegStart(ea), SegEnd(ea)):
    functionName = GetFunctionName(funcea)
    functionStart = "0x%08x"% (funcea - idaapi.get_imagebase())
    functionEnd = "0x%08x"%( idc.find_func_end(funcea)  - idaapi.get_imagebase())
    print functionName,functionStart,functionEnd   
    output="lable"+";" + functionName+";" + functionStart + ";" + functionEnd + "\n" 
    f.write(output)
# here we will export all comments    
for function in idautils.Functions():
    for address in idautils.FuncItems(function):
        if idc.get_cmt(address,0) is not None:
             output= "comments"+";" + idc.get_cmt(address,0) + ";" + "0x%08x"%(address-imagebase) +";" + "none" + "\n"
             print (output)
             f.write(output) 
        if idc.get_cmt(address,1) is not None:#           
             output= "comments"+";" + idc.get_cmt(address,0) + ";" + "0x%08x"%(address-imagebase) +";" + "none" + "\n"
             print (output)
             f.write(output) 
f.close()