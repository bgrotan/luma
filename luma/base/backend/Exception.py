# -*- coding: utf-8 -*-
#
# base.backend.Exception
#
# Copyright (c) 2011
#     Einar Uvsløkk, <einar.uvslokk@linux.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/

__all__ = ['LumaConnectionException', 'ServerCertificateException',
           'InvalidPasswordException']


class LumaConnectionException(Exception):
    """This exception class will be raised if no proper server object
    is passed to the LumaConnection constructor.
    """
    pass


class ServerCertificateException(Exception):
    """This exception will be raised if we get an certificate error.
    """
    pass


class InvalidPasswordException(Exception):
    """This exception will be raised when a password is needed to
    proceed with a bind operation. This normaly occurs when the
    given password is either invalid or blank.
    """
    pass


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
