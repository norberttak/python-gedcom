# -*- coding: utf-8 -*-

# Python GEDCOM Parser
#
# Copyright (C) 2018 Damon Brodie (damon.brodie at gmail.com)
# Copyright (C) 2018-2019 Nicklas Reincke (contact at reynke.com)
# Copyright (C) 2016 Andreas Oberritter
# Copyright (C) 2012 Madeleine Price Ball
# Copyright (C) 2005 Daniel Zappala (zappala at cs.byu.edu)
# Copyright (C) 2005 Brigham Young University
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Further information about the license: http://www.gnu.org/licenses/gpl-2.0.html

from gedcom.element.element import Element
import gedcom.tags


class NotAnActualFamilyError(Exception):
    pass


class FamilyElement(Element):

    def is_family(self):
        """Checks if this element is an actual family
        :rtype: bool
        """
        return self.get_tag() == gedcom.tags.GEDCOM_TAG_FAMILY

    def get_marrige_detail(self):
        husband_ptr = ""
        wife_ptr = ""
        place = ""
        date = ""
        for element in self.get_child_elements():
            if element.get_tag() == gedcom.tags.GEDCOM_TAG_HUSBAND:
                husband_ptr = element.get_value()
            if element.get_tag() == gedcom.tags.GEDCOM_TAG_WIFE:
                wife_ptr = element.get_value()
            if element.get_tag() == gedcom.tags.GEDCOM_TAG_MARRIAGE:
                for marr_element in element.get_child_elements():
                    if marr_element.get_tag() == gedcom.tags.GEDCOM_TAG_PLACE:
                        place = marr_element.get_value()
                    if marr_element.get_tag() == gedcom.tags.GEDCOM_TAG_DATE:
                        date = marr_element.get_value()
        return (husband_ptr, wife_ptr, date, place)
