##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
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


class Openpmd(CMakePackage):
    """API for easy reading and writing of openPMD files"""

    homepage = "http://www.openPMD.org"
    url      = "https://github.com/ComputationalRadiationPhysics/archive/1.0.0.tar.gz"
    maintainers = ['ax3l']

    version('develop', branch='dev',
            git='https://github.com/ComputationalRadiationPhysics/libopenPMD.git')

    variant('mpi', default=True,
            description='Enable parallel I/O')
    variant('hdf5', default=True,
            description='Enable HDF5 support')
    variant('adios1', default=True,
            description='Enable ADIOS1 support')
    # variant('adios2', default=True,
    #         description='Enable ADIOS2 support')
    # variant('json', default=True,
    #         description='Enable JSON support')
    variant('python', default=True,
            description='Enable Python bindings')

    depends_on('cmake@3.10.0:', type='build')
    depends_on('boost@1.62.0:')
    depends_on('mpi@2.3:', when='+mpi')  # might become MPI 3.0+
    depends_on('hdf5@1.8.6:', when='+hdf5')
    depends_on('hdf5@1.8.6: +mpi', when='+mpi +hdf5')
    depends_on('adios@1.10.0:', when='+adios1')
    depends_on('adios@1.10.0: +mpi', when='+mpi +adios1')
    depends_on('adios2', when='+adios2')
    depends_on('adios2 +mpi', when='+mpi +adios2')
    depends_on('pybind11@2.2.1:', when='+python')  # ideally we want 2.3.0+ for full C++11 CT function signature support

    def cmake_args(self):
        spec = self.spec

        args = [
            '-DopenPMD_USE_MPI:BOOL={0}'.format(
                'ON' if '+mpi' in spec else 'OFF'),
            '-DopenPMD_USE_HDF5:BOOL={0}'.format(
                'ON' if '+hdf5' in spec else 'OFF'),
            '-DopenPMD_USE_ADIOS1:BOOL={0}'.format(
                'ON' if '+adios1' in spec else 'OFF'),
            # '-DopenPMD_USE_ADIOS2:BOOL={0}'.format(
            #     'ON' if '+adios2' in spec else 'OFF'),
            # '-DopenPMD_USE_JSON:BOOL={0}'.format(
            #     'ON' if '+json' in spec else 'OFF'),
            '-DopenPMD_USE_PYTHON:BOOL={0}'.format(
                'ON' if '+python' in spec else 'OFF')
        ]
        return args
