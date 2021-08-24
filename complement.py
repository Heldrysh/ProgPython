'''
VERSION
	0.2
	Python3.8
AUTHOR
	Fuentes Mendez David Gregorio
DESCRIPTION
	Simple FASTA lector
CATEGORY
	Reader
USAGE
	Counts AT in genomic sequence
ARGUMNETS
      Formato tipo FASTA y ej
SEE ALSO
'''
Valid=["a","A","t","T","c","C","g","G"]
VALID=["A","T","C","G"]
valid=["a","t","c","g"]

print("COMPLEMENTO DE SECUENCIA \n")

m=0
while m == 0:
	option = int(input("Desea: \n1.Insertar la secuencia 2.Insertar archivo FASTA \n\t="))

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
				with open(fasta_doc, "r") as fasta:		#Then we open that file, and save the data in the reads variable 
					reads = fasta.read()
				for x in reads:							#This FOR checks and deletes non-nucleic acid characters, such as those from fragment headers, new-line characters (\n) and spaces.#
					if not x in Valid:					#Then rewrites the string in the same variable#
						reads = reads.replace(x, '')
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

reads = reads.replace('a','A')
reads = reads.replace('c','C')
reads = reads.replace('g','G')
reads = reads.replace('t','T')

reads = reads.replace('A','t')
reads = reads.replace('C','g')
reads = reads.replace('G','c')
reads = reads.replace('T','a')

reads = reads.replace('a','A')
reads = reads.replace('c','C')
reads = reads.replace('g','G')
reads = reads.replace('t','T')

print(reads)
