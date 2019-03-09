# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# Authors: Axel Huebl
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
    # version('0.3.4',
    #     sha256='fbe6778568817761c70c4302bb4e876db736a002120b668330026dc5f17e05d7')
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
        for troll in [".gitignore", ".travis.yml", ".zenodo.json", "LICENSE", "README.md"]:
            install(troll, prefix)

    #def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
    #    spack_env.prepend_path(
    #        'CMAKE_MODULE_PATH',
    #        join_path(self.prefix, 'cmake')
    #    )
