for i in **/*.txt; do
sed -i s/oldstring/newstring/ $i &
done
