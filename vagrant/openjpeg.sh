NUMTHREADS=2
if [[ -f /sys/devices/system/cpu/online ]]; then
    # Calculates 1.5 times physical threads
    NUMTHREADS=$(( ( $(cut -f 2 -d '-' /sys/devices/system/cpu/online) + 1 ) * 15 / 10  ))
fi
#NUMTHREADS=1 # disable MP
export NUMTHREADS

cd /vagrant
if [ ! -f openjpeg-2.0.0.tar.gz ]; then
    wget http://sourceforge.net/projects/openjpeg.mirror/files/openjpeg-2.0.0.tar.gz/download -O openjpeg-2.0.0.tar.gz
fi
tar xvzf openjpeg-2.0.0.tar.gz
cd openjpeg-2.0.0
mkdir build
cd build
cmake ..

make -j $NUMTHREADS
sudo make install

cd
