#! /bin/bash
cd ./"BlueBlocksCraft 1.12.2"/
zip -0 -FS -r BlueBlocksCraft-1.12.zip * -x='*.pdn' -x='*.png~' -x='*.cubik' -x='*deprecated*'
cd ..
mv ./"BlueBlocksCraft 1.12.2"/BlueBlocksCraft-1.12.zip ./
