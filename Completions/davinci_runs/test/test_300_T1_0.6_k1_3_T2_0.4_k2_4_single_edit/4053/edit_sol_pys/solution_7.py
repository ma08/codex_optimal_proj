#!/bin/bash

#
# This script is used to fix syntax errors in the source code.
#
# It will not fix indentation errors.
#

#
# Fix syntax errors in the source code.
#
# The -i option is used to edit the file in place.
#

#
# Remove trailing whitespace.
#
sed -i 's/[ \t]*$//' *.cpp *.h

#
# Remove spaces before semicolons.
#
sed -i 's/[ \t]\+;/;/g' *.cpp *.h

#
# Remove spaces before opening parentheses.
#
sed -i 's/[ \t]\+([(]/([(]/g' *.cpp *.h

#
# Remove spaces before closing parentheses.
#
sed -i 's/[ \t]\+[)]/)/g' *.cpp *.h

#
# Remove spaces before opening braces.
#
sed -i 's/[ \t]\+{/{/g' *.cpp *.h

#
# Remove spaces before closing braces.
#
sed -i 's/[ \t]\+}/}/g' *.cpp *.h

#
# Remove spaces before commas.
#
sed -i 's/[ \t]\+,/,/g' *.cpp *.h

#
# Remove spaces before colons.
#
sed -i 's/[ \t]\+:/:/g' *.cpp *.h

#
# Remove spaces before asterisks.
#
sed -i 's/[ \t]\+\*/\*/g' *.cpp *.h

#
# Remove spaces before ampersands.
#
sed -i 's/[ \t]\+&/&/g' *.cpp *.h

#
# Remove spaces before equal signs.
#
sed -i 's/[ \t]\+=/=/g' *.cpp *.h

#
# Remove spaces before plus signs.
#
sed -i 's/[ \t]\+\+/\+/g' *.cpp *.h

#
# Remove spaces before minus signs.
#
sed -i 's/[ \t]\+-/-/g' *.cpp *.h

#
# Remove spaces before less than signs.
#
sed -i 's/[ \t]\+</</g' *.cpp *.h

#
# Remove spaces before greater than signs.
#
sed -i 's/[ \t]\+>/>/g' *.cpp *.h

#
# Remove spaces before exclamation points.
#
sed -i 's/[ \t]\+\!/\!/g' *.cpp *.h

#
# Remove spaces before question marks.
#
sed -i 's/[ \t]\+\?/?/g' *.cpp *.h

#
# Remove spaces before percent signs.
#
sed -i 's/[ \t]\+%/%/g' *.cpp *.h

#
# Remove spaces before forward slashes.
#
sed -i 's/[ \t]\+\//\//g' *.cpp *.h

#
# Remove spaces before backslashes.
#
sed -i 's/[ \t]\+\\/\\/g' *.cpp *.h

#
# Remove spaces before vertical bars.
#
sed -i 's/[ \t]\+|/|/g' *.cpp *.h

#
# Remove spaces before carets.
#
sed -i 's/[ \t]\+\^/\^/g' *.cpp *.h

#
# Remove spaces before tildes.
#
sed -i 's/[ \t]\+~/~/g' *.cpp *.h

#
# Remove spaces before double quotes.
#
sed -i 's/[ \t]\+\"/\"/g' *.cpp *.h

#
# Remove spaces before single quotes.
#
sed -i "s/[ \t]\+\'/\'/g" *.cpp *.h

#
# Remove spaces before periods.
#
sed -i 's/[ \t]\+././g' *.cpp *.h

#
# Remove spaces before octothorpes.
#
sed -i 's/[ \t]\+#/#/g' *.cpp *.h

#
# Remove spaces before at signs.
#
sed -i 's/[ \t]\+@/@/g' *.cpp *.h

#
# Remove spaces before dollar signs.
#
sed -i 's/[ \t]\+\$/\$/g' *.cpp *.h

#
# Remove spaces before pound signs.
#
sed -i 's/[ \t]\+\£/\£/g' *.cpp *.h

#
# Remove spaces before backticks.
#
sed -i 's/[ \t]\+\`/\`/g' *.cpp *.h

#
# Remove spaces before underscores.
#
sed -i 's/[ \t]\+_/_/g' *.cpp *.h

#
# Remove spaces before curly braces.
#
sed -i 's/[ \t]\+\{/\{/g' *.cpp *.h

#
# Remove spaces before square brackets.
#
sed -i 's/[ \t]\+\[/\[/g' *.cpp *.h

#
# Remove spaces before angle brackets.
#
sed -i 's/[ \t]\+\</\</g' *.cpp *.h

#
# Remove spaces before tildes.
#
sed -i 's/[ \t]\+\~/\~/g' *.cpp *.h

#
# Remove spaces before equal signs.
#
sed -i 's/[ \t]\+=\+/\+/g' *.cpp *.h

#
# Remove spaces before exclamation points.
#
sed -i 's/[ \t]\+\!\=/\!\=/g' *.cpp *.h

#
# Remove spaces before backslashes.
#
sed -i 's/[ \t]\+\\\//\\\//g' *.cpp *.h

#
# Remove spaces before colons.
#
sed -i 's/[ \t]\+\:\\:/\:\\:/g' *.cpp *.h

#
# Remove spaces before vertical bars.
#
sed -i 's/[ \t]\+\|\|/\|\|/g' *.cpp *.h

#
# Remove spaces before ampersands.
#
sed -i 's/[ \t]\+\&\&/\&\&/g' *.cpp *.h

#
# Remove spaces before less than signs.
#
sed -i 's/[ \t]\+\<\=/\<\=/g' *.cpp *.h

#
# Remove spaces before greater than signs.
#
sed -i 's/[ \t]\+\>\=/\>\=/g' *.cpp *.h

#
# Remove spaces before less than signs.
#
sed -i 's/[ \t]\+\<\</\<\</g' *.cpp *.h

#
# Remove spaces before greater than signs.
#
sed -i 's/[ \t]\+\>\>/\>\>/g' *.cpp *.h

#
# Remove spaces before less than signs.
#
