#! /bin/bash
cd ./"BlueBlocksCraft 1.16"/
zip -1 -FS -r BlueBlocksCraft-1.16.zip * -x='*.pdn' -x='*.png~' -x='*.cubik' -x='*deprecated*'
cd ..
mv ./"BlueBlocksCraft 1.16"/BlueBlocksCraft-1.16.zip ./
