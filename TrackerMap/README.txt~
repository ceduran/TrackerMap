
STEPS:

1) You need to get any new release CMSSW_7_X (we use CMSSW_7_1_0) and then
execute "cmsenv".

2) You need to have a file with cabling information, in our case it is
CablingInfo_Run100357.txt

Our code  "Cabling_function.py" gets information of
CablingInfo_Run100357.txt, makes a dictionary of dictionaries with it,
and a .txt file.

3)When you run the code you get a file called "data.txt" (a list of "detids" and
"value", by now a single entry for each detid). In order to run the script you only
type:
python Cabling_function.py

4) Then you type the command "print_TrackerMap" (Mail Andrea was very
clear then we copy and paste, sorry). This command works this way

print_TrackerMap $2 "$3" $4 $5 $6 $7 $8 $9
where:
$2 is the ASCII file with two columns: detid and values
$3 is the title which will be printed on the map
$4 is the output file name (I am using png, I do not know/remember if it
recognizes automatically other formats)
$5 is the horizontal size: 2400 is the default. The vertical size is
computed properly by the code to keep the correct aspect ratio
$6 is True or False depending on whether you (don't) want the log scale
$7 is True, False, Only depending on whether you want to have _also_ the
pixel detector, you don't want it, or you want _only_ the pixel detector
$8 and $9 are the min and max values.

IN OUR CASE FOR EXAMPLE IT WAS:
print_TrackerMap data.txt trackermap maptracker.png 2400 False True 999 -999
