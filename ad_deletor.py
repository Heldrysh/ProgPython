'''
VERSION
	0.1
	Python3.8
AUTHOR
	Fuentes Mendez David Gregorio
DESCRIPTION
	Simple FASTA editor
CATEGORY
	Editor
USAGE
	Deletes adaptator sequence from FASTA file
ARGUMNETS
SEE ALSO
'''
Valid=["a","A","t","T","c","C","g","G","\n"]

print("ELIMINADOR DE ADAPTADORES \n")

#Insertion of sequence to edit#
m=0
while m == 0:
	option = int(input("Desea: \n1.Insertar la secuencia a editar 2.Insertar archivo FASTA a editar \n\t="))

	error=1
	while error>0:
		m = m + 1					#This WHILE repeats the input insertion if any errors occur#
		if (option == 1):								#If the user chooses to insert a sequence, here we scan an user-given sequence#
			reads = str(input("\nEscriba la secuencia: ")) 
			error=0											
			for x in reads:								#Then, with this FOR we check if the user has inserted invalid characters#
				if (not(x in Valid)):
					print("\nSe introdujeron caracteres no validos\n")
					error=1
					break
		elif (option == 2):								#If the user chooses to insert a file, here we scan the absolute rute to that file# 
			fasta_doc = str(input("\nRuta absoluta del archivo: "))
			error=0
			if not ".fasta" in fasta_doc:				#Here we check if the file name has a .fasta extension#
				print("\nNo se introdujo archivo FASTA\n")
				error=1
			else:
				try:
				    check = open(fasta_doc)				#We need to check if the file exists in order to repeat the input insertion (WHILE)#
				except IOError:
				    print("\nArchivo no encontrado\n")
				    error=1
			if error == 0:										
				with open(fasta_doc, "r") as fasta:		#Then we open that file, and save the data in the reads variable# 
					reads = fasta.read()
				for line in reads:
					if line.startswith('>'):				
						continue						#This FOR checks and deletes non-nucleic acid characters, such as non 'atcg' letters, new-line characters (\n) and spaces.#
					if not line in Valid:				#Ignores those from fragment headers.#
						reads = reads.replace(x, '')	#Then rewrites the string in the same variable#
		else:
			print ("\nOpcion no valida, intente otra vez\n")
			m=0
			break

		if error == 1 and m % 3 == 0:			#Here we ask the user if he wants to choose another insertion option each time he gets 3 insertion failures#
			while error:
				toomany = input("Han ocurrido 3 fallos. \n ¿Quieres escoger otra opcion de insercion? (y or n): ")
				if toomany == "y":
					error=0
					m=0
					break
				elif toomany == "n":
					error=1
					break
				else:
					print ("\nOpcion no valida, intente de nuevo\n")

#Insertion of adapting sequence#
m=0
while m == 0:
	option = int(input("Desea: \n1.Insertar la secuencia de adaptador 2.Insertar archivo FASTA de adaptador\n\t="))

	error=1
	while error>0:
		m = m + 1					#This WHILE repeats the input insertion if any errors occur#
		if (option == 1):								#If the user chooses to insert a sequence, here we scan an user-given sequence#
			adapt = str(input("\nEscriba la secuencia: ")) 
			error=0											
			for x in adapt:								#Then, with this FOR we check if the user has inserted invalid characters#
				if (not(x in Valid)):
					print("\nSe introdujeron caracteres no validos\n")
					error=1
					break
		elif (option == 2):								#If the user chooses to insert a file, here we scan the absolute rute to that file# 
			fasta_adp = str(input("\nRuta absoluta del archivo: "))
			error=0
			if not ".fasta" in fasta_adp:				#Here we check if the file name has a .fasta extension#
				print("\nNo se introdujo archivo FASTA\n")
				error=1
			else:
				try:
				    check = open(fasta_adp)				#We need to check if the file exists in order to repeat the input insertion (WHILE)#
				except IOError:
				    print("\nArchivo no encontrado\n")
				    error=1
			if error == 0:										
				with open(fasta_adp, "r") as fasta_a:	#Then we open that file, and save the data in the reads variable 
					adapt = fasta_a.read()
				for line in adapt:						#This FOR checks and deletes non-nucleic acid characters, such as those from fragment headers, new-line characters (\n) and spaces.#
					if not line in Valid:				#Then rewrites the string in the same variable#
						adapt = adapt.replace(x, '')
		else:
			print ("\nOpcion no valida, intente otra vez\n")
			m=0
			break

		if error == 1 and m % 3 == 0:			#Here we ask the user if he wants to choose another insertion option each time he gets 3 insertion failures#
			while error:
				toomany = input("Han ocurrido 3 fallos. \n ¿Quieres escoger otra opcion de insercion? (y or n): ")
				if toomany == "y":
					error=0
					m=0
					break
				elif toomany == "n":
					error=1
					break
				else:
					print ("\nOpcion no valida, intente de nuevo\n")

#Deletion of sequence#
newfile = fasta_doc.replace(".fasta","_wthout-adaptators.fasta")
edited_fasta = open(newfile,"w+")

counter = 0
fsf = 0
for line in reads:
	counter++
	if line.startswith('>'):
		fsf = counter
		#(fragment start flag)#
		continue
	if (not fsf == 0) and ( counter == (fsf + 1) ): #Given that the fasta has alot of lines, and we just want to edit the fist one (supposing that the adapting sequence
		edited_fasta = reads.replace(adapt, '')     #is smaller than the line lenght), we need this IF to exclude comparison with the other lines#

print('The new edited fasta file is: {}'.format(newfile))