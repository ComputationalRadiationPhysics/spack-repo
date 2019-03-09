# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# Authors: Axel Huebl
from spack import *


class Grpc(CMakePackage):
    """A high performance, open-source universal RPC framework"""

    homepage = "https://grpc.io"
    url      = "https://github.com/grpc/grpc/archive/v1.6.0.tar.gz"
    maintainers = ['ax3l']

    version('develop', branch='master',
            git='https://github.com/grpc/grpc.git')

    version('1.6.0', '0142fc5ea622d996376bd4eebff07d00')

    variant('shared', default=True,
            description='Build shared libraries (else static)')

    depends_on('cmake@3.0.0:', type='build')
    depends_on('protobuf@3.4.0:')
    depends_on('zlib')
    depends_on('openssl')
    depends_on('cares@1.13.0:')
    depends_on('gflags')
    depends_on('benchmark@1.2.0:')

    def cmake_args(self):
        spec = self.spec

        args = [
            '-DgRPC_ZLIB_PROVIDER=package',
            '-DgRPC_PROTOBUF_PROVIDER=package',
            '-DgRPC_PROTOBUF_PACKAGE_TYPE=CONFIG',
            '-DgRPC_SSL_PROVIDER=package',
            '-DgRPC_CARES_PROVIDER=package',
            '-DgRPC_GFLAGS_PROVIDER=package',
            '-DgRPC_BENCHMARK_PROVIDER=package',
            '-DBUILD_SHARED_LIBS={0}'.format((
                'ON' if '+shared' in spec else 'OFF'))
        ]
        return args
