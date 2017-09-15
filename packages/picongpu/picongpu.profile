export PIC_PROFILE=$(cd $(dirname $BASH_SOURCE) && pwd)"/"$(basename $BASH_SOURCE)

spack load @PIC_SPACK_COMPILER@
spack load @PIC_SPACK_SPEC@
