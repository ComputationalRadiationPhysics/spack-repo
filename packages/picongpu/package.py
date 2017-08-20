##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Picongpu(Package):
    """PIConGPU: A particle-in-cell code for GPGPUs"""

    homepage = "https://github.com/ComputationalRadiationPhysics/picongpu"
    url      = "https://github.com/ComputationalRadiationPhysics/picongpu/archive/0.4.0.tar.gz"

    version('develop', branch='dev',
            git='https://github.com/ComputationalRadiationPhysics/picongpu.git')
    # version('master', branch='master',
    #         git='https://github.com/ComputationalRadiationPhysics/picongpu.git')
    # version('0.4.0', '')

    # Alpaka computing backends.
    # Accepted values are:
    #   cuda  - Nvidia CUDA (GPUs)
    #   omp2b - OpenMP 2.0 with grid-blocks parallel, sequential block-threads
    variant('backend', default='cuda',
            values=('cuda', 'omp2b'),
            multi=False,
            description='Control the computing backend')
    variant('cudacxx', default='nvcc',
            values=('nvcc', 'clang'),
            multi=False,
            description='Device compiler for the CUDA backend')
    variant('png', default=True,
            description='Enable the PNG plugin')
    variant('hdf5', default=True,
            description='Enable multiple plugins requiring HDF5')
    variant('adios', default=False,
            description='Enable the ADIOS plugin')
    variant('isaac', default=False,
            description='Enable the ISAAC plugin')

    # @TODO add type=('link, 'run') to all these?
    # @TODO define supported ranges instead of fixed versions
    depends_on('cmake@3.7:3.9', type='build')
    depends_on('cuda@8.0.61', when='backend=cuda')
    depends_on('zlib@1.2.11')
    depends_on('boost@1.62.0')
    # depends_on('mpi@2.3:')
    depends_on('openmpi@2.1.1')
    depends_on('pngwriter@0.6.0', when='+png')
    depends_on('libsplash@1.6.0 ^hdf5~fortran', when='+hdf5')
    depends_on('adios@1.10.0', when='+adios')
    depends_on('isaac@1.3.1', when='+isaac')
    depends_on('isaac-server@1.3.1', type='run', when='+isaac')

    # shipped internal dependencies
    # @TODO get from extern!
    # alpaka, cupla, cuda-memtest, mallocMC, mpiInfo, CRP's cmake-modules

    # C++11
    conflicts('%gcc@:4.8')
    conflicts('%clang@:3.4')

    # NVCC host-compiler incompatibility list
    #   https://gist.github.com/ax3l/9489132
    conflicts('%gcc@5:', when='backend=cuda cudacxx=nvcc ^cuda@:7.5')
    conflicts('%gcc@6:', when='backend=cuda cudacxx=nvcc ^cuda@:8')
    conflicts('%gcc@7:', when='backend=cuda cudacxx=nvcc ^cuda@:9')
    conflicts('%clang@:3.4,3.7:', when='backend=cuda cudacxx=nvcc ^cuda@7.5')
    conflicts('%clang@:3.7,4:', when='backend=cuda cudacxx=nvcc ^cuda@8:9')
    conflicts('%intel@:14,16:', when='backend=cuda cudacxx=nvcc ^cuda@7.5')
    conflicts('%intel@:14,17:', when='backend=cuda cudacxx=nvcc ^cuda@8.0.44')
    conflicts('%intel@:14,18:', when='backend=cuda cudacxx=nvcc ^cuda@8.0.61:9')

    def install(self, spec, prefix):
        install_tree('bin', join_path(prefix, 'bin'))
        install_tree('buildsystem', join_path(prefix, 'buildsystem'))
        install_tree('etc', join_path(prefix, 'etc'))
        install_tree('include', join_path(prefix, 'include'))
        install_tree('src', join_path(prefix, 'src'))
        install_tree('share', join_path(prefix, 'share'))
        install_tree('thirdParty', join_path(prefix, 'thirdParty'))
        install('pic-build', prefix)
        install('pic-compile', prefix)
        install('pic-configure', prefix)
        install('pic-create', prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PICSRC', self.prefix)
        # note: still a PIC_PROFILE export and/or picongpu.profile expected
        run_env.prepend_path('PATH', self.prefix)
        run_env.prepend_path('PATH',
                             join_path(self.prefix, 'src/tools/bin'))
        run_env.prepend_path('PYTHONPATH',
                             join_path(self.prefix, 'src/tools/lib/python'))
        # optional: default for TBG_SUBMIT, TBG_TPLFILE
