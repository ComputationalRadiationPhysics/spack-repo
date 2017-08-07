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


class Openpmd(CMakePackage):
    """API for easy reading and writing of openPMD files"""

    homepage = "http://www.openPMD.org"
    url      = "https://github.com/google/benchmark/archive/1.0.0.tar.gz"

    version('develop', branch='dev',
            git='https://github.com/ComputationalRadiationPhysics/libopenPMD.git')

    variant('mpi', default=True,
            description='Enable parallel I/O')

    depends_on('cmake@3.5.1:', type='build')
    depends_on('mpi', when='+mpi')
    depends_on('hdf5')
    depends_on('hdf5+mpi', when='+mpi')
    depends_on('adios2')
    depends_on('adios2+mpi', when='+mpi')

