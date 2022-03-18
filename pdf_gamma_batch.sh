for i in [^G2_]*.pdf; do
mutool draw -G 2 -r 300 -o temp.ps $i
ps2pdf temp.ps "G2_"$i
done
