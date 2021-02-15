#!/usr/bin/env bash

echo "Welcome to change name script!"

# Declare a condition for loop

condition=0

# Loop menu 
while (( $condition == 0 ))
do
	# Select action
	echo "Typed your option:"
	echo "1) Insert a patter"
	echo "2) Exit"
	read option
	if (( $option == 2 ))
	then
		# Exit of the script 
		break
	elif (( $option == 1))
	then
		echo "Insert your patter to get all files name in current directory to modify"
		read patter
		# Check if the patter have conincidences 
		if (( $patter==1 ))
		then 
			echo "god patter"
			# break loop condition=1
		else
			# message display if the number of coincidences are zero 
			echo "non coincidences with typed patter."
	
		fi
	fi
	
done

echo "Thank you to use x1hibi script!"

