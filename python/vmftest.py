var = "1428"
with open("newVMF.vmf","w") as file:
	file.write('versioninfo')
	file.close()

with open("newVMF.vmf","a") as file:
	file.write('\n{')
	file.close()
	
with open("newVMF.vmf","a") as file:
	file.write('\n\t"editorversion" "' + var + '"')
	file.close()

with open("newVMF.vmf","a") as file:
	file.write('\n\t"editorbuild" "9008"')
	file.close()

with open("newVMF.vmf","a") as file:
	file.write('\n\t"mapversion" "1"')
	file.close()

with open("newVMF.vmf","a") as file:
	file.write('\n\t"formatversion" "100"')
	file.close()
	
with open("newVMF.vmf","a") as file:
	file.write('\n\t"prefab" "0"')
	file.close()

with open("newVMF.vmf","a") as file:
	file.write('\n}')
	file.close()
	
	pass