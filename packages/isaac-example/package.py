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


class IsaacExample(CMakePackage):
    """In Situ Animation of Accelerated Computations: Example Visualization Plugin"""

    homepage = "http://computationalradiationphysics.github.io/isaac/"
    url      = "https://github.com/ComputationalRadiationPhysics/isaac/archive/v1.3.1.tar.gz"

    version('develop', branch='dev',
            git='https://github.com/ComputationalRadiationPhysics/isaac.git')
    version('master', branch='master',
            git='https://github.com/ComputationalRadiationPhysics/isaac.git')
    version('1.3.1', '7fe075f9af68d05355eaba0e224f20ca')

    variant('cuda', default=False,
            description='Generate CUDA example for Nvidia GPUs')
    variant('alpaka', default=True,
            description='Generate CPU example via Alpaka (OpenMP 2)')

    depends_on('cmake@3.3:', type='build')
    depends_on('isaac+cuda', type='link', when='+cuda')
    depends_on('isaac~cuda', type='link', when='~cuda')
    depends_on('icet') # aww....
    depends_on('alpaka', type='link', when='+alpaka')

    root_cmakelists_dir = 'example'

    def cmake_args(self):
        spec = self.spec

        args = [
            '-DISAAC_CUDA:BOOL={0}'.format((
                'ON' if '+cuda' in spec else 'OFF')),
            '-DISAAC_ALPAKA:BOOL={0}'.format((
                'ON' if '+alpaka' in spec else 'OFF')),
            '-DISAAC_DIR={0}'.format(
                spec['isaac'].prefix)
        ]
        if '+alpaka' in spec:
            args.append('-DALPAKA_ROOT={0}'.format(
                spec['alpaka'].prefix))
            if '~cuda' in spec:
                args.append('-DALPAKA_ACC_GPU_CUDA_ENABLE:BOOL=OFF')
        return args

    def install(self, spec, prefix):
        if '+alpaka' in spec:
            install('spack-build/example_alpaka', prefix.bin)
        if '+cuda' in spec:
            install('spack-build/example_cuda', prefix.bin)
