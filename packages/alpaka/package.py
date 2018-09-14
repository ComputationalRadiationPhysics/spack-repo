##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
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


class Alpaka(Package):
    """Abstraction Library for Parallel Kernel Acceleration"""

    homepage = "https://github.com/ComputationalRadiationPhysics/alpaka"
    url      = "https://github.com/ComputationalRadiationPhysics/alpaka/archive/0.2.0.tar.gz"
    maintainers = ['ax3l']

    version('develop', branch='develop',
            git='https://github.com/ComputationalRadiationPhysics/alpaka.git')
    # version('master', branch='master',
    #         git='https://github.com/ComputationalRadiationPhysics/alpaka.git')
    # version('0.2.0', 'bd778afe300731c935a415ec73fb18b8')
    # version('0.1.0', '744546f1984093db416d93b691945015')

    # depends_on('cmake@3.7:', type='build')

    def install(self, spec, prefix):
        install_tree('cmake', join_path(prefix, 'cmake'))
        install_tree('doc', join_path(prefix, 'doc'))
        install_tree('include', join_path(prefix, 'include'))
        install('alpakaConfig.cmake', prefix)
        install('CMakeLists.txt', prefix)
        install('Findalpaka.cmake', prefix)
        # awww
        for troll in [".gitignore", ".travis.yml", ".zenodo.json", ".appveyor.yml", "COPYING", "COPYING.LESSER", "README.md"]:
            install(troll, prefix)

    #def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
    #    spack_env.prepend_path(
    #        'CMAKE_MODULE_PATH',
    #        join_path(self.prefix, 'cmake')
    #    )
