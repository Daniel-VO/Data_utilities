for i in *.pdf; do
pdftoppm $i $i -png -r 600 &
done
