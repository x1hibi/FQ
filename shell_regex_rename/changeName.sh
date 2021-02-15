#!/usr/bin/env bash

echo "#Welcome to change name script!"

echo "#Frist get all filesnames and save as array"

# get all file name as a list !!!
echo insert the file extension of the files to modify
read extension
	
extensionSize=${#extension}
filenames=$(ls | grep ""$extension"$")

echo the ext is ${#extension}

if [[ -z $filenames ]]
then 
	echo "Don't found any coincidences"
fi


echo ${filenames[@]}

echo ${#filenames[@]}


echo "#we iterate each of them"

# we iterate each name as a list not as a array

for i in ${filenames[@]}
do
	echo actual name: $i
	echo actual name less identifier
	filenameSize=${#i}
	filenameLenght=$((filenameSize-extensionSize))
	echo the filename lenght is $filenameLenght
	echo the size of extension is $extensionSize
	echo $i | cut -c1-$filenameLenght
	newName="${i}-test"
	echo new name: $newName
	#mv $i $newName
done


