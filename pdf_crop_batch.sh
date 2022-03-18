for i in *.pdf; do
pdfcrop --hires $i $i
done
