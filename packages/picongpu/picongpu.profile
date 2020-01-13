export PIC_PROFILE=$(cd $(dirname $BASH_SOURCE) && pwd)"/"$(basename $BASH_SOURCE)

. @PIC_SPACK_ROOT@/share/spack/setup-env.sh

# optional: compiler, if not regular system compiler
spack load @PIC_SPACK_COMPILER@ >/dev/null 2>&1 || echo "using default compiler"

# required: PIConGPU and its dependencies
spack load -r @PIC_SPACK_SPEC@

# activate bash completion if available
PIC_COMP_FILE=$PICSRC/bin/picongpu-completion.bash
if [ -f $PIC_COMP_FILE ] ; then
    source PIC_COMP_FILE
fi
