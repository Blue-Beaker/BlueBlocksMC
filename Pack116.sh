#! /bin/bash
cd ./"BlueBlocksCraft 1.16"/
zip -0 -FS -r BlueBlocksCraft-1.16.zip * -x='*.pdn' -x='*.png~'
cd ..
mv ./"BlueBlocksCraft 1.16"/BlueBlocksCraft-1.16.zip ./
