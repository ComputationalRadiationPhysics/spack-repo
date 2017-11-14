export PIC_PROFILE=$(cd $(dirname $BASH_SOURCE) && pwd)"/"$(basename $BASH_SOURCE)

. @PIC_SPACK_ROOT@/share/spack/setup-env.sh

spack load @PIC_SPACK_COMPILER@
spack load --dependencies @PIC_SPACK_SPEC@
