# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# Authors: Axel Huebl
from spack import *


class Graybat(CMakePackage):
    """Graph Approach for Highly Generic Communication Schemes Based on Adaptive Topologies"""

    homepage = "https://github.com/ComputationalRadiationPhysics/graybat"
    url      = "https://github.com/ComputationalRadiationPhysics/graybat/archive/1.2.0.tar.gz"
    maintainers = ['ax3l']

    # version('develop', branch='remove_grpc',
    #         git='https://github.com/fabian-jung/graybat.git')
    version('develop', branch='dev',
            git='https://github.com/ComputationalRadiationPhysics/graybat.git')
    version('master', branch='master',
            git='https://github.com/ComputationalRadiationPhysics/graybat.git')
    # todo: only add first working version
    version('1.2.0', 'd47200e99d712d33e6e6a5f0ad946c6a')

    # this should not be necessary when all variants are properly optional
    build_targets = ['all', 'signaling']

    # C++14
    conflicts('%gcc@:5')
    conflicts('%clang@:3.4')

    variant('mpi', default=True,
            description='Enable MPI communication policy')
    variant('zeromq', default=True,
            description='Enable ZeroMQ communication policy')
    variant('metis', default=False,
            description='Enable graph partitioning mapping')
    variant('grpc', default=True,
            description='Enable gRPC signaling')

    depends_on('cmake@3.0.2:', type='build')
    depends_on('boost@1.61.0:1.62.0~mpi', type='link', when='~mpi')
    depends_on('boost@1.61.0:1.62.0+mpi', type='link', when='+mpi')
    depends_on('mpi', type='link', when='+mpi')
    depends_on('cppzmq@4.2.2:', type='link', when='+zeromq')
    depends_on('metis@5.1.0:', type='link', when='+metis')
    depends_on('protobuf@3.4.0:')  # , when='@:1.2.0')
    depends_on('grpc@1.6.0+shared', when='+grpc')

    def setup_run_environment(self, env):
        env.prepend_path('CMAKE_PREFIX_PATH', join_path(self.prefix, 'include/graybat/utils/cmake/modules/'))
