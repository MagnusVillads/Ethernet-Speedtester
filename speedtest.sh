echo Angiv Filnavn
read filnavn
echo
echo Læn Dig Tilbage Mens Jeg Klare Arbejdet
echo
python -u speedtest.py | tee $filnavn
echo
echo Din Test Er Færdig
echo
echo Credit: Magnus Villads

