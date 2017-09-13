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


class Grpc(CMakePackage):
    """A high performance, open-source universal RPC framework"""

    homepage = "https://grpc.io"
    url      = "https://github.com/grpc/grpc/archive/v1.6.0.tar.gz"

    version('develop', branch='master',
            git='https://github.com/grpc/grpc.git')

    version('1.6.0', '0142fc5ea622d996376bd4eebff07d00')

    depends_on('cmake@3.0.0:', type='build')
    depends_on('protobuf@3.4.0:')
    depends_on('zlib')
    depends_on('openssl')
    depends_on('cares@1.13.0:')
    depends_on('gflags')
    depends_on('benchmark@1.2.0:')

    def cmake_args(self):
        args = [
            '-DgRPC_ZLIB_PROVIDER=package',
            '-DgRPC_PROTOBUF_PROVIDER=package',
            '-DgRPC_PROTOBUF_PACKAGE_TYPE=CONFIG',
            '-DgRPC_SSL_PROVIDER=package',
            '-DgRPC_CARES_PROVIDER=package',
            '-DgRPC_GFLAGS_PROVIDER=package',
            '-DgRPC_BENCHMARK_PROVIDER=package'
        ]
        return args
