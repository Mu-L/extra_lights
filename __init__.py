# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Extra Lights",
    "author": "Jonathan Lampel",
    "version": (1, 1),
    "blender": (2, 91, 0),
    "location": "View3D > Add > Light",
    "description": "Adds new preset light objects based on real world values",
    "warning": "",
    "doc_url": "",
    "category": "Add Light",
}

from . import ui

def register():
    ui.register()

def unregister():
    ui.unregister()
